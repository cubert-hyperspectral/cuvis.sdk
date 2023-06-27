#pragma once

/** @file cuvis_spectral.hpp
  *
  * 
  * @authors BenMGeo, Simon
  * @date 02/08/2023
  * @details written for use with cuvis measurements of all modes. 
  * @copyright Apache V2.0
  * */

//TODO make Simon check the comments

#include <cassert>
#include <cuvis.hpp>
#include <opencv2/opencv.hpp>
#include <vector>

/**
  * @brief Helper functions and structures for spectral calculation.
  *
  * Spectral helpers include structures and methods to extract spectra of type spectrum_t
  * from polygones of type polygon_t and calculate wavelength specific histograms of type histogram_vector_t.
  * */
namespace cuvis::aux::spectral
{
  /** @brief Couple of wavelength, respective mean value and standard deviation with default values.
   *  
   * Basic type for spectral information.
   * */
  struct spectral_mean_t
  {
    /** The wavelength (in nm).*/
    std::uint32_t wavelength;

    /** The value (counts/reflectance, depending on input).*/
    double value = //default value:
        -999.0;

    /** The standard deviation for the repsective value.*/
    double std = //default value:
        0.0;
  };

  /** @brief Couple of wavelength, respective count and occurrence
   */
  struct histogram_t
  {
    /** The center wavelength (in nm).*/
    std::uint32_t wavelength;

    /** The count for a specific center wavelength.*/
    std::vector<std::uint64_t> count;

    /** The occurence for the respective count.*/
    std::vector<std::uint64_t> occurrence;
  };

  /** @brief A vector type for describing a spectrum with mean and standard deviation
   * */
  using spectrum_t = std::vector<spectral_mean_t>;

  /** @brief A vector type for describing a histogram for individual wavelengths with counts and ocurrences
   * */
  using histogram_vector_t = std::vector<histogram_t>;

  /** @brief 2-dimensional definition of a single point
   * */
  struct point_t
  {
    /** The x coordinate. (E-W)*/
    double _x;

    /** The y coordinate. (S-N)*/
    double _y;
  };

  /** @brief A vector type for describing a polygon with x and y coordinates
   * */
  using polygon_t = std::vector<point_t>;

  template <typename data_t>

  /** @brief Calculates a spectrum for a polygon.
    *
    * Calculates a spectrum with mean and standard deviation for all 
    * wavelengths for a given polygon, i.e. vector of points.
    *  
    * @param[in] img Cuvis Image data from @ref Measurement
    * @param[in] poly Polygon for subsetting the image (can also be only 1 point)
    * @returns A vector of type @ref spectrum_t
    * */
  spectrum_t
      get_spectrum_polygon(image_t<data_t> const& img, polygon_t const& poly)
  {
    //checks if image is reasonable.
    assert(img._width > 1);
    assert(img._height > 1);
    assert(img._channels > 0);
    assert(img._wavelength != nullptr);

    // initializing the result
    spectrum_t res(img._channels);

    // conversion of polygon relative coordinates to absolute pixel coordinates
    if (poly.size() > 1) //polygon case
    {
      std::vector<cv::Point> transformed_pt; //needs to be integers
      for (auto const& pt : poly)
      {
        transformed_pt.emplace_back(
            pt._x * (img._width - 1), pt._y * (img._height - 1));
      }

      //empty mask
      cv::Mat mask = cv::Mat::zeros(cv::Size(img._width, img._height), CV_8UC1);

      //binary mask
      //using nearest neighbor
      cv::fillPoly(mask, transformed_pt, cv::Scalar(255));

      std::uint16_t n = 0;                                  //counter variable
      std::vector<std::double_t> sum_v(img._channels, 0.0); //growing sum
      std::vector<std::double_t> sq_sum_v(
          img._channels, 0.0); //growing square sum

      //checking all pixels in polygon mask
      for (int x = 0; x < img._width; x++)
      {
        for (int y = 0; y < img._height; y++)
        {
          if (mask.at<std::uint8_t>(y, x) > 128)
          {
            n++;
            for (int z = 0; z < img._channels; z++)
            {
              //reading out value
              auto loc_val =
                  img._data[((y)*img._width + (x)) * img._channels + (z)];
              //adding up values
              sum_v[z] += loc_val;
              sq_sum_v[z] += loc_val * loc_val;
            }
          }
        }
      }

      for (int z = 0; z < img._channels; z++)
      {
        // convert sum to mean
        double mean = sum_v[z] / n;
        spectral_mean_t loc_res;
        loc_res.value = mean;

        // sum(x - y)^2 = sum( x^2 - 2xy + y^2) // second binomial formula
        // Therefore: (sum(x^2) - 2 * sum(x) * y + n*y^2 ) / n
        // Therefore (sum(x^2) - 2 * sum(x) * y ) / n + y^2
        loc_res.std =
            sqrt((sq_sum_v[z] - 2 * sum_v[z] * mean) / n + mean * mean);

        // set wavelength
        std::uint32_t loc_wl = img._wavelength[z];
        loc_res.wavelength = loc_wl;
        res[z] = loc_res;
      }

      return res;
    }
    else if (poly.size() == 1) //single point case
    {
      //check if out of range
      if (poly.front()._x > 1.0 || poly.front()._x < 0.0 ||
          poly.front()._y > 1.0 || poly.front()._y < 0.0)
      {
        // outside range. nothing to return
        // TODO throw error?
        return res;
      }

      for (int z = 0; z < img._channels; z++)
      {
        //calculate position in memory
        int y_shift =
            std::round(poly.front()._y * (img._height - 1)) * img._width;
        int xy_shift = y_shift + std::round(poly.front()._x * (img._width - 1));
        //read out point value
        double loc_val = img._data[xy_shift * img._channels + z];
        //set wavelength and value
        std::uint32_t loc_wl = img._wavelength[z];
        spectral_mean_t loc_res;
        loc_res.value = loc_val;
        loc_res.wavelength = loc_wl;
        res[z] = (loc_res);
      }
      return res;
    }
    else // poly is empty should never happen
    {
      // TODO throw error?
      return res;
    }
  }


  /** @brief Calculates a histogram for an image
    *
    * Calculates a histogram for all wavelengths with counts and occurence
    * for a given Cuvis @ref Measurement Image.
    *  
    * @param[in] img Cuvis Image data from @ref Measurement
    * @param[in] histogram_min_size Lower limit for image data points
    * @param[in] count_bins Number of count bins of histogram
    * @param[in] wavelength_bins Number of wavelength bins of histogram
    * @returns A vector of type @ref histogram_vector_t
    * */
  template <typename data_t>
  histogram_vector_t get_histogram(
      image_t<data_t> const& img,
      size_t histogram_min_size,
      size_t count_bins,
      size_t wavelength_bins,
      bool detect_max_value)
  {
    histogram_vector_t output;
    //check if data is available and
    assert(img._height * img._width * img._channels > histogram_min_size);
    assert(img._wavelength != nullptr);

    data_t max_val = data_t(0);
    //detect maximum value for all data
    if (detect_max_value)
    {
      for (size_t y = 0; y < img._height; y++)
      {
        for (size_t x = 0; x < img._width; x++)
        {
          for (size_t i = 0; i < img._channels; i++)
          {
            data_t value = img._data[(y * img._width + x) * img._channels + i];
            if (value > max_val)
            {
              max_val = value;
            }
          }
        }
      }
    }
    else
    {
      // maxval is set to possible absolute maximum
      //size_t bit_depth = sizeof(data_t) * 8;
      data_t max_val = std::numeric_limits<decltype(max_val)>::max();
    }

    //calculate the size of each count bin for the histogram (min 1)
    const size_t bin_size =
        max_val / count_bins != 0 ? max_val / count_bins : 1;

    //calculate the size of each wavelength bin for the histogram (min 1)
    const size_t wlbin_size = img._channels / wavelength_bins != 0
                                  ? img._channels / wavelength_bins
                                  : 1;

    // Prepare histogram vector
    for (size_t i = 0; i < img._channels; i += wlbin_size)
    {
      // Initialize histogram objects
      histogram_t histogram;
      size_t const floor_maxval_width =
          static_cast<size_t>(std::floor(max_val / bin_size));
      histogram.occurrence = std::vector<std::uint64_t>(floor_maxval_width);
      histogram.count = std::vector<std::uint64_t>(floor_maxval_width);
      histogram.wavelength = img._wavelength[i + wlbin_size / 2];
      for (size_t k = 0; k < floor_maxval_width; k++)
      {
        histogram.count[k] =
            static_cast<std::remove_reference_t<decltype(histogram.count[0])>>(
                k * bin_size);
      }
      output.push_back(histogram);
    }

    // Iterate over cube: Fill out histograms
    for (size_t y = 0; y < img._height; y++)
    {
      for (size_t x = 0; x < img._width; x++)
      {
        for (size_t i = 0; i < img._channels; i++)
        {
          data_t value = img._data[(y * img._width + x) * img._channels + i];
          std::uint64_t region = std::uint64_t(std::floor(value / bin_size));
          if (region >= count_bins)
            region = count_bins - 1;
          output[i / wlbin_size].occurrence[region]++;
        }
      }
    }

    return output;
  }

} // namespace cuvis::aux::spectral