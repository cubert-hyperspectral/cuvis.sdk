#include "cuvis.hpp"

#include <cassert>
#include <iostream>

int main(int argc, char* argv[])
{
  if (argc != 5)
  {
    std::cout << std::endl << "Too few Arguments! Please provide:" << std::endl;
    std::cout << "user settings directory" << std::endl;
    std::cout << "sessionfile (.cu3s)" << std::endl;
    std::cout << "new distance" << std::endl;
    std::cout << "Name of export directory" << std::endl;

    return -1;
  }

  char* const userSettingsDir = argv[1];
  char* const sessionLoc = argv[2];
  char* const distanceString = argv[3];
  char* const exportDir = argv[4];

  int distance = std::stoi(distanceString);

  std::cout << "Example 04 change distance cpp " << std::endl;
  std::cout << "User Settings Dir: " << userSettingsDir << std::endl;
  std::cout << "sessionfile (.cu3s): " << sessionLoc << std::endl;
  std::cout << "New Distance: " << distance << std::endl;
  std::cout << "Export Dir: " << exportDir << std::endl;

  std::cout << "loading settings... " << std::endl;
  cuvis::General::init(userSettingsDir);
  cuvis::General::set_log_level(loglevel_info);

  std::cout << "loading session... " << std::endl;
  cuvis::SessionFile sess(sessionLoc);

  std::cout << "loading measurement... " << std::endl;
  auto optmesu = sess.get_mesu(0);
  assert(optmesu.has_value());
  cuvis::Measurement mesu = optmesu.value();

  std::cout << "Data 1" << mesu.get_meta()->name << " "
            << "t=" << mesu.get_meta()->integration_time << " ms "
            << "mode=" << mesu.get_meta()->processing_mode << " " << std::endl;

  std::cout << "Loading Calibration and processing context..." << std::endl;
  cuvis::ProcessingContext proc(sess);

  cuvis::SaveArgs saveArgs;
  saveArgs.allow_overwrite = true;
  saveArgs.export_dir = exportDir;
  saveArgs.allow_session_file = true;

  cuvis::CubeExporter exporter(saveArgs);

  std::cout << "setting distance..." << std::endl;
  proc.calc_distance(distance);

  cuvis::ProcessingArgs procArgs = proc.get_processingArgs();
  procArgs.processing_mode = cuvis::processing_mode_t::Cube_Raw;

  assert(proc.is_capable(mesu, procArgs));

  std::cout << "changing distance..." << std::endl;
  proc.apply(mesu);
  std::cout << "saving..." << std::endl;
  exporter.apply(mesu);
  std::cout << "finished." << std::endl;
}
