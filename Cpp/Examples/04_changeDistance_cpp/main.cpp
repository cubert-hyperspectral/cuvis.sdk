#include "cuvis.hpp"

#include <cassert>
#include <iostream>

int main(int argc, char* argv[])
{   

     if (argc != 6)
  {
    std::cout << std::endl << "To few Arguments! Please provide:" << std::endl;
    std::cout << "user settings directory" << std::endl;
    std::cout << "measurement file (.cu3)" << std::endl;
    std::cout << "factory directory" << std::endl;
    std::cout << "new distance" << std::endl;
    std::cout << "Name of export directory" << std::endl;

    return -1;
  }
  char* const userSettingsDir = argv[1];
  char* const measurementLoc = argv[2];
  char* const factoryDir = argv[3];
  char* const distanceString = argv[4];
  char* const exportDir = argv[5];

  int distance = std::stoi(distanceString);

  std::cout << "Example 04 change distance cpp " << std::endl;
  std::cout << "User Settings Dir: " << userSettingsDir << std::endl;
  std::cout << "measurement file: " << measurementLoc << std::endl;
  std::cout << "Factory Dir: " << factoryDir << std::endl;
  std::cout << "New Distance: " << distance << std::endl;
  std::cout << "Export Dir: " << exportDir << std::endl;

  std::cout << "loading settings... " << std::endl;

    

    cuvis::General::init(userSettingsDir);
    cuvis::General::set_log_level(loglevel_info);

    std::cout << "loading measurement... " << std::endl;
    cuvis::Measurement mesu(measurementLoc);

    std::cout
        << "Data 1" << mesu.get_meta()->name << " "
        << "t=" << mesu.get_meta()->integration_time << " ms "
        << "mode=" << mesu.get_meta()->processing_mode << " "
        << std::endl;

    std::cout << "Loading Calibration and processing context..." << std::endl;

    cuvis::Calibration calib(factoryDir);
    cuvis::ProcessingContext proc(calib);

    std::cout << "Setting distance..." << std::endl;
    proc.calc_distance(distance);

    cuvis::ProcessingArgs procArgs = proc.get_processingArgs();
    procArgs.processing_mode = cuvis::processing_mode_t::Cube_Raw;

    cuvis::SaveArgs saveArgs;
    saveArgs.allow_overwrite = true;
    saveArgs.export_dir = exportDir;

    assert(proc.is_capable(mesu,procArgs));

    std::cout << "changing Distance..." << std::endl;
    proc.apply(mesu);
    std::cout << "saving..." << std::endl;
    mesu.save(saveArgs);
    std::cout << "finished." << std::endl;

    

}
