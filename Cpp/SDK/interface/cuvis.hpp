#pragma once

/**
  * @file cuvis.hpp
  * SDK calls for cuvis CPP SDK (wrapper).
  *
  * This header defines all public CPP SDK (wrapper) functions
  * */


#include "cuvis.h"
#pragma warning(disable : 26812)

#include <atomic>
#include <cassert>
#include <chrono>
#include <cstring>
#include <deque>
#include <exception>
#include <filesystem>
#include <functional>
#include <future>
#include <map>
#include <memory>
#include <mutex>
#include <optional>
#include <string>
#include <thread>
#include <type_traits>
#include <variant>

namespace cuvis
{
  //pre-declarations
  class Calibration;
  class Measurement;
  class SessionFile;
  class ProcessingContext;
  class AcquisitionContext;
  class Exporter;
  class Async;
  class AsyncMesu;
  class General;
  class Worker;

  struct ProcessingArgs;

  struct SaveArgs;
  struct TiffArgs;
  struct EnviArgs;
  struct ViewArgs;

  struct SessionInfo;

  /** @addtogroup typedefs CPP Type definitions from cuvis C sdk.
    * 
    * Theese type definitions are taken from the CUVIS C SDK (see @ref cuvis.h). Please refer to the C types for documentation.
    *  @{
    */

  /** @copydoc CUVIS_INT */
  using int_t = CUVIS_INT;

  /** @copydoc CUVIS_EVENT */
  using event_t = CUVIS_EVENT;

  /** @copydoc cuvis_loglevel_t */
  using loglevel_t = cuvis_loglevel_t;

  /** @copydoc cuvis_operation_mode_t */
  using operation_mode_t = cuvis_operation_mode_t;

  /** @copydoc cuvis_reference_type_t */
  using reference_type_t = cuvis_reference_type_t;

  /** @copydoc cuvis_processing_mode_t */
  using processing_mode_t = cuvis_processing_mode_t;

  /** @copydoc cuvis_pan_sharpening_interpolation_type_t */
  using pan_sharpening_interpolation_type_t =
      cuvis_pan_sharpening_interpolation_type_t;

  /** @copydoc cuvis_pan_sharpening_algorithm_t */
  using pan_sharpening_algorithm_t = cuvis_pan_sharpening_algorithm_t;

  /** @copydoc cuvis_tiff_compression_mode_t */
  using tiff_compression_mode_t = cuvis_tiff_compression_mode_t;

  /** @copydoc cuvis_tiff_format_t */
  using tiff_format_t = cuvis_tiff_format_t;

  /** @copydoc cuvis_session_info_t */
  using session_info_t = cuvis_session_info_t;

  /** @copydoc cuvis_mesu_metadata_t */
  using mesu_metadata_t = cuvis_mesu_metadata_t;

  /** @copydoc cuvis_sensor_info_t */
  using sensor_info_t = cuvis_sensor_info_t;

  /** @copydoc cuvis_hardware_state_t */
  using hardware_state_t = cuvis_hardware_state_t;

  /** @copydoc cuvis_capabilities_t */
  using capabilities_t = cuvis_capabilities_t;


  /** @} */

  /** as timesamp use STL system clock */
  using timestamp_t = std::chrono::time_point<std::chrono::system_clock>;

  /** The event call-back type must be of the format void fun(event_t)*/
  using cpp_event_callback_t = std::function<void(event_t)>;

  /** @cond INTERNAL */
  void chk(CUVIS_STATUS status);

  //image data traits
  template <typename T>
  struct is_supported_image_data_t
  {
    static const bool value = false;
  };
  template <>
  struct is_supported_image_data_t<std::uint8_t>
  {
    static const bool value = true;
  };
  template <>
  struct is_supported_image_data_t<std::uint16_t>
  {
    static const bool value = true;
  };
  template <>
  struct is_supported_image_data_t<std::uint32_t>
  {
    static const bool value = true;
  };
  template <>
  struct is_supported_image_data_t<float>
  {
    static const bool value = true;
  };

  template <typename T>
  struct is_supported_view_data_t
  {
    static const bool value = false;
  };
  template <>
  struct is_supported_view_data_t<std::uint8_t>
  {
    static const bool value = true;
  };
  template <>
  struct is_supported_view_data_t<float>
  {
    static const bool value = true;
  };

  /** @endcond */


  /** @brief Metaclass for handling image data (2d or 3d)
    *
    * Holds an X/Y/Z- dimensional image cube, without wavelength informaiton. 
    *
    * @tparam data_t The pixel bit depth, either std::uint8_t, std::uint16_t, std::uint32_t or float
    * */
  template <typename data_t>
  struct common_image_t
  {
    static_assert(
        is_supported_image_data_t<data_t>::value,
        "data_t must be std::uint8_t, std::uint16_t, std::uint32_t or float");

    /** width of channel(X - dimension) */
    std::size_t _width;

    /** height of channel(Z - dimension) */
    std::size_t _height;

    /** number of channels */
    std::size_t _channels;

    /** @brief The raw data pointer
      *
      * It is recommended to access the data with the @ref get function.\n
      * The memory interleave is BIP. E.g. for a 3x3x2 (x,y,z) the coordinates are:
      *
      *> (0,0,0); (0,0,1); (0,1,0); (0,1,1) \n
      *> (1,0,0); (1,0,1); (1,1,0); (0,1,1) \n
      *> (2,0,0); (2,0,1); (2,1,0); (0,1,1) \n
      *
      * */
    data_t const* _data;

    /** Access to a given memory location within @ref _data 
      *
      * @param x x pixel position (0 - @ref _width - 1)
      * @param y y pixel position (0 - @ref _height - 1)
      * @param y z pixel position (0 - @ref _channels - 1), Use "0" for a 2d image
      * @returns the pixel value of the image / cube at position (x,y,z)
      * */
    data_t const&
        get(std::size_t x, std::size_t y, std::size_t z = std::size_t(0)) const;
  };

  /** @brief Image data from a measurement
    *
    * See @ref common_image_t for single pixel access.
    * The @ref _wavelength is either a nullptr or, if set contains the cube's wavelengths in nano meter.
    *
    * @tparam data_t The pixel bit depth, either std::uint8_t, std::uint16_t, std::uint32_t or float 
    * */
  template <typename data_t>
  struct image_t : common_image_t<data_t>
  {
    friend class Measurement;
    friend class Viewer;

  public:
    /** wavelength vector. nullptr, an array of size @ref _channels contianing the wavelengths in nano meter. */
    uint32_t const* _wavelength;

  private:
    std::shared_ptr<CUVIS_MESU> _ref;
  };

  /** @brief Image data created from @ref ViewExporter
    *    
    * The @ref ViewExpoter generates image views (int 8 bit resolution) and data views (in floating point precision). Each image is named by it's @ref _id. 
    * Also the @ref _show flag is set with respect to the setting of the view's author. See @ref ViewExporter for more information.
    * See @ref common_image_t for single pixel access.
    *
    * @tparam data_t The pixel bit depth, either std::uint8_t or float 
    * */
  template <typename data_t>
  struct view_t : common_image_t<data_t>
  {
    static_assert(
        is_supported_view_data_t<data_t>::value,
        "data_t must be std::uint8_t or float");

    friend class Viewer;

  public:
    /** The image categroy */
    cuvis_view_category_t _category;

    /** Hint, if data can be shown on a screen as an image */
    bool _show;

    /**  The name of the image */
    std::string _id;

  private:
    std::shared_ptr<CUVIS_VIEW> _ref;
  };

  /** @brief Export Settings common to all exporters
    *
    * The options of this structure can be set for any @ref Exporter. However, not all options are respected by the @ref Exporter. 
    * */
  struct GeneralExportArgs
  {
    /** Constructor to create default parameters */
    GeneralExportArgs();

    /** convert to C - SDK settings structure */
    operator cuvis_export_general_settings_t() const;

    /** The directory where the files should be exported to (default: ".") */
    std::filesystem::path export_dir;

    /** @brief The selection of spectral channels to be exproted. (default  : "all")
      *
      * @copydoc cuvis_export_general_settings_t.channel_selection 
      * */
    std::string channel_selection;

    /** @brief Multiply the spectrum before exporting. 
      *
      * @copydoc cuvis_export_general_settings_t.spectra_multiplier
      * */
    double spectra_multiplier;

    /** @brief amount of pan-sharpening (default: 0)
      *
      * @copydoc cuvis_export_general_settings_t.pan_scale
      * */
    double pan_scale;

    /** @brief The pansharpening interpolation type (default: @ref pan_sharpening_interpolation_type_Linear)
      *
      * @copydoc cuvis_export_general_settings_t.pan_interpolation_type
      * */
    pan_sharpening_interpolation_type_t pan_interpolation_type;

    /** @brief The pansharpening algorithm (default: @ref pan_sharpening_algorithm_CubertMacroPixel)
      *
      * @copydoc cuvis_export_general_settings_t.pan_interpolation_type
      * */
    pan_sharpening_algorithm_t pan_algorithm;

    
    /** 
      * @copydoc cuvis_viewer_settings_t.blend_opacity
      */
    double blend_opacity;

    /** @brief Add the pan image to the output (default: @ref false)
      *
      * @copydoc cuvis_export_general_settings_t.add_pan
      * */
    bool add_pan;

    /** @brief Add a full-resolution pan image to the export (default: @ref false)
      *
      * @copydoc cuvis_export_general_settings_t.add_fullscale_pan
      * */
    bool add_fullscale_pan;

    /** @brief Set @ref Expor   ter to permisive mode (default: @ref false)
      *
      * @copydoc cuvis_export_general_settings_t.permissive
      * */
    bool permissive;
  };

  /** @brief Options for saving cu3s/cu3 files
    * 
    * Use with either @ref CubeExporter (recommended) or @ref Measurement.save
    */
  struct SaveArgs : public GeneralExportArgs
  {
    /** Constructor to create default parameters */
    SaveArgs();

    /** @brief convert to C - SDK settings structure 
      *
      * @copydoc cuvis_save_args_t
      */
    operator cuvis_save_args_t() const;

    /** @brief allow to split to several files (default: false)
      *
      * @copydoc cuvis_save_args_t.allow_fragmentation
      * */
    bool allow_fragmentation;

    /** @brief allow to overwrite existing files (default: false)
      *
      * @copydoc cuvis_save_args_t.allow_overwrite
      * */
    bool allow_overwrite;

    /** @brief allow to drop measurements if internal buffers a depleted (default: false)
      *
      * @copydoc cuvis_save_args_t.allow_drop
      * */
    bool allow_drop;

    /** @brief allow to drop measurements if internal buffers a depleted (default: false)
      *
      * @copydoc cuvis_save_args_t.allow_drop
      * */
    bool allow_session_file;

    /** @brief allow to write an additional .info file (default: true)
      *
      * @copydoc cuvis_save_args_t.allow_info_file
      * */
    bool allow_info_file;

    /** @brief The operation mode to be stored with a session file (default: @ref operation_mode_t.OperationMode_Software)
      *
      * @copydoc cuvis_save_args_t.operation_mode
      * */
    operation_mode_t operation_mode;

    /** @brief The fps to be stored with a session file (default: 0)
      *
      * @copydoc cuvis_save_args_t.fps
      * */
    double fps;

    /** @brief Out-of-order frames are sorted within the cache, as long as the cache useage is below this limit
      *
      * @copydoc cuvis_save_args_t.soft_limit
      * */
    size_t soft_limit;

    /** @brief Maximum number of elements in output cache.
      *
      * @copydoc cuvis_save_args_t.hard_limit
      * */
    size_t hard_limit;

    /** Any frame is forced to be written after this time, latest. 
      *
      * @copydoc cuvis_save_args_t.max_buftime
      * */
    std::chrono::milliseconds max_buftime;
  };
  /** @brief Additional settings for exporting tiff.*/
  struct TiffArgs : public GeneralExportArgs
  {
    /** Constructor to create default parameters */
    TiffArgs();

    /** convert to C - SDK settings structure */
    operator cuvis_export_tiff_settings_t() const;

    /**
      * @copydoc cuvis_tiff_compression_mode_t
      * */
    tiff_compression_mode_t compression_mode;

    /** 
      * @copydoc cuvis_tiff_format_t
      * */

    tiff_format_t format;
  };


  struct EnviArgs : public GeneralExportArgs
  {
    /** Constructor to create default parameters */
    EnviArgs() = default;
  };
  /** @brief viewer settings
  * 
  * */
  struct ViewArgs : public GeneralExportArgs
  {
    /** Constructor to create default parameters */
    ViewArgs();

    /** @brief convert to C - SDK settings structure 
      *
      * @copydoc cuvis_viewer_settings_t
      */
    operator cuvis_viewer_settings_t() const;

    /** @brief convert to C - SDK settings structure 
      *
      * @copydoc cuvis_export_view_settings_t
      */
    operator cuvis_export_view_settings_t() const;

    /** 
      * @copydoc cuvis_viewer_settings_t.userplugin
      */
    std::string userplugin;

    /** 
      * @copydoc cuvis_viewer_settings_t.complete
      */
    bool complete;
  };
  /** @brief processing arguments */
  struct ProcessingArgs
  {
    /** Constructor to create default parameters */
    ProcessingArgs();
    /** @brief convert to C - SDK settings structure 
      *
      * @copydoc cuvis_proc_args_t
      */
    operator cuvis_proc_args_t() const;

    /** 
      * @copydoc cuvis_proc_args_t.processing_mode
      */
    processing_mode_t processing_mode;

    /** 
      * @copydoc cuvis_proc_args_t.allow_recalib
      */
    bool allow_recalib;
  };

  /** settings for the worker*/
  struct WorkerArgs
  {
    /** Constructor to create default parameters */
    WorkerArgs();
    /** @brief convert to C - SDK settings structure 
      *
      * @copydoc cuvis_worker_settings_t
      */
    operator cuvis_worker_settings_t() const;

    /**
    * @brief Number of threads
    * 
    * @copydoc cuvis_worker_settings_t.worker_count
    */
    unsigned worker_count;

    /**
    * @copydoc cuvis_worker_settings_t.poll_interval
    */
    std::chrono::milliseconds poll_interval;

    /**
    * @copydoc cuvis_worker_settings_t.keep_out_of_sequence
    */
    bool keep_out_of_sequence;

    /*
    * @copydoc cuvis_worker_settings_t.worker_queue_size
    */
    int worker_queue_size;

    /*
    * @copydoc cuvis_worker_settings_t.worker_queue_hard_limit
    */
    int worker_queue_hard_limit;

    /*
    * @copydoc cuvis_worker_settings_t.worker_queue_soft_limit
    */
    int worker_queue_soft_limit;

    /*
    * @copydoc cuvis_worker_settings_t.can_drop
    */
    bool can_drop;
  };

  /*
  * internal info
  */
  struct SessionInfo
  {
    /** Constructor to create default parameters */
    SessionInfo();

    /** Constructor to create session info from session*/
    SessionInfo(session_info_t const& sess);

    /** @brief convert to C - SDK settings structure 
      *
      * @copydoc cuvis_session_info_t
      */
    operator session_info_t() const;

    /**
    * @copydoc cuvis_session_info_t.name
    */
    std::string name;

    /**
    * @copydoc cuvis_session_info_t.session_no
    */
    unsigned session_no;

    /**
    * @copydoc cuvis_session_info_t.sequence_no
    */
    unsigned sequence_no;
  };

  /**
  * measurement meta structure
  */
  struct MeasurementMetaData
  {
    /** Constructor to create default parameters */
    MeasurementMetaData(mesu_metadata_t const& meta);

    /**
    * @copydoc cuvis_mesu_metadata_t.name
    */
    std::string name;

    /**
    * @copydoc cuvis_mesu_metadata_t.path
    */
    std::string path;

    /**
    * @copydoc cuvis_mesu_metadata_t.comment
    */
    std::string comment;

    /**
    * @copydoc cuvis_mesu_metadata_t.capture_time
    */
    timestamp_t capture_time;

    /**
    * @copydoc cuvis_mesu_metadata_t.factory_calibration
    */
    timestamp_t factory_calibration;

    /**
    * @copydoc cuvis_mesu_metadata_t.product_name
    */
    std::string product_name;

    /**
    * @copydoc cuvis_mesu_metadata_t.serial_number
    */
    std::string serial_number;

    /**
    * @copydoc cuvis_mesu_metadata_t.assembly
    */
    std::string assembly;

    /**
    * @copydoc cuvis_mesu_metadata_t.integration_time
    */
    double integration_time;

    /**
    * @copydoc cuvis_mesu_metadata_t.averages
    */
    unsigned averages;


    /**
    * The distance, the measurement was recorded in, in millimeters, if available.
    */
    std::optional<double> distance;

    /**
    * The session information of the measurement.
    */
    SessionInfo session_info;
    processing_mode_t processing_mode;
    std::map<std::string, std::string> measurement_flags;
  };

  /**
* sensor info data structure
*/
  struct SensorInfoData
  {
    SensorInfoData(sensor_info_t const& info);
    /** number of averages used*/
    uint32_t averages;
    /** the sensors's temperature while readout (0 if not applicable) */
    int32_t temperature;
    /** gain value while recording */
    double gain;
    /** the timestamp (UTC) of the image readout (senor's hardware clock )*/
    timestamp_t readout_time;
  };


  class cuvis_sdk_exception : public std::exception
  {
  public:
    cuvis_sdk_exception(std::string const& msg, std::wstring const& wmsg);

    char const* what(void) const noexcept;

    std::wstring what_wstr(void) const noexcept;

  protected:
    std::string const _msg;
    std::wstring const _wmsg;
  };


  class General
  {
  public:
    static void set_log_level(int_t lvl);
    static void set_exception_locale(std::string const& locale = "");
    static void register_log_callback(
        std::function<void(char const*, loglevel_t)> callback, int_t min_lvl);
    static void reset_log_callback();
    static void register_log_callback_localized(
        std::function<void(wchar_t const*, loglevel_t)> callback,
        int_t min_lvl,
        std::string const& loc_id);
    static void reset_log_callback_localized();
    static std::string version();
    static void init(std::string const& settings_path);

    static int_t
        register_event_callback(cpp_event_callback_t callback, int_t i_type);
    static void unregister_event_callback(int_t i_handler_id);
  };


  /** @brief central measurement class
    */
  class Measurement
  {
  public:
    friend class ProcessingContext;
    friend class Exporter;
    friend class AsyncMesu;
    friend class Viewer;
    friend class SessionFile;
    friend class AcquisitionContext;
    friend class Worker;

  public:
    using image_variant_t = std::variant<
        image_t<std::uint8_t>,
        image_t<std::uint16_t>,
        image_t<std::uint32_t>,
        image_t<float>>;


    using gps_data_t = std::map<std::string, cuvis_gps_t>;
    using string_data_t = std::map<std::string, std::string>;
    using image_data_t = std::map<std::string, image_variant_t>;
    using sensor_info_data_t = std::map<std::string, SensorInfoData>;

  public:
    /* shallow copy(move assignment) */
    Measurement& operator=(Measurement const& measurement) = default;

    /* move constructor */
    Measurement(Measurement&& measurement) = default;

    /* deep copy */
    Measurement(Measurement const& source);

    Measurement(std::filesystem::path const& path);

    /** @brief Get the capabilites of the measurement which were present in the calibration during capture.
    * This doesn't indicate which capabilities are currently available for the measurement.
    */
    std::vector<capabilities_t> get_capabilities() const;

    /** @brief Get the metadata of the measurement
    * 
    * The meta-data from the measurement contains information about
    * the measurement when it was recorded: when and how. Meta-Data
    * do not contain the actual recorded data.
    */
    MeasurementMetaData const* get_meta() const;

    /** @brief Get image info data from measurement
   *
   * Return image data from a measurement.
   */
    sensor_info_data_t const* get_sensor_info() const;

    /** @brief Get GPS data from measurement
      */
    gps_data_t const* get_gps() const { return _gps_data.get(); }

    /**  @brief Get image data from measurement
    *
    * Return image data from measurement.
    */
    image_data_t const* get_imdata() const { return _image_data.get(); }

    /** @brief Get string data from measurement
      */
    string_data_t const* get_strdata() const { return _string_data.get(); }

    /** @brief Get thumbnail / preview image of measurement
    * 
    */
    image_t<std::uint8_t> const* get_thumbnail() const;
    /** @brief get calibration id of this measurement
    */
    std::string get_calib_id() const;

    /** @brief Save measurement 
    * 
    * Save the measurement with given arguments
    * 
    * @param args The Save Arguments to use for saving the measurement. See also @ref SaveArgs
    */
    void save(SaveArgs const& args);

    /** @brief Set name of measurement
    * 
    *   @param name String to use as name of the measuremen
    */
    void set_name(std::string const& name);

    /** @brief set comment of measurement
    * @param comment String to use as comment for the measurement
    */
    void set_comment(std::string const& comment);

    /** @brief clears the cube from the measurement
    * 
    * Clears the proceessing result, i. e. the cube, from the measurement. This returns the measurement the state before
    * applying the processing. This can be usefull for reduced data usage.
    */
    void clear_cube();

    /**@brief Clear the implicit reference measurement
    * 
    * Implict measurements are created, when a measurement is processed with a processing context, where 
    * explicit references are set. Then, these references are remebemred by the measurement. When changing
    * the processing context, the references are implicitly available, still. Clearing them may be interesing
    * if the references set are wrong/invalid or if disk space is a concearn.
    * 
    * @param type Type of reference to clear
    */
    void clear_implicit_reference(reference_type_t type);

    /**@brief Resynchronize the Measurement with the SDK data
    * 
	* usally this does not have to be called manually, but is rather called internally by any operation that may result in invalidated (meta-)data
    * */
    void refresh();

  private:
    Measurement(CUVIS_MESU handle);



  private:
    std::shared_ptr<CUVIS_MESU> _mesu;

  private:
    std::shared_ptr<MeasurementMetaData> _meta;
    std::shared_ptr<sensor_info_data_t> _sensor_info;
    std::shared_ptr<gps_data_t> _gps_data;
    std::shared_ptr<string_data_t> _string_data;
    std::shared_ptr<image_data_t> _image_data;
    std::shared_ptr<image_t<std::uint8_t>> _preview_image;
  };

  /**
  * central calibration Class
  */
  class Calibration
  {
    friend class ProcessingContext;
    friend class AcquisitionContext;

  public:
    /** @brief Create a calibration from factory path
    *
    * The calibration is created from a factory path, containing the license and calibration
    * file "init.daq" as well as further calibration files (e.g. SpRad.cu3).
    *
    * The calibration is lazy-loading, i.e. the AcquisitionContext and the
    * ProcessingContext will only be initialized, when explicitly called.
    *
    * @note do not load multiple calibration instances of the same camera
    *
    * @param[in] path The path to the factory directory
    */
    Calibration(std::filesystem::path const& path);

    /** @brief Create a calibration from session file
    *
    * Create a calibration from an existion session file.
    *
    * The calibration is lazy-loading, i.e. the AcquisitionContext and the
    * ProcessingContext will only be initialized, when explicitly called.
    * 
    * When you create a processing context from the calibration cerated with
    * this function, you won't have the references from the session file set.
    * Use @ref cuvis_proc_cont_create_from_session_file to load a processing context
    * where the referenecs are taken from the session file.
    *
    * @note do not load multiple calibration instances of the same camera
    *
    * @param[in] session The session file
    */
    Calibration(SessionFile const& session);

    /**
    * @brief get calibration capabilities
    * 
    * @param mode Operation mode of the camera see also @ref cuvis_operation_mode_t
    */
    std::vector<capabilities_t>
        get_capabilities(CUVIS_OPERATION_MODE mode) const;
    /**
    * @brief get the calibration id
    */
    std::string get_id() const;

  private:
    std::shared_ptr<CUVIS_CALIB> _calib;
  };

  class SessionFile
  {
    friend class Calibration;
    friend class ProcessingContext;
    friend class AcquisitionContext;
    friend class Worker;

  public:
    SessionFile(std::filesystem::path const& path);

    std::optional<Measurement> get_mesu(
        int_t frameNo,
        cuvis_session_item_type_t type =
            cuvis_session_item_type_t::session_item_type_frames) const;

    std::optional<Measurement>
        get_ref(int_t refNo, cuvis_reference_type_t type) const;
    /**
    * @brief get size of the SessionFile
    */
    int_t get_size(
        cuvis_session_item_type_t type =
            cuvis_session_item_type_t::session_item_type_frames) const;


    /**
    * @brief get the frame rate of this session
    */
    double get_fps() const;

    /**
    * @brief get operation mode of the session
    */
    CUVIS_OPERATION_MODE get_operation_mode() const;

  private:
    std::shared_ptr<CUVIS_SESSION_FILE> _session;
  };

  class ProcessingContext
  {
    friend class Worker;

  public:
    //Builders
    ProcessingContext(Calibration const& calib);
    ProcessingContext(Measurement const& mesu);
    ProcessingContext(SessionFile const& session);
    //Apply
    Measurement& apply(Measurement& mesu) const;
    bool calc_distance(double distMM);

  public:
    //setters

    /**
    * @brief Set the reference for processing context
    *  
    * @param mesu measurement The measurement to be used as explicit reference
    * @param type Type of reference to set
    */
    void set_reference(Measurement const& mesu, reference_type_t type);

    /**
    * @brief Clear a reference measurement
    * 
    * @param type Type of reference to clear
    */
    void clear_reference(reference_type_t type);
    /**
    * @brief set the processing arguments for the processing context
    * 
    * @param procArgs arguments to set
    */
    void set_processingArgs(ProcessingArgs const& procArgs);

    //getters
    /**
    * @brief get a specific reference from the processing context
    *
    * The processing context can hold explicit references (e.g. a dark),
    * see @ref ProcessingArgs.set_reference . These reference can be obtained
    * by this functions
    */
    std::optional<Measurement> get_reference(reference_type_t type) const;

    /**
    * @brief get the arguments of the processing context
    */
    ProcessingArgs const& get_processingArgs() const;

    //checkers
    /**
    @brief Check if a processing mode is possible for a measurement
    *
    * Depending on the measurement, it's intrinsic references, the processing
    * context's explicit references and the internal camera calibration itself
    * the availability of a mode varies.
    *
    * Use this function, to check whether a specific mode is explicitly possible for
    * a measurement.
    */
    bool is_capable(
        Measurement const& mesu, ProcessingArgs const& procArgs) const;

    /**
    * @brief Check if an explicit reference was set
    * 
    * @param type reference type to check for
    */
    bool has_reference(reference_type_t type) const;
    /**
    * @brief get the calibration id of the procession context
    */
    std::string get_calib_id() const;

  private:
    std::shared_ptr<CUVIS_PROC_CONT> _procCont;
    ProcessingArgs _procArgs;
  };

  enum class async_result_t
  {
    done,
    timeout,
    overwritten,
    deferred
  };

  class Async
  {
    friend class AcquisitionContext;

  public:
    async_result_t
        get(std::chrono::milliseconds waittime = std::chrono::milliseconds(0));

  private:
    std::shared_ptr<CUVIS_ASYNC_CALL_RESULT> _async;
  };

  class AsyncMesu
  {
    friend class AcquisitionContext;

  public:
    std::pair<async_result_t, std::optional<Measurement>>
        get(std::chrono::milliseconds waittime = std::chrono::milliseconds(0));


  private:
    std::shared_ptr<CUVIS_ASYNC_CAPTURE_RESULT> _async;
  }; // namespace cuvis



  class AcquisitionContext
  {
    friend class Worker;

  public:
    struct component_state_info_t
    {
      std::string display_name;
      bool is_online;
    };

  public:
    using mesu_callback_t = std::function<void(Measurement)>;
    using component_state_t = std::pair<std::string, bool>;
    using state_callback_t = std::function<void(
        hardware_state_t, std::map<int_t, component_state_info_t>)>;


  public:
    AcquisitionContext(Calibration const& calib);
    AcquisitionContext(SessionFile const& sess, bool simulate = false);
    ~AcquisitionContext();

  public:
    AsyncMesu capture();
    void capture_queue();
    hardware_state_t get_state() const;
    std::optional<Measurement> get_next_measurement(
        std::chrono::milliseconds timeout_ms =
            std::chrono::milliseconds(0)) const;
    SessionInfo get_session_info() const;
    int_t get_component_count() const;
    CUVIS_COMPONENT_INFO get_component_info(int_t id) const;

    void set_session_info(SessionInfo session);
    void set_queue_size(int_t size);

    bool has_next_measurement() const;

    void register_state_change_callback(
        state_callback_t callback, bool output_initial_state = true);
    void reset_state_change_callback();


#define ACQ_STUB_0a(funname, sdkname, type_ifcae, type_wrapped) \
  type_wrapped get_##funname() const                            \
  {                                                             \
    type_ifcae res;                                             \
    chk(sdkname##_get(*_acqCont, &res));                        \
    return static_cast<type_wrapped>(res);                      \
  }
#define ACQ_STUB_0b(funname, sdkname, type_ifcae, type_wrapped)     \
  Async set_##funname(type_wrapped value) const                     \
  {                                                                 \
    CUVIS_ASYNC_CALL_RESULT async_handle;                           \
    chk(sdkname##_set_async(                                        \
        *_acqCont, &async_handle, static_cast<type_ifcae>(value))); \
    Async async;                                                    \
    async._async = std::shared_ptr<CUVIS_ASYNC_CALL_RESULT>(        \
        new CUVIS_ASYNC_CALL_RESULT{async_handle},                  \
        [](CUVIS_ASYNC_CALL_RESULT* handle) {                       \
          cuvis_async_capture_free(handle);                         \
          delete handle;                                            \
        });                                                         \
    return async;                                                   \
  }

    ACQ_STUB_0a(fps, cuvis_acq_cont_fps, double, double);
    ACQ_STUB_0a(
        integration_time, cuvis_acq_cont_integration_time, double, double);
    ACQ_STUB_0a(auto_exp, cuvis_acq_cont_auto_exp, int_t, bool);
    ACQ_STUB_0a(preview_mode, cuvis_acq_cont_preview_mode, int_t, bool);
    ACQ_STUB_0a(
        operation_mode,
        cuvis_acq_cont_operation_mode,
        cuvis_operation_mode_t,
        operation_mode_t);
    ACQ_STUB_0a(average, cuvis_acq_cont_average, int_t, int);

    ACQ_STUB_0a(bandwidth, cuvis_acq_cont_bandwidth, int_t, int);

    ACQ_STUB_0a(queue_size, cuvis_acq_cont_queue_size, int_t, int);

    ACQ_STUB_0a(queue_used, cuvis_acq_cont_queue_used, int_t, int);

    ACQ_STUB_0b(fps, cuvis_acq_cont_fps, double, double);
    ACQ_STUB_0b(
        integration_time, cuvis_acq_cont_integration_time, double, double);
    ACQ_STUB_0b(auto_exp, cuvis_acq_cont_auto_exp, int_t, bool);
    ACQ_STUB_0b(preview_mode, cuvis_acq_cont_preview_mode, int_t, bool);
    ACQ_STUB_0b(
        operation_mode,
        cuvis_acq_cont_operation_mode,
        cuvis_operation_mode_t,
        operation_mode_t);
    ACQ_STUB_0b(average, cuvis_acq_cont_average, int_t, int);

    ACQ_STUB_0b(continuous, cuvis_acq_cont_continuous, int_t, int);

    //ACQ_STUB_0b(queue_size, cuvis_acq_cont_queue_size, int_t, int);

#undef ACQ_STUB_0a
#undef ACQ_STUB_0b

#define ACQ_STUB_1a(funname, sdkname, type_ifcae, type_wrapped) \
  type_wrapped get_##funname(size_t id) const                   \
  {                                                             \
    type_ifcae res;                                             \
    chk(sdkname##_get(*_acqCont, id, &res));                    \
    return static_cast<type_wrapped>(res);                      \
  }

    ACQ_STUB_1a(component_online, cuvis_comp_online, int_t, int);
    ACQ_STUB_1a(component_gain, cuvis_comp_gain, double, double);
    ACQ_STUB_1a(
        component_integration_time_factor,
        cuvis_comp_integration_time_factor,
        double,
        double);
    ACQ_STUB_1a(bandwidth, cuvis_comp_bandwidth, int_t, int);

    ACQ_STUB_1a(driver_queue_size, cuvis_comp_driver_queue_size, int_t, size_t);
    ACQ_STUB_1a(driver_queue_used, cuvis_comp_driver_queue_used, int_t, size_t);
    ACQ_STUB_1a(
        hardware_queue_size, cuvis_comp_hardware_queue_size, int_t, size_t);
    ACQ_STUB_1a(
        hardware_queue_used, cuvis_comp_hardware_queue_used, int_t, size_t);

    ACQ_STUB_1a(temperature, cuvis_comp_temperature, int_t, int);

#undef ACQ_STUB_1a

#define ACQ_STUB_1b(funname, sdkname, type_ifcae, type_wrapped)         \
  Async set_##funname(size_t id, type_wrapped value) const              \
  {                                                                     \
    CUVIS_ASYNC_CALL_RESULT async_handle;                               \
    chk(sdkname##_set_async(                                            \
        *_acqCont, id, &async_handle, static_cast<type_ifcae>(value))); \
    Async async;                                                        \
    async._async = std::shared_ptr<CUVIS_ASYNC_CALL_RESULT>(            \
        new CUVIS_ASYNC_CALL_RESULT{async_handle},                      \
        [](CUVIS_ASYNC_CALL_RESULT* handle) {                           \
          cuvis_async_capture_free(handle);                             \
          delete handle;                                                \
        });                                                             \
    return async;                                                       \
  }

    ACQ_STUB_1b(component_gain, cuvis_comp_gain, double, double);
    ACQ_STUB_1b(
        component_integration_time_factor,
        cuvis_comp_integration_time_factor,
        double,
        double);

#undef ACQ_STUB_1b
    CUVIS_ACQ_CONT get_handle() const;

  private:
    std::shared_ptr<CUVIS_ACQ_CONT> _acqCont;
    std::atomic_bool _state_poll_thread_run;

    std::thread _state_poll_thread;
  };

  class Viewer
  {
    friend class Worker;

  public:
    using viewer_settings_t = cuvis_viewer_settings_t;
    using view_variant_t = std::variant<view_t<std::uint8_t>, view_t<float>>;
    using view_data_t = std::map<std::string, view_variant_t>;


  public:
    Viewer(ViewArgs const& args);
    view_data_t apply(Measurement const& mesu);

  private:
    std::shared_ptr<CUVIS_VIEWER> _viewer;
    static view_data_t create_view_data(CUVIS_VIEW);
  };

  class Exporter
  {
    friend class Worker;

  public:
    using general_export_settings_t = cuvis_export_general_settings_t;

    Measurement const& apply(Measurement const& mesu) const;

    size_t get_queue_used() const;

  protected:
    Exporter() = default;
    void setHandle(CUVIS_EXPORTER exporter);

  private:
    std::shared_ptr<CUVIS_EXPORTER> _exporter;
  };

  class CubeExporter : public Exporter
  {
  public:
    using format_settings_t = cuvis_save_args_t;

  public:
    CubeExporter(SaveArgs const& args);
  };

  class TiffExporter : public Exporter
  {
  public:
    using format_settings_t = cuvis_export_tiff_settings_t;

  public:
    TiffExporter(TiffArgs const& args);
  };

  class EnviExporter : public Exporter
  {
  public:
    EnviExporter(EnviArgs const& args);
  };

  class ViewExporter : public Exporter
  {
  public:
    using format_settings_t = cuvis_export_view_settings_t;

  public:
    ViewExporter(ViewArgs const& args);
  };

  class Worker
  {
  public:
    struct worker_return_t
    {
      std::optional<Measurement> mesu;
      std::optional<Viewer::view_data_t> view;
      std::exception_ptr exception;
    };

    using worker_callback_t = std::function<void(worker_return_t)>;


  public:
    Worker(WorkerArgs const& args);

    void set_acq_cont(AcquisitionContext const* acqCont);
    void set_proc_cont(ProcessingContext const* procCont);
    void set_exporter(Exporter const* exporter);
    void set_viewer(Viewer const* viewer);
    std::future<int> set_session_file(
        SessionFile const* session, bool skip_dropped_frames = false);
    std::pair<int, int> query_session_progress();
    bool get_drop_behavior();
    void set_drop_behavior(bool canDrop);

    bool has_next_result() const;
    worker_return_t get_next_result() const;


    void register_worker_callback(
        worker_callback_t callback, unsigned concurrency = 1);

    void reset_worker_callback();


    std::pair<int32_t, int32_t> get_queue_limits() const;
    size_t get_queue_used() const;
    void set_queue_limits(int32_t hard_limit, int32_t soft_limit);

  private:
    std::shared_ptr<CUVIS_WORKER> _worker;


    std::atomic_bool _worker_poll_thread_run;

    std::thread _worker_poll_thread;
  };

  /** \cond INTERNAL */

  // implementation part


  inline void chk(CUVIS_STATUS status)
  {
    if (status != status_ok)
    {
      throw cuvis_sdk_exception(
          cuvis_get_last_error_msg(), cuvis_get_last_error_msg_localized());
    }
  }

  inline Measurement::Measurement(Measurement const& source)
      : _gps_data(std::make_shared<gps_data_t>()),
        _string_data(std::make_shared<string_data_t>()),
        _image_data(std::make_shared<image_data_t>()),
        _sensor_info(std::make_shared<sensor_info_data_t>())
  {
    CUVIS_MESU copy_handle;
    chk(cuvis_measurement_deep_copy(*source._mesu, &copy_handle));

    _mesu = std::shared_ptr<CUVIS_MESU>(
        new CUVIS_MESU{copy_handle}, [](CUVIS_MESU* handle) {
          cuvis_measurement_free(handle);
          delete handle;
        });
    refresh();
  }


  inline Measurement::Measurement(std::filesystem::path const& path)
      : _gps_data(std::make_shared<gps_data_t>()),
        _string_data(std::make_shared<string_data_t>()),
        _image_data(std::make_shared<image_data_t>()),
        _sensor_info(std::make_shared<sensor_info_data_t>())
  {
    CUVIS_MESU mesu;
    chk(cuvis_measurement_load(path.string().c_str(), &mesu));

    _mesu = std::shared_ptr<CUVIS_MESU>(
        new CUVIS_MESU{mesu}, [](CUVIS_MESU* handle) {
          cuvis_measurement_free(handle);
          delete handle;
        });

    refresh();
  }
  inline Measurement::Measurement(CUVIS_MESU handle)
      : _gps_data(std::make_shared<gps_data_t>()),
        _string_data(std::make_shared<string_data_t>()),
        _image_data(std::make_shared<image_data_t>()),
        _sensor_info(std::make_shared<sensor_info_data_t>()),
        _mesu(std::shared_ptr<CUVIS_MESU>(
            new CUVIS_MESU{handle}, [](CUVIS_MESU* handle) {
              cuvis_measurement_free(handle);
              delete handle;
            }))
  {
    refresh();
  }

  inline void Measurement::save(SaveArgs const& args)
  {
    chk(cuvis_measurement_save(*_mesu, args.export_dir.string().c_str(), args));
    refresh();
  }



  inline void Measurement::set_name(std::string const& name)
  {
    chk(cuvis_measurement_set_name(*_mesu, name.c_str()));
    refresh();
  }

  inline void Measurement::set_comment(std::string const& comment)
  {
    chk(cuvis_measurement_set_comment(*_mesu, comment.c_str()));
    refresh();
  }

  inline void Measurement::clear_cube()
  {
    chk(cuvis_measurement_clear_cube(*_mesu));
    refresh();
  }


  inline void Measurement::clear_implicit_reference(reference_type_t type)
  {
    chk(cuvis_measurement_clear_implicit_reference(*_mesu, type));
    refresh();
  }

  inline void Measurement::refresh()
  {
    mesu_metadata_t meta;
    chk(cuvis_measurement_get_metadata(*_mesu, &meta));
    _meta = std::make_shared<cuvis::MeasurementMetaData>(meta);

    auto get_flag = [&](CUVIS_FLAGS flag, std::string const& key) -> void {
      if (meta.measurement_flags & flag)
      {
        CUVIS_CHAR value[CUVIS_MAXBUF];
        chk(cuvis_measurement_get_data_string(*_mesu, key.c_str(), value));
        _meta->measurement_flags.emplace(key, value);
      }
    };

    get_flag(
        CUVIS_MESU_FLAG_OVERILLUMINATED, CUVIS_MESU_FLAG_OVERILLUMINATED_KEY);
    get_flag(
        CUVIS_MESU_FLAG_POOR_REFERENCE, CUVIS_MESU_FLAG_POOR_REFERENCE_KEY);
    get_flag(
        CUVIS_MESU_FLAG_POOR_WHITE_BALANCING,
        CUVIS_MESU_FLAG_POOR_WHITE_BALANCING_KEY);
    get_flag(CUVIS_MESU_FLAG_DARK_INTTIME, CUVIS_MESU_FLAG_DARK_INTTIME_KEY);
    get_flag(CUVIS_MESU_FLAG_DARK_TEMP, CUVIS_MESU_FLAG_DARK_TEMP_KEY);
    get_flag(CUVIS_MESU_FLAG_WHITE_INTTIME, CUVIS_MESU_FLAG_WHITE_INTTIME_KEY);
    get_flag(CUVIS_MESU_FLAG_WHITE_TEMP, CUVIS_MESU_FLAG_WHITE_TEMP_KEY);
    get_flag(
        CUVIS_MESU_FLAG_WHITEDARK_INTTIME,
        CUVIS_MESU_FLAG_WHITEDARK_INTTIME_KEY);
    get_flag(
        CUVIS_MESU_FLAG_WHITEDARK_TEMP, CUVIS_MESU_FLAG_WHITEDARK_TEMP_KEY);

    int_t numel;
    chk(cuvis_measurement_get_data_count(*_mesu, &numel));

    _gps_data->clear();
    _string_data->clear();
    _image_data->clear();
    _preview_image.reset();
    _sensor_info->clear();

    for (decltype(numel) k = decltype(numel){0}; k < numel; k++)
    {
      CUVIS_CHAR key[CUVIS_MAXBUF];
      cuvis_data_type_t type;
      chk(cuvis_measurement_get_data_info(*_mesu, key, &type, k));

      switch (type)
      {
        case cuvis_data_type_t::data_type_gps: {
          cuvis_gps_t gps;
          chk(cuvis_measurement_get_data_gps(*_mesu, key, &gps));
          _gps_data->emplace(std::string(key), gps);
        }
        break;
        case cuvis_data_type_t::data_type_sensor_info: {
          sensor_info_t info;
          chk(cuvis_measurement_get_data_sensor_info(*_mesu, key, &info));
          _sensor_info->emplace(std::string(key), SensorInfoData(info));
        }
        break;
        case cuvis_data_type_t::data_type_image: {
          cuvis_imbuffer_t im;
          chk(cuvis_measurement_get_data_image(*_mesu, key, &im));
          switch (im.format)
          {
            case cuvis_imbuffer_format_t::imbuffer_format_uint8: {
              image_t<std::uint8_t> image({});
              image._width = im.width;
              image._height = im.height;
              image._channels = im.channels;
              image._data = reinterpret_cast<std::uint8_t const*>(im.raw);
              image._wavelength = im.wavelength;
              image._ref = _mesu;

              _image_data->emplace(std::string(key), image);
              if (std::string(key) == CUVIS_MESU_PREVIEW_KEY)
              {
                _preview_image = std::make_shared<image_t<std::uint8_t>>(image);
              }
              else if (
                  std::string(key) == CUVIS_MESU_PAN_KEY && !_preview_image)
              {
                _preview_image = std::make_shared<image_t<std::uint8_t>>(image);
              }
            }
            break;
            case cuvis_imbuffer_format_t::imbuffer_format_uint16: {
              image_t<std::uint16_t> image({});
              image._width = im.width;
              image._height = im.height;
              image._channels = im.channels;
              image._data = reinterpret_cast<std::uint16_t const*>(im.raw);
              image._wavelength = im.wavelength;
              image._ref = _mesu;

              _image_data->emplace(std::string(key), image);
            }
            break;
            case cuvis_imbuffer_format_t::imbuffer_format_uint32: {
              image_t<std::uint32_t> image({});
              image._width = im.width;
              image._height = im.height;
              image._channels = im.channels;
              image._data = reinterpret_cast<std::uint32_t const*>(im.raw);
              image._wavelength = im.wavelength;
              image._ref = _mesu;

              _image_data->emplace(std::string(key), image);
            }
            break;
            case cuvis_imbuffer_format_t::imbuffer_format_float: {
              image_t<float> image({});
              image._width = im.width;
              image._height = im.height;
              image._channels = im.channels;
              image._data = reinterpret_cast<float const*>(im.raw);
              image._wavelength = im.wavelength;
              image._ref = _mesu;

              _image_data->emplace(std::string(key), image);
            }
            break;
            default: //unknown or unsupported
              throw std::runtime_error(
                  "unsupported measurement data bit depth");
              break;
          }
        }
        break;
        case cuvis_data_type_t::data_type_string: {
          CUVIS_CHAR value[CUVIS_MAXBUF];
          chk(cuvis_measurement_get_data_string(*_mesu, key, value));
          _string_data->emplace(std::string(key), std::string(value));
        }
        break;
        default: // unknown or unsupported
          break;
      }
    }
  }

  inline std::vector<capabilities_t> Measurement::get_capabilities() const
  {
    int32_t bitmap;
    chk(cuvis_measurement_get_capabilities(*_mesu, &bitmap));
    std::vector<capabilities_t> capabilities;
    for (int32_t i = 1; i <= 33554432; i = i * 2)
    {
      if ((bitmap & i) != 0)
      {
        capabilities.push_back(static_cast<capabilities_t>(i));
      }
    }
    return capabilities;
  }

  inline std::string Measurement::get_calib_id() const
  {
    CUVIS_CHAR id[CUVIS_MAXBUF];
    chk(cuvis_measurement_get_calib_id(*_mesu, id));
    std::string res(id);
    return res;
  }

  inline std::string Calibration::get_id() const
  {
    CUVIS_CHAR id[CUVIS_MAXBUF];
    chk(cuvis_calib_get_id(*_calib, id));
    std::string res(id);
    return res;
  }

  inline std::string ProcessingContext::get_calib_id() const
  {
    CUVIS_CHAR id[CUVIS_MAXBUF];
    chk(cuvis_proc_cont_get_calib_id(*_procCont, id));
    std::string res(id);
    return res;
  }

  inline std::vector<capabilities_t>
      Calibration::get_capabilities(CUVIS_OPERATION_MODE mode) const
  {
    int32_t bitmap;
    chk(cuvis_calib_get_capabilities(*_calib, mode, &bitmap));
    std::vector<capabilities_t> capabilities;
    for (int32_t i = 1; i <= 33554432; i = i * 2)
    {
      if ((bitmap & i) != 0)
      {
        capabilities.push_back(static_cast<capabilities_t>(i));
      }
    }
    return capabilities;
  }

  inline image_t<std::uint8_t> const* Measurement::get_thumbnail() const
  {
    return _preview_image.get();
  }

  inline MeasurementMetaData const* Measurement::get_meta() const
  {
    return _meta.get();
  }

  inline cuvis::Measurement::sensor_info_data_t const*
      Measurement::get_sensor_info() const
  {
    return _sensor_info.get();
  }

  inline Calibration::Calibration(std::filesystem::path const& path)
  {
    CUVIS_CALIB calib;
    chk(cuvis_calib_create_from_path(path.string().c_str(), &calib));

    _calib = std::shared_ptr<CUVIS_CALIB>(
        new CUVIS_CALIB{calib}, [](CUVIS_CALIB* handle) {
          cuvis_calib_free(handle);
          delete handle;
        });
  }

  inline Calibration::Calibration(SessionFile const& session)
  {
    CUVIS_CALIB calib;
    chk(cuvis_calib_create_from_session_file(*session._session, &calib));

    _calib = std::shared_ptr<CUVIS_CALIB>(
        new CUVIS_CALIB{calib}, [](CUVIS_CALIB* handle) {
          cuvis_calib_free(handle);
          delete handle;
        });
  }
  inline ProcessingContext::ProcessingContext(Calibration const& calib)
  {
    CUVIS_PROC_CONT procCont;
    chk(cuvis_proc_cont_create_from_calib(*calib._calib, &procCont));
    _procCont = std::shared_ptr<CUVIS_PROC_CONT>(
        new CUVIS_PROC_CONT{procCont}, [](CUVIS_PROC_CONT* handle) {
          cuvis_proc_cont_free(handle);
          delete handle;
        });
  }

  inline ProcessingContext::ProcessingContext(Measurement const& mesu)
  {
    CUVIS_PROC_CONT procCont;
    chk(cuvis_proc_cont_create_from_mesu(*mesu._mesu, &procCont));
    _procCont = std::shared_ptr<CUVIS_PROC_CONT>(
        new CUVIS_PROC_CONT{procCont}, [](CUVIS_PROC_CONT* handle) {
          cuvis_proc_cont_free(handle);
          delete handle;
        });
  }

  inline ProcessingContext::ProcessingContext(SessionFile const& session)
  {
    CUVIS_PROC_CONT procCont;
    chk(cuvis_proc_cont_create_from_session_file(*session._session, &procCont));
    _procCont = std::shared_ptr<CUVIS_PROC_CONT>(
        new CUVIS_PROC_CONT{procCont}, [](CUVIS_PROC_CONT* handle) {
          cuvis_proc_cont_free(handle);
          delete handle;
        });
  }

  inline Measurement& ProcessingContext::apply(Measurement& mesu) const
  {
    chk(cuvis_proc_cont_apply(*_procCont, *mesu._mesu));
    mesu.refresh();
    return mesu;
  }

  inline void ProcessingContext::set_reference(
      Measurement const& mesu, reference_type_t type)
  {
    chk(cuvis_proc_cont_set_reference(*_procCont, *mesu._mesu, type));
    return;
  }
  inline void ProcessingContext::clear_reference(reference_type_t type)
  {
    chk(cuvis_proc_cont_clear_reference(*_procCont, type));
    return;
  }

  inline std::optional<Measurement>
      ProcessingContext::get_reference(reference_type_t type) const
  {
    bool hasRef = has_reference(type);
    if (!hasRef)
    {
      return {};
    }

    CUVIS_MESU handle;
    chk(cuvis_proc_cont_get_reference(*_procCont, &handle, type));

    Measurement mesu(handle);

    return {mesu};
  }

  inline bool ProcessingContext::calc_distance(double distMM)
  {
    chk(cuvis_proc_cont_calc_distance(*_procCont, distMM));
    return true;
  }

  inline bool ProcessingContext::is_capable(
      Measurement const& mesu, ProcessingArgs const& procArgs) const
  {
    int_t isCap;

    cuvis_proc_args_t args;
    args.allow_recalib = procArgs.allow_recalib;
    args.processing_mode = procArgs.processing_mode;
    chk(cuvis_proc_cont_is_capable(*_procCont, *mesu._mesu, args, &isCap));

    return {1 == isCap};
  }

  inline bool ProcessingContext::has_reference(reference_type_t type) const
  {
    int_t hasRef;
    chk(cuvis_proc_cont_has_reference(*_procCont, type, &hasRef));

    return {1 == hasRef};
  }

  inline void
      ProcessingContext::set_processingArgs(ProcessingArgs const& procArgs)
  {
    _procArgs = procArgs;
    chk(cuvis_proc_cont_set_args(*_procCont, _procArgs));
  }

  inline ProcessingArgs const& ProcessingContext::get_processingArgs() const
  {
    return _procArgs;
  }

  inline Worker::Worker(WorkerArgs const& args) : _worker_poll_thread_run(false)

  {
    CUVIS_WORKER worker;
    chk(cuvis_worker_create(&worker, args.operator cuvis_worker_settings_t()));
    _worker = std::shared_ptr<CUVIS_WORKER>(
        new CUVIS_WORKER{worker}, [](CUVIS_WORKER* handle) {
          cuvis_worker_free(handle);
          delete handle;
        });
  }

  inline void Worker::set_acq_cont(AcquisitionContext const* acqCont)
  {
    if (nullptr != acqCont)
    {
      chk(cuvis_worker_set_acq_cont(*_worker, *acqCont->_acqCont));
    }
    else
    {
      chk(cuvis_worker_set_acq_cont(*_worker, CUVIS_HANDLE_NULL));
    }
  }

  // Returns the number of frames processed in total via the future
  inline std::future<int> Worker::set_session_file(
      SessionFile const* session, bool skip_dropped_frames)
  {
    if (session != nullptr)
    {
      chk(cuvis_worker_set_session_file(
          *_worker, *session->_session, skip_dropped_frames ? 1 : 0));
      CUVIS_WORKER this_worker = *_worker;

      auto wait_on_session_done = [this_worker]() {
        const int poll_time_ms = 10;
        CUVIS_INT session_total;
        CUVIS_INT session_current;
        CUVIS_INT status;
        do
        {
          status = cuvis_worker_query_session_progress(
              this_worker, &session_current, &session_total);
        } while (status == status_ok);
        return session_current;
      };

      return std::async(std::launch::deferred, wait_on_session_done);
    }
    else
    {
      chk(cuvis_worker_set_session_file(
          *_worker, CUVIS_HANDLE_NULL, skip_dropped_frames ? 1 : 0));
      auto dummy = []() { return -1; };
      return std::async(std::launch::deferred, dummy);
    }
  }

  inline std::pair<int, int> Worker::query_session_progress()
  {
    CUVIS_INT read = 0;
    CUVIS_INT total = 0;
    if (cuvis_worker_query_session_progress(*_worker, &read, &total) ==
        status_ok)
    {
      return std::make_pair(read, total);
    }
    return std::make_pair(-1, -1);
  }


  inline bool Worker::get_drop_behavior()
  {
    CUVIS_INT canDrop;
    chk(cuvis_worker_get_drop_behavior(*_worker, &canDrop));
    return bool(canDrop);
  }

  inline void Worker::set_drop_behavior(bool canDrop)
  {
    chk(cuvis_worker_set_drop_behavior(*_worker, canDrop ? 1 : 0));
  }

  inline void Worker::set_proc_cont(ProcessingContext const* procCont)
  {
    if (nullptr != procCont)
    {
      chk(cuvis_worker_set_proc_cont(*_worker, *procCont->_procCont));
    }
    else
    {
      chk(cuvis_worker_set_proc_cont(*_worker, CUVIS_HANDLE_NULL));
    }
  }

  inline void Worker::set_exporter(Exporter const* exporter)
  {
    if (nullptr != exporter)
    {
      chk(cuvis_worker_set_exporter(*_worker, *exporter->_exporter));
    }
    else
    {
      chk(cuvis_worker_set_exporter(*_worker, CUVIS_HANDLE_NULL));
    }
  }
  inline void Worker::set_viewer(Viewer const* viewer)
  {
    if (nullptr != viewer)
    {
      chk(cuvis_worker_set_viewer(*_worker, *viewer->_viewer));
    }
    else
    {
      chk(cuvis_worker_set_viewer(*_worker, CUVIS_HANDLE_NULL));
    }
  }

  inline bool Worker::has_next_result() const
  {
    int_t hasNext;
    chk(cuvis_worker_has_next_result(*_worker, &hasNext));
    return hasNext != 0;
  }

  inline void Worker::set_queue_limits(int32_t hard_limit, int32_t soft_limit)
  {
    chk(cuvis_worker_set_queue_limits(*_worker, hard_limit, soft_limit));
    return;
  }

  inline std::pair<int32_t, int32_t> Worker::get_queue_limits() const
  {
    int32_t hard, soft;
    chk(cuvis_worker_get_queue_limits(*_worker, &hard, &soft));
    return std::make_pair(hard, soft);
  }
  inline size_t Worker::get_queue_used() const
  {
    int_t size;
    chk(cuvis_worker_get_queue_used(*_worker, &size));
    return size;
  }
  inline Worker::worker_return_t Worker::get_next_result() const
  {
    try
    {
      CUVIS_VIEW current_view;
      CUVIS_MESU current_mesu;
      chk(cuvis_worker_get_next_result(
          *_worker, &current_mesu, &current_view, 0));

      std::optional<Measurement> mesu;
      std::optional<Viewer::view_data_t> view;
      if (current_mesu != CUVIS_HANDLE_NULL)
      {
        mesu = std::move(Measurement(current_mesu));
        /*
        auto tmp = Measurement(current_mesu);
      mesu = tmp;*/
      }
      if (current_view != CUVIS_HANDLE_NULL)
      {
        view = Viewer::create_view_data(current_view);
      }
      return {std::move(mesu), view, nullptr};
    }
    catch (cuvis::cuvis_sdk_exception const& ex)
    {
      return {{}, {}, std::make_exception_ptr(ex)};
    }
  }

  inline void Worker::register_worker_callback(
      worker_callback_t callback, unsigned concurrency)
  {
    reset_worker_callback();

    static const std::chrono::milliseconds poll_time =
        std::chrono::milliseconds(1);

    _worker_poll_thread_run = true;

    _worker_poll_thread = std::thread([this, callback, concurrency] {
      std::deque<std::future<void>> async_tasks;
      while (_worker_poll_thread_run.load())
      {
        if (has_next_result())
        {
          auto ret = get_next_result();

          async_tasks.push_back(
              std::async(std::launch::async, callback, std::move(ret)));

          if (async_tasks.size() >= concurrency)
          {
            auto& res = async_tasks.front();
            while (true)
            {
              if (res.wait_for(poll_time) == std::future_status::ready)
              {
                break;
              }

              if (!_worker_poll_thread_run.load())

              {
                return;
              }
            }
            try
            {
              res.get();
            }
            catch (...)
            {}

            async_tasks.pop_front();
          }
        }

        else
        {
          std::this_thread::sleep_for(poll_time);
        }
      }
    });
  }

  inline void Worker::reset_worker_callback()
  {
    _worker_poll_thread_run = false;
    if (_worker_poll_thread.joinable())
    {
      _worker_poll_thread.join();
    }
  }

  inline Viewer::Viewer(ViewArgs const& args)
  {
    CUVIS_VIEWER viewer;
    chk(cuvis_viewer_create(&viewer, args));
    _viewer = std::shared_ptr<CUVIS_VIEWER>(
        new CUVIS_VIEWER{viewer}, [](CUVIS_VIEWER* handle) {
          cuvis_viewer_free(handle);
          delete handle;
        });
  }

  inline Viewer::view_data_t Viewer::apply(Measurement const& mesu)
  {
    CUVIS_VIEW current_view;
    chk(cuvis_viewer_apply(*_viewer, *mesu._mesu, &current_view));


    return create_view_data(current_view);
  }
  inline Viewer::view_data_t Viewer::create_view_data(CUVIS_VIEW current_view)
  {
    Viewer::view_data_t view_array;

    auto current_view_handle = std::shared_ptr<CUVIS_VIEW>(
        new CUVIS_VIEW{current_view}, [](CUVIS_VIEW* handle) {
          cuvis_view_free(handle);
          delete handle;
        });


    int_t numel;
    chk(cuvis_view_get_data_count(current_view, &numel));

    for (decltype(numel) k = decltype(numel){0}; k < numel; k++)
    {
      cuvis_view_data_t view_data;
      chk(cuvis_view_get_data(current_view, k, &view_data));


      cuvis_imbuffer_t const& im = view_data.data;



      switch (im.format)
      {
        case cuvis_imbuffer_format_t::imbuffer_format_uint8: {
          view_t<std::uint8_t> view({});
          view._width = im.width;
          view._height = im.height;
          view._channels = im.channels;
          view._data = reinterpret_cast<std::uint8_t const*>(im.raw);
          view._show = (view_data.show != 0);
          view._category = view_data.category;
          view._ref = current_view_handle;

          view_array.emplace(std::string(view_data.id), std::move(view));

          break;
        }
        case cuvis_imbuffer_format_t::imbuffer_format_float: {
          view_t<float> view({});
          view._width = im.width;
          view._height = im.height;
          view._channels = im.channels;
          view._data = reinterpret_cast<float const*>(im.raw);
          view._show = (view_data.show != 0);
          view._category = view_data.category;
          view._ref = current_view_handle;

          view_array.emplace(std::string(view_data.id), view);

          break;
        }

        break;
        default: //unknown or unsupported
          throw std::runtime_error("unsupported view bit depth");
          break;
      }
    }

    return view_array;
  }
  inline AcquisitionContext::~AcquisitionContext()
  {
    reset_state_change_callback();
  }

  inline CUVIS_ACQ_CONT AcquisitionContext::get_handle() const
  {
    return *_acqCont;
  }

  inline AcquisitionContext::AcquisitionContext(Calibration const& calib)
      : _state_poll_thread_run(false)
  {
    CUVIS_ACQ_CONT acqCont;
    chk(cuvis_acq_cont_create_from_calib(*calib._calib, &acqCont));
    _acqCont = std::shared_ptr<CUVIS_ACQ_CONT>(
        new CUVIS_ACQ_CONT{acqCont}, [](CUVIS_ACQ_CONT* handle) {
          cuvis_acq_cont_free(handle);
          delete handle;
        });
  }

  inline AcquisitionContext::AcquisitionContext(
      SessionFile const& sess, bool simulate)
      : _state_poll_thread_run(false)
  {
    CUVIS_ACQ_CONT acqCont;
    chk(cuvis_acq_cont_create_from_session_file(
        *sess._session, simulate, &acqCont));
    //chk(cuvis_proc_cont_create_from_session_file(*sess._session, &acqCont));
    _acqCont = std::shared_ptr<CUVIS_ACQ_CONT>(
        new CUVIS_ACQ_CONT{acqCont}, [](CUVIS_ACQ_CONT* handle) {
          cuvis_acq_cont_free(handle);
          delete handle;
        });
  }


  inline void AcquisitionContext::register_state_change_callback(
      state_callback_t callback, bool output_initial_state)
  {
    reset_state_change_callback();

    _state_poll_thread_run = true;

    _state_poll_thread = std::thread([this, callback, output_initial_state] {
      hardware_state_t last_state = hardware_state_offline;
      std::map<int_t, component_state_info_t> last_component_states;
      for (int k = 0; k < get_component_count(); k++)
      {
        auto info = get_component_info(k);
        last_component_states.emplace(
            k, component_state_info_t{std::string(info.displayname), false});
      }

      bool first_pending = output_initial_state;

      while (_state_poll_thread_run.load())
      {
        bool state_changed = first_pending;
        first_pending = false;

        decltype(last_state) current_state = get_state();
        if (last_state != current_state)
        {
          state_changed = true;
          last_state = current_state;
        }
        for (int k = 0; k < get_component_count(); k++)
        {
          auto comp_state = get_component_online(k) != 0;
          auto last_comp_state = last_component_states[k].is_online;

          if (comp_state != last_comp_state)
          {
            state_changed = true;
            last_component_states[k].is_online = comp_state;
          }
        }
        if (state_changed)
          callback(last_state, last_component_states);
        else
        {
          static const std::chrono::milliseconds poll_time =
              std::chrono::milliseconds(500);
          std::this_thread::sleep_for(poll_time);
        }
      }
    });
  }

  inline void AcquisitionContext::reset_state_change_callback()
  {
    _state_poll_thread_run = false;

    if (_state_poll_thread.joinable())
    {
      _state_poll_thread.join();
    }
  }


  inline Measurement const& Exporter::apply(Measurement const& mesu) const
  {
    chk(cuvis_exporter_apply(*_exporter, *mesu._mesu));
    return mesu;
  }

  inline size_t Exporter::get_queue_used() const
  {
    int_t size;
    chk(cuvis_exporter_get_queue_used(*_exporter, &size));
    return size;
  }

  inline void Exporter::setHandle(CUVIS_EXPORTER exporter)
  {
    _exporter = std::shared_ptr<CUVIS_EXPORTER>(
        new CUVIS_EXPORTER{exporter}, [](CUVIS_EXPORTER* handle) {
          cuvis_exporter_free(handle);
          delete handle;
        });
  }

  inline CubeExporter::CubeExporter(SaveArgs const& args)
  {
    CUVIS_EXPORTER exporter;
    chk(cuvis_exporter_create_cube(&exporter, args, args));
    setHandle(exporter);
  }

  inline TiffExporter::TiffExporter(TiffArgs const& args)
  {
    CUVIS_EXPORTER exporter;
    chk(cuvis_exporter_create_tiff(&exporter, args, args));
    setHandle(exporter);
  }

  inline EnviExporter::EnviExporter(EnviArgs const& args)
  {
    CUVIS_EXPORTER exporter;
    chk(cuvis_exporter_create_envi(&exporter, args));
    setHandle(exporter);
  }

  inline ViewExporter::ViewExporter(ViewArgs const& args)
  {
    CUVIS_EXPORTER exporter;
    chk(cuvis_exporter_create_view(&exporter, args, args));
    setHandle(exporter);
  }

  inline async_result_t Async::get(std::chrono::milliseconds waittime)
  {
    auto result = cuvis_async_call_get(_async.get(), int_t(waittime.count()));
    switch (result)
    {
      case cuvis_status_t::status_ok: return async_result_t::done;
      case cuvis_status_t::status_deferred: return async_result_t::deferred;
      case cuvis_status_t::status_overwritten:
        return async_result_t::overwritten;
      case cuvis_status_t::status_timeout: return async_result_t::timeout;
      default:
        throw cuvis_sdk_exception(
            cuvis_get_last_error_msg(), cuvis_get_last_error_msg_localized());
    }
  }

  inline std::pair<async_result_t, std::optional<Measurement>>
      AsyncMesu::get(std::chrono::milliseconds waittime)
  {
    CUVIS_MESU mesu;
    auto result =
        cuvis_async_capture_get(_async.get(), int_t(waittime.count()), &mesu);
    switch (result)
    {
      case cuvis_status_t::status_ok:
        return {async_result_t::done, Measurement(mesu)};
      case cuvis_status_t::status_deferred:
        return {async_result_t::deferred, {}};
      case cuvis_status_t::status_overwritten:
        return {async_result_t::overwritten, {}};
      case cuvis_status_t::status_timeout: return {async_result_t::timeout, {}};
      default:
        throw cuvis_sdk_exception(
            cuvis_get_last_error_msg(), cuvis_get_last_error_msg_localized());
    }
  }

  inline void AcquisitionContext::capture_queue()
  {
    chk(cuvis_acq_cont_capture_async(*_acqCont, nullptr));
  }

  inline AsyncMesu AcquisitionContext::capture()
  {
    CUVIS_ASYNC_CAPTURE_RESULT asyncRes;
    chk(cuvis_acq_cont_capture_async(*_acqCont, &asyncRes));
    AsyncMesu am;
    am._async = std::shared_ptr<CUVIS_ASYNC_CAPTURE_RESULT>(
        new CUVIS_ASYNC_CAPTURE_RESULT{asyncRes},
        [](CUVIS_ASYNC_CAPTURE_RESULT* handle) {
          cuvis_async_capture_free(handle);
          delete handle;
        });
    return am;
  }

  inline hardware_state_t AcquisitionContext::get_state() const
  {
    CUVIS_HARDWARE_STATE state;
    chk(cuvis_acq_cont_get_state(*_acqCont, &state));
    return state;
  }

  inline std::optional<Measurement> AcquisitionContext::get_next_measurement(
      std::chrono::milliseconds timeout_ms) const
  {
    CUVIS_MESU mesu;
    auto ret = cuvis_acq_cont_get_next_measurement(
        *_acqCont, &mesu, int_t(timeout_ms.count()));
    if (status_ok == ret)
    {
      return Measurement(mesu);
    }
    else if (status_no_measurement == ret)
    {
      return {};
    }

    throw cuvis_sdk_exception(
        cuvis_get_last_error_msg(), cuvis_get_last_error_msg_localized());
  }

  inline bool AcquisitionContext::has_next_measurement() const
  {
    int_t has_next;
    chk(cuvis_acq_cont_has_next_measurement(*_acqCont, &has_next));
    return 1 == has_next;
  }


  inline SessionInfo AcquisitionContext::get_session_info() const
  {
    CUVIS_SESSION_INFO session;
    chk(cuvis_acq_cont_get_session_info(*_acqCont, &session));
    return {session};
  }
  inline int_t AcquisitionContext::get_component_count() const
  {
    int_t count;
    chk(cuvis_acq_cont_get_component_count(*_acqCont, &count));
    return count;
  }
  inline CUVIS_COMPONENT_INFO
      AcquisitionContext::get_component_info(int_t id) const
  {
    CUVIS_COMPONENT_INFO info;
    chk(cuvis_acq_cont_get_component_info(*_acqCont, id, &info));
    return info;
  }
  inline void AcquisitionContext::set_session_info(SessionInfo session)
  {
    auto const csess = session.operator cuvis::session_info_t();
    chk(cuvis_acq_cont_set_session_info(*_acqCont, &csess));
    return;
  }

  inline void AcquisitionContext::set_queue_size(int_t size)
  {
    chk(cuvis_acq_cont_queue_size_set(*_acqCont, size));
    return;
  }

  inline void General::set_log_level(int_t lvl)
  {
    chk(cuvis_set_log_level(lvl));
    return;
  }

  inline void General::set_exception_locale(std::string const& locale)
  {
    chk(cuvis_set_last_error_locale(locale.c_str()));
    return;
  }

  namespace event_impl
  {
    class event_handler_register
    {
    private:
      event_handler_register() = default;

    public:
      static event_handler_register& get_handler_register()
      {
        static event_handler_register reg;
        return reg;
      }

    public:
      event_handler_register(event_handler_register const&) = delete;
      event_handler_register(event_handler_register&&) = delete;
      event_handler_register& operator=(event_handler_register&&) = delete;
      event_handler_register& operator=(event_handler_register const&) = delete;

    private:
      std::mutex mtx_;
      std::map<int_t, cpp_event_callback_t> handler_register_;

      static void handler_function(int_t handler_id, int_t event_id)
      {
        /* handler function gets called from another thread than register/unregister */
        event_handler_register& reg = get_handler_register();
        std::lock_guard lock(reg.mtx_);
        const auto itr = reg.handler_register_.find(handler_id);
        if (itr != reg.handler_register_.end())
        {
          reg.handler_register_[handler_id](event_id);
        }
      }

    public:
      /* register event callback is not threadsafe */
      int_t register_event_callback(cpp_event_callback_t callback, int_t i_type)
      {
        int handler_id = -1;
        chk(cuvis_register_external_event_callback(
            handler_function, i_type, &handler_id));
        if (handler_id >= 0)
        {
          std::lock_guard lock(mtx_);
          handler_register_[handler_id] = callback;
        }
        return handler_id;
      }
      /* unregister event callback is not threadsafe */
      void unregister_event_callback(int_t i_handler_id)
      {
        chk(cuvis_unregister_event_callback(i_handler_id));
        /* we want the lock only after the sdk call to prevent a dead-lock from happening */
        /* e.g. unregister gets lock, but event-queue handle has internal lock, and also wants this lock */
        /* therefore deadlock */
        std::lock_guard lock(mtx_);
        handler_register_.erase(i_handler_id);
      }
    };
  } // namespace event_impl
  inline int_t General::register_event_callback(
      cpp_event_callback_t callback, int_t i_type)
  {
    return event_impl::event_handler_register::get_handler_register()
        .register_event_callback(callback, i_type);
  }
  inline void General::unregister_event_callback(int_t i_handler_id)
  {
    event_impl::event_handler_register::get_handler_register()
        .unregister_event_callback(i_handler_id);
  }

  namespace log_impl
  {
    inline std::mutex log_callback_fun_mutex;
    inline std::function<void(char const*, loglevel_t)> log_callback_fun;
    inline void SDK_CCALL custom_log(char const* msg, loglevel_t lvl)
    {
      log_callback_fun(msg, lvl);
    }
    inline std::mutex log_callback_localized_fun_mutex;
    inline std::function<void(wchar_t const*, loglevel_t)>
        log_callback_localized_fun;
    inline void SDK_CCALL
        custom_log_localized(wchar_t const* msg, loglevel_t lvl)
    {
      log_callback_localized_fun(msg, lvl);
    }
  } // namespace log_impl



  inline void General::register_log_callback(
      std::function<void(char const*, loglevel_t)> callback, int_t min_lvl)
  {
    const std::lock_guard<std::mutex> lock(log_impl::log_callback_fun_mutex);
    log_impl::log_callback_fun = callback;
    chk(cuvis_register_log_callback(
        (log_callback)log_impl::custom_log, min_lvl));

    return;
  }

  inline void General::reset_log_callback()
  {
    const std::lock_guard<std::mutex> lock(log_impl::log_callback_fun_mutex);
    chk(cuvis_reset_log_callback());
    log_impl::log_callback_fun = std::function<void(char const*, loglevel_t)>();
    return;
  }

  inline void General::register_log_callback_localized(
      std::function<void(wchar_t const*, loglevel_t)> callback,
      int_t min_lvl,
      std::string const& loc_id = "")
  {
    const std::lock_guard<std::mutex> lock(
        log_impl::log_callback_localized_fun_mutex);
    log_impl::log_callback_localized_fun = callback;
    chk(cuvis_register_log_callback_localized(
        (log_callback_localized)log_impl::custom_log_localized,
        min_lvl,
        loc_id.c_str()));
    return;
  }

  inline void General::reset_log_callback_localized()
  {
    const std::lock_guard<std::mutex> lock(
        log_impl::log_callback_localized_fun_mutex);
    chk(cuvis_reset_log_callback_localized());
    log_impl::log_callback_localized_fun =
        std::function<void(wchar_t const*, loglevel_t)>();
    return;
  }

  inline std::string General::version()
  {
    CUVIS_CHAR version[CUVIS_MAXBUF];
    chk(cuvis_version(version));
    return std::string(version);
  }

  inline void General::init(std::string const& settings_path)
  {
    chk(cuvis_init(settings_path.c_str()));
    return;
  }

  inline SessionFile::SessionFile(std::filesystem::path const& path)
  {
    CUVIS_SESSION_FILE session;
    chk(cuvis_session_file_load(path.string().c_str(), &session));
    _session = std::shared_ptr<CUVIS_SESSION_FILE>(
        new CUVIS_SESSION_FILE{session}, [](CUVIS_SESSION_FILE* handle) {
          cuvis_session_file_free(handle);
          delete handle;
        });
  }

  inline std::optional<Measurement>
      SessionFile::get_mesu(int_t frameNo, cuvis_session_item_type_t type) const
  {
    CUVIS_MESU mesu;
    const auto ret =
        cuvis_session_file_get_mesu(*_session, frameNo, type, &mesu);

    if (CUVIS_HANDLE_NULL == mesu)
    {
      return {};
    }

    return Measurement(mesu);
  }

    inline std::optional<Measurement>
      SessionFile::get_ref(int_t refNo, cuvis_reference_type_t type) const
  {
    CUVIS_MESU mesu;
    const auto ret =
        cuvis_session_file_get_reference_mesu(*_session, refNo, type, &mesu);

    if (CUVIS_HANDLE_NULL == mesu)
    {
      return {};
    }

    return Measurement(mesu);
  }

  inline int_t SessionFile::get_size(cuvis_session_item_type_t type) const
  {
    int_t size;
    chk(cuvis_session_file_get_size(*_session, type, &size));
    return size;
  }


  inline double SessionFile::get_fps() const
  {
    double fps;
    chk(cuvis_session_file_get_fps(*_session, &fps));
    return fps;
  }

  inline CUVIS_OPERATION_MODE SessionFile::get_operation_mode() const
  {
    CUVIS_OPERATION_MODE op_mode;
    chk(cuvis_session_file_get_operation_mode(*_session, &op_mode));
    return op_mode;
  }

  template <typename data_t>
  inline data_t const& common_image_t<data_t>::get(
      std::size_t x, std::size_t y, std::size_t z) const
  {
    assert(x < _width);
    assert(y < _height);
    assert(z < _channels);
    return _data[((y)*_width + (x)) * _channels + (z)];
  }



  inline GeneralExportArgs::GeneralExportArgs()
      : export_dir("."),
        channel_selection("all"),
        spectra_multiplier(1.0),
        pan_scale(0.0),
        pan_interpolation_type(pan_sharpening_interpolation_type_Linear),
        pan_algorithm(pan_sharpening_algorithm_CubertMacroPixel),
        add_pan(false),
        add_fullscale_pan(false),
        permissive(false),
        blend_opacity(0.0)
  {}

  inline GeneralExportArgs::operator cuvis_export_general_settings_t() const
  {
    cuvis_export_general_settings_t ges({});
    std::strncpy(ges.export_dir, export_dir.string().c_str(), CUVIS_MAXBUF);
    std::strncpy(
        ges.channel_selection, channel_selection.c_str(), CUVIS_MAXBUF);
    ges.spectra_multiplier = spectra_multiplier;
    ges.pan_scale = pan_scale;
    ges.pan_interpolation_type = pan_interpolation_type;
    ges.pan_algorithm = pan_algorithm;
    ges.add_pan = static_cast<int_t>(add_pan);
    ges.add_fullscale_pan = static_cast<int_t>(add_fullscale_pan);
    ges.permissive = static_cast<int_t>(permissive);
    ges.blend_opacity = blend_opacity; 
    return ges;
  }

  inline SaveArgs::SaveArgs()
      : allow_fragmentation(false),
        allow_overwrite(false),
        allow_drop(false),
        allow_session_file(true),
        operation_mode(operation_mode_t::OperationMode_Software),
        fps(0.0),
        allow_info_file(true),
        soft_limit(20),
        hard_limit(100),
        max_buftime(10000)
  {}

  inline SaveArgs::operator cuvis_save_args_t() const
  {
    cuvis_save_args_t save_args;
    save_args.allow_fragmentation = static_cast<int_t>(allow_fragmentation);
    save_args.allow_overwrite = static_cast<int_t>(allow_overwrite);
    save_args.allow_drop = static_cast<int_t>(allow_drop);
    save_args.allow_session_file = static_cast<int_t>(allow_session_file);
    save_args.allow_info_file = static_cast<int_t>(allow_info_file);
    save_args.operation_mode = operation_mode;
    save_args.fps = fps;
    save_args.soft_limit = soft_limit;
    save_args.hard_limit = hard_limit;
    save_args.max_buftime = max_buftime.count();
    return save_args;
  }

  inline ProcessingArgs::ProcessingArgs()
      : processing_mode(processing_mode_t::Cube_Raw), allow_recalib(false)
  {}
  inline ProcessingArgs::operator cuvis_proc_args_t() const
  {
    cuvis_proc_args_t proc_args({});
    proc_args.processing_mode = processing_mode;
    proc_args.allow_recalib = allow_recalib;
    return proc_args;
  }

  inline ViewArgs::ViewArgs()
      : userplugin(), complete(false)
  {}

  inline ViewArgs::operator cuvis_viewer_settings_t() const
  {
    cuvis_viewer_settings_t args;
    args.userplugin = userplugin.c_str();
    args.pan_scale = pan_scale;
    args.pan_interpolation_type = pan_interpolation_type;
    args.pan_algorithm = pan_algorithm;
    args.complete = complete;
    args.blend_opacity = blend_opacity;

    return args;
  }
  inline ViewArgs::operator cuvis_export_view_settings_t() const
  {
    cuvis_export_view_settings_t args;
    args.userplugin = userplugin.c_str();

    return args;
  }

  inline TiffArgs::TiffArgs()
      : compression_mode(tiff_compression_mode_None),
        format(tiff_format_MultiChannel)
  {}

  inline TiffArgs::operator cuvis_export_tiff_settings_t() const
  {
    cuvis_export_tiff_settings_t args;
    args.compression_mode = compression_mode;
    args.format = format;
    return args;
  }

  inline WorkerArgs::WorkerArgs()
      : worker_count(std::thread::hardware_concurrency()),
        poll_interval(std::chrono::milliseconds(5)),
        keep_out_of_sequence(false),
        worker_queue_hard_limit(100),
        worker_queue_soft_limit(90),
        can_drop(false)
  {}

  inline WorkerArgs::operator cuvis_worker_settings_t() const
  {
    cuvis_worker_settings_t args;

    args.worker_count = worker_count;
    args.poll_interval = (std::int32_t)(poll_interval.count());
    args.keep_out_of_sequence = (int)keep_out_of_sequence;
    args.worker_queue_hard_limit = worker_queue_hard_limit;
    args.worker_queue_soft_limit = worker_queue_soft_limit;
    args.can_drop = can_drop;

    return args;
  }

  inline SessionInfo::SessionInfo()
      : name("auto"), session_no(0), sequence_no(0)
  {}

  inline SessionInfo::SessionInfo(session_info_t const& sess)
      : name(sess.name),
        session_no(sess.session_no),
        sequence_no(sess.sequence_no)
  {}

  inline SessionInfo::operator cuvis::session_info_t() const
  {
    session_info_t sess;
    std::strncpy(sess.name, name.c_str(), CUVIS_MAXBUF);
    sess.session_no = static_cast<int_t>(session_no);
    sess.sequence_no = static_cast<int_t>(sequence_no);
    return sess;
  }

  inline MeasurementMetaData::MeasurementMetaData(mesu_metadata_t const& meta)
  {
    name = std::string(meta.name);
    path = std::string(meta.path);
    comment = std::string(meta.comment);
    capture_time = std::chrono::time_point<std::chrono::system_clock>(
        std::chrono::milliseconds(meta.capture_time));
    factory_calibration = std::chrono::time_point<std::chrono::system_clock>(
        std::chrono::milliseconds(meta.factory_calibration));
    product_name = std::string(meta.product_name);
    serial_number = std::string(meta.serial_number);
    assembly = std::string(meta.assembly);
    integration_time = meta.integration_time;
    averages = static_cast<decltype(averages)>(meta.averages);
    auto dist = meta.distance;
    if (dist > 0.0)
    {
      distance = dist;
    }
    else
    {
      distance.reset();
    }


    session_info = SessionInfo();
    session_info.name = meta.session_info_name;
    session_info.sequence_no = meta.session_info_sequence_no;
    session_info.session_no = meta.session_info_session_no;
    processing_mode = meta.processing_mode;
  }

  inline SensorInfoData::SensorInfoData(sensor_info_t const& info)
  {
    averages = info.averages;
    temperature = info.temperature;
    gain = info.gain;
    readout_time = std::chrono::time_point<std::chrono::system_clock>(
        std::chrono::milliseconds(info.readout_time));
  }


  inline cuvis_sdk_exception::cuvis_sdk_exception(
      std::string const& msg, std::wstring const& wmsg)
      : _msg(msg), _wmsg(wmsg)
  {}

  inline char const* cuvis_sdk_exception::what(void) const noexcept
  {
    return _msg.c_str();
  }

  inline std::wstring cuvis_sdk_exception::what_wstr(void) const noexcept
  {
    return _wmsg;
  }
  /** \endcond   */

} // namespace cuvis
