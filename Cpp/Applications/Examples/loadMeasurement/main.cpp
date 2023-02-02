#include "cuvis.hpp"

#include <cassert>
#include <iostream>
//#include <opencv/opencv.hpp>
int main(int argc, char* argv[])
{


  if (argc != 3)
  {
    std::cout << "To few Arguments! Please provide:" << std::endl;
    std::cout << "user settings directory" << std::endl;
    std::cout << "measurement file (.cu3)" << std::endl;

    return -1;
  }
  char* const userSettingsDir = argv[1];
  char* const measurementLoc = argv[2];




    std::cout << "Example 01 load measurement cpp " << std::endl;
    std::cout <<"User Settings Dir: " << userSettingsDir << std::endl;
    std::cout << "measurement file(.cu3): " <<measurementLoc << std::endl;

     std::cout << "loading user settings..." << std::endl;
    cuvis::General::init(userSettingsDir);
    cuvis::General::set_log_level(loglevel_info);

    std::cout << "loading measurement file..." << std::endl;
    cuvis::Measurement mesu(measurementLoc);

    std::cout
        << "Data 1" << mesu.get_meta()->name << " "
        << "t=" << mesu.get_meta()->integration_time << " ms "
        << "mode=" << mesu.get_meta()->processing_mode << " "
        << std::endl;
    if (mesu.get_meta()->measurement_flags.size() > 0)
    {
        std::cout << "  Flags" << std::endl;
        for (auto const& flags : mesu.get_meta()->measurement_flags)
        {
            std::cout << "  - " << flags.first << " (" << flags.second << ")" << std::endl;
        }
    }


    assert(
        mesu.get_meta()->processing_mode == Cube_Raw &&
        "This example requires raw mode");


    auto const& cube_it = mesu.get_imdata()->find(CUVIS_MESU_CUBE_KEY);
    assert(
        cube_it != mesu.get_imdata()->end() &&
        "Cube not found");

    auto cube = std::get<cuvis::image_t<std::uint16_t>>(cube_it->second);

     //uncomment to show a single channel with openCV
    /*
    cv::Mat img(
    cv::Size(cube._width, cube._height),
    CV_16UC(cube._channels),
    const_cast<void*>(reinterpret_cast<const void*>(cube._data)),
    cv::Mat::AUTO_STEP);

    cv::Mat singleChannel;
    cv::extractChannel(
        img, singleChannel, 25); // extract channel 25 as an example
    singleChannel.convertTo(singleChannel, CV_8U, 1 / 16.0);
    cv::imshow("channel 25", singleChannel);
    cv::waitKey(0);
    */

    
    std::size_t x = 120;
    std::size_t y = 200;

    assert(x < cube._width && "x index exceeds cube width");
    assert(y < cube._height && "x index exceeds cube width");

    std::cout << "lambda [nm]; raw counts [au] " << std::endl;

    for (std::size_t chn = 0; chn < cube._channels; chn++)
    {
        // memory layout:
        //unsigned index = (y * cube.width + x) * cube.channels + chn;
        //uint16_t value = cube16bit[index];


        auto const value = cube.get(x, y, chn);
        unsigned lambda = cube._wavelength[chn];

        std::cout << lambda << "; " << value << std::endl;
    }
    std::cout << "finished. " << std::endl;

    
}
