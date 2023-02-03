#include "cuvis.hpp"

#include <cassert>
#include <iostream>

int main(int argc, char* argv[])
{   

   if (argc != 8)
  {
    std::cout << std::endl << "To few Arguments! Please provide:" << std::endl;
    std::cout << "user settings directory" << std::endl;
    std::cout << "measurement file (.cu3)" << std::endl;
    std::cout << "dark file (.cu3)" << std::endl;
    std::cout << "white file (.cu3)" << std::endl;
    std::cout << "distance file (.cu3)" << std::endl;
    std::cout << "factory directory" << std::endl;
    std::cout << "Name of output directory" << std::endl;

    return -1;
  }
  char* const userSettingsDir = argv[1];
  char* const measurementLoc = argv[2];
  char* const darkLoc = argv[3];
  char* const whiteLoc = argv[4];
  char* const distanceLoc = argv[5];
  char* const factoryDir = argv[6];
  char* const outDir = argv[7];

  std::cout << "Example 02 reprocess measurement cpp " << std::endl;
  std::cout << "User Settings Dir: " << userSettingsDir << std::endl;  
  std::cout << "measurement file: " << measurementLoc << std::endl;
  std::cout << "dark file (.cu3): " << darkLoc << std::endl;
  std::cout << "white file (.cu3): " << whiteLoc << std::endl;
  std::cout << "distance file (.cu3): " << distanceLoc << std::endl;
  std::cout << "Factory Dir: " << factoryDir << std::endl;
  std::cout << "output Dir: " << outDir << std::endl;

  std::cout << "loading settings... " << std::endl;
  cuvis::General::init(userSettingsDir);
  cuvis::General::set_log_level(loglevel_info);

  std::cout << "loading measurment... " << std::endl;
  cuvis::Measurement mesu(measurementLoc);

    std::cout << "loading dark... " << std::endl;
  cuvis::Measurement dark(darkLoc);
    std::cout << "loading white... " << std::endl;
  cuvis::Measurement white(whiteLoc);
    std::cout << "loading distance... " << std::endl;
  cuvis::Measurement distance(distanceLoc);


  std::cout << "Data 1" << mesu.get_meta()->name << " "
            << "t=" << mesu.get_meta()->integration_time << " ms "
            << "mode=" << mesu.get_meta()->processing_mode << " " << std::endl;

  std::cout << "Loading Calibration and processing context (factory)" << std::endl;
  cuvis::Calibration calib(factoryDir);
  cuvis::ProcessingContext proc(calib);

  std::cout << "Set references" << std::endl;

  proc.set_reference(dark, cuvis::reference_type_t::Reference_Dark);
  proc.set_reference(white, cuvis::reference_type_t::Reference_White);
  proc.set_reference(distance, cuvis::reference_type_t::Reference_Distance);

  cuvis::ProcessingArgs procArgs;
  cuvis::SaveArgs saveArgs;
  saveArgs.allow_overwrite = true;

  std::map<std::string, cuvis::processing_mode_t> target_modes = {
      {"Raw", cuvis::processing_mode_t::Cube_Raw},
      {"DS", cuvis::processing_mode_t::Cube_DarkSubtract},
      {"Ref", cuvis::processing_mode_t::Cube_Reflectance}, 
      {"RAD", cuvis::processing_mode_t::Cube_SpectralRadiance}};

  for (auto const& mode : target_modes)
  {
    procArgs.processing_mode = mode.second;
    if (proc.is_capable(mesu, procArgs))
    {
      std::cout << "processing to mode " << mode.first << std::endl;
      proc.set_processingArgs(procArgs);
      proc.apply(mesu);
      saveArgs.export_dir = std::filesystem::path(outDir) / mode.first;
      mesu.save(saveArgs);
    }
    else
    {
        std::cout << "cannot process to mode " << mode.first << std::endl;
    }
  }
  std::cout << "finished." << std::endl;
}
