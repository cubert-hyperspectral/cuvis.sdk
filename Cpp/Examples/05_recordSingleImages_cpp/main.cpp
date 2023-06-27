#include "cuvis.hpp"

#include <cassert>
#include <iostream>

int main(int argc, char* argv[])
{
  if (argc != 6)
  {
    std::cout << std::endl << "Too few Arguments! Please provide:" << std::endl;
    std::cout << "user settings directory" << std::endl;
    std::cout << "factory directory" << std::endl;
    std::cout << "name of recording directory" << std::endl;
    std::cout << "exposure time in ms" << std::endl;
    std::cout << "number of images" << std::endl;

    return -1;
  }

  char* const userSettingsDir = argv[1];
  char* const factoryDir = argv[2];
  char* const recDir = argv[3];
  char* const exposureString = argv[4];
  char* const nrImagesString = argv[5];

  int exposure_ms = std::stoi(exposureString);
  int nrImages = std::stoi(nrImagesString);

  std::cout << "Example 05 record single image " << std::endl;
  std::cout << "User Settings Dir: " << userSettingsDir << std::endl;
  std::cout << "Factory Dir: " << factoryDir << std::endl;
  std::cout << "Recording Dir: " << recDir << std::endl;
  std::cout << "Exposure in ms: " << exposure_ms << std::endl;
  std::cout << "Number of Images: " << nrImages << std::endl;

  std::cout << "loading user settings..." << std::endl;
  cuvis::General::init(userSettingsDir);
  cuvis::General::set_log_level(loglevel_info);

  std::cout << "Loading Calibration and processing context..." << std::endl;
  cuvis::Calibration calib(factoryDir);
  cuvis::ProcessingContext proc(calib);
  cuvis::AcquisitionContext acq(calib);

  cuvis::SaveArgs saveArgs;
  saveArgs.allow_overwrite = true;
  saveArgs.export_dir = recDir;
  saveArgs.allow_session_file = true;

  cuvis::CubeExporter exporter(saveArgs);

  while (cuvis::hardware_state_t::hardware_state_offline == acq.get_state())
  {
    std::this_thread::sleep_for(std::chrono::seconds(1));
  }

  std::cout << "Camera is online" << std::endl;
  acq.set_operation_mode(cuvis::operation_mode_t::OperationMode_Software).get();
  acq.set_integration_time(exposure_ms).get();

  std::cout << "Start recording now" << std::endl;
  for (int k = 0; k < nrImages; k++)
  {
    std::cout << "Record image #" << k << "... (async) ";
    auto async_mesu = acq.capture();
    auto mesu_res = async_mesu.get(std::chrono::milliseconds(500));
    if (mesu_res.first == cuvis::async_result_t::done &&
        mesu_res.second.has_value())
    {
      auto& mesu = mesu_res.second.value();

      proc.apply(mesu);
      exporter.apply(mesu);

      std::cout << "done" << std::endl;
    }
    else
    {
      std::cout << "failed" << std::endl;
    }
  }

  //uncomment for recording in queue mode
  /* 
  for (int k = 0; k < nrImages; k++)
  {
    std::cout << "Record image #" << k << "... (queue)";
    acq.capture_queue();
    auto mesu = acq.get_next_measurement(std::chrono::milliseconds(500));
    if (mesu)
    {
        proc.apply(mesu.value());
        exporter.apply(mesu.value());
        std::cout << "done" << std::endl;
    }
    else
    {
        std::cout << "failed" << std::endl;
    }
    std::cout << "done" << std::endl;
  }
  */
  std::cout << "finished." << std::endl;
}
