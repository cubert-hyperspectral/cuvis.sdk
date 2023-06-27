#include "cuvis.hpp"

#include <cassert>
#include <iostream>

int main(int argc, char* argv[])
{
  if (argc != 7)
  {
    std::cout << std::endl << "Too few Arguments! Please provide:" << std::endl;
    std::cout << "user settings directory" << std::endl;
    std::cout << "measurement file (.cu3s)" << std::endl;
    std::cout << "dark file (.cu3s)" << std::endl;
    std::cout << "white file (.cu3s)" << std::endl;
    std::cout << "distance file (.cu3s)" << std::endl;
    std::cout << "Name of output directory" << std::endl;

    return -1;
  }

  char* const userSettingsDir = argv[1];
  char* const measurementLoc = argv[2];
  char* const darkLoc = argv[3];
  char* const whiteLoc = argv[4];
  char* const distanceLoc = argv[5];
  char* const outDir = argv[6];

  std::cout << "Example 02 reprocess measurement cpp " << std::endl;
  std::cout << "User Settings Dir: " << userSettingsDir << std::endl;
  std::cout << "measurement file (.cu3s): " << measurementLoc << std::endl;
  std::cout << "dark file (.cu3s): " << darkLoc << std::endl;
  std::cout << "white file (.cu3s): " << whiteLoc << std::endl;
  std::cout << "distance file (.cu3s): " << distanceLoc << std::endl;
  std::cout << "output Dir: " << outDir << std::endl;

  std::cout << "loading settings... " << std::endl;
  cuvis::General::init(userSettingsDir);
  cuvis::General::set_log_level(loglevel_info);

  std::cout << "loading measurement... " << std::endl;
  cuvis::SessionFile sessMesu(measurementLoc);
  auto optMesu = sessMesu.get_mesu(0);
  assert(optMesu.has_value());
  cuvis::Measurement mesu = optMesu.value();

  std::cout << "loading dark... " << std::endl;
  cuvis::SessionFile sessDark(darkLoc);
  auto optDark = sessDark.get_mesu(0);
  assert(optDark.has_value());
  cuvis::Measurement dark = optDark.value();

  std::cout << "loading white... " << std::endl;
  cuvis::SessionFile sessWhite(whiteLoc);
  auto optWhite = sessWhite.get_mesu(0);
  assert(optWhite.has_value());
  cuvis::Measurement white = optWhite.value();

  std::cout << "loading distance... " << std::endl;
  cuvis::SessionFile sessDistance(distanceLoc);
  auto optDistance = sessDistance.get_mesu(0);
  assert(optDistance.has_value());
  cuvis::Measurement distance = optDistance.value();

  std::cout << "Data 1" << mesu.get_meta()->name << " "
            << "t=" << mesu.get_meta()->integration_time << " ms "
            << "mode=" << mesu.get_meta()->processing_mode << " " << std::endl;

  std::cout << "Loading processing context" << std::endl;
  cuvis::ProcessingContext proc(sessMesu);

  std::cout << "Set references" << std::endl;

  proc.set_reference(dark, cuvis::reference_type_t::Reference_Dark);
  proc.set_reference(white, cuvis::reference_type_t::Reference_White);
  proc.set_reference(distance, cuvis::reference_type_t::Reference_Distance);

  cuvis::ProcessingArgs procArgs;
  cuvis::SaveArgs saveArgs;
  saveArgs.allow_overwrite = true;
  saveArgs.allow_session_file = true;
  saveArgs.allow_info_file = false;

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

      cuvis::CubeExporter exporter(saveArgs);
      exporter.apply(mesu);
    }
    else
    {
      std::cout << "cannot process to mode " << mode.first << std::endl;
    }
  }
  std::cout << "finished." << std::endl;
}
