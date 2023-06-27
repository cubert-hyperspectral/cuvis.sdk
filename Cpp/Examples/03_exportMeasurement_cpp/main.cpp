#include "cuvis.hpp"

#include <cassert>
#include <fstream>
#include <iostream>

int main(int argc, char* argv[])
{
  if (argc != 5)
  {
    std::cout << std::endl << "Too few Arguments! Please provide:" << std::endl;
    std::cout << "user settings directory" << std::endl;
    std::cout << "sessionfile (.cu3s)" << std::endl;
    std::cout << "user plugin file (.xml)" << std::endl;
    std::cout << "Name of export directory" << std::endl;

    return -1;
  }
  char* const userSettingsDir = argv[1];
  char* const sessionLoc = argv[2];
  char* const pluginLoc = argv[3];
  char* const exportDir = argv[4];

  std::cout << "Example 03 export measurement" << std::endl;
  std::cout << "User Settings Dir: " << userSettingsDir << std::endl;
  std::cout << "sessionfile (.cu3s): " << sessionLoc << std::endl;
  std::cout << "user plugin file (.xml): " << pluginLoc << std::endl;
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

  assert(mesu.get_meta()->processing_mode != cuvis::processing_mode_t::Preview);

  {
    std::cout << "Export to Envi" << std::endl;
    cuvis::EnviArgs args;
    char exportDirEnvi[CUVIS_MAXBUF];
    strcpy(exportDirEnvi, exportDir);
    strcat(exportDirEnvi, "/envi");
    args.export_dir = exportDirEnvi;
    cuvis::EnviExporter exporter(args);
    exporter.apply(mesu);
  }
  {
    std::cout << "Export to Multi-Channel Tiff" << std::endl;
    cuvis::TiffArgs args;
    char exportDirMulti[CUVIS_MAXBUF];
    strcpy(exportDirMulti, exportDir);
    strcat(exportDirMulti, "/multi");
    args.export_dir = exportDirMulti;
    args.format = cuvis::tiff_format_t::tiff_format_MultiChannel;
    cuvis::TiffExporter exporter(args);
    exporter.apply(mesu);
  }
  {
    std::cout << "Export to separate Tiffs" << std::endl;
    cuvis::TiffArgs args;
    char exportDirSingle[CUVIS_MAXBUF];
    strcpy(exportDirSingle, exportDir);
    strcat(exportDirSingle, "/single");
    args.export_dir = exportDirSingle;
    args.format = cuvis::tiff_format_t::tiff_format_Single;
    cuvis::TiffExporter exporter(args);
    exporter.apply(mesu);
  }
  {
    std::cout << "Export View to file" << std::endl;
    cuvis::ViewArgs args;
    char exportDirView[CUVIS_MAXBUF];
    strcpy(exportDirView, exportDir);
    strcat(exportDirView, "/view");
    args.export_dir = exportDirView;

    std::cout << "Load plugin" << std::endl;
    std::ifstream file(pluginLoc);
    args.userplugin = std::string(
        (std::istreambuf_iterator<char>(file)),
        std::istreambuf_iterator<char>());

    cuvis::ViewExporter exporter(args);
    exporter.apply(mesu);
  }
  {
    std::cout << "Export to sessionfile" << std::endl;
    char exportDirView[CUVIS_MAXBUF];
    strcpy(exportDirView, exportDir);
    strcat(exportDirView, "/session");

    cuvis::SaveArgs saveArgs;
    saveArgs.export_dir = exportDirView;
    saveArgs.allow_overwrite = true;
    saveArgs.allow_session_file = true;

    cuvis::CubeExporter exporter(saveArgs);
    exporter.apply(mesu);
  }
  std::cout << "finished." << std::endl;
}
