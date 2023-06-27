#include "cuvis.h"

#include <assert.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>


int main(int argc, char* argv[])
{
  if (argc != 5)
  {
    printf("To few Arguments! Please provide:\n");
    printf("user settings directory\n");
    printf("sessionfile (.cu3s)\n");
    printf("user plugin file (.xml)\n");
    printf("Name of export directory\n");
    fflush(stdout);

    return -1;
  }
  const char* userSettingsDir = argv[1];
  const char* sessionLoc = argv[2];
  const char* pluginLoc = argv[3];
  const char* exportDir = argv[4];

  printf("Example 03 export measurement\n");
  printf("User Settings Dir: ");
  printf(userSettingsDir);
  printf("\nsessionfile (.cu3s): ");
  printf(sessionLoc);
  printf("\nuser plugin file (.xml): ");
  printf(pluginLoc);
  printf("\nExport Dir: ");
  printf(exportDir);
  fflush(stdout);

  CUVIS_SESSION_FILE sess;
  CUVIS_MESU mesu;

  CUVIS_EXPORTER envi_exporter;
  CUVIS_EXPORTER single_tiff_exporter;

  CUVIS_EXPORT_TIFF_SETTINGS single_tiff_settings;

  CUVIS_EXPORTER multi_tiff_exporter;
  CUVIS_EXPORT_TIFF_SETTINGS multi_tiff_settings;

  CUVIS_EXPORTER view_exporter;
  CUVIS_EXPORT_VIEW_SETTINGS view_settings;

  CUVIS_EXPORTER cube_exporter;

  char* buffer = 0;
  long length;
  FILE* f;

  printf("\nloading user settings...\n");
  fflush(stdout);

  CUVIS_CHECK(cuvis_init(userSettingsDir));
#ifdef _DEBUG
  CUVIS_CHECK(cuvis_set_log_level(loglevel_debug));
#else
  CUVIS_CHECK(cuvis_set_log_level(loglevel_info));
#endif

  CUVIS_EXPORT_GENERAL_SETTINGS general_settings_envi = {
      "", //initializer list only takes const char*, leave empty and modify afterwards.
      "all",
      1.0,
      0.0,
      pan_sharpening_interpolation_type_NearestNeighbor,
      pan_sharpening_algorithm_Noop,
      0,
      0};

  char exportDirEnvi[CUVIS_MAXBUF];
  strcpy(exportDirEnvi, exportDir);
  strcat(exportDirEnvi, "/envi");
  strcpy(general_settings_envi.export_dir, exportDirEnvi);

  CUVIS_EXPORT_GENERAL_SETTINGS general_settings_single = {
      "", //initializer list only takes const char*, leave empty and modify afterwards.
      "all",
      1.0,
      0.0,
      pan_sharpening_interpolation_type_NearestNeighbor,
      pan_sharpening_algorithm_Noop,
      0,
      0};
  char exportDirSingle[CUVIS_MAXBUF];
  strcpy(exportDirSingle, exportDir);
  strcat(exportDirSingle, "/single");
  strcpy(general_settings_single.export_dir, exportDirSingle);

  CUVIS_EXPORT_GENERAL_SETTINGS general_settings_multi = {
      "", //initializer list only takes const char*, leave empty and modify afterwards.
      "all",
      1.0,
      0.0,
      pan_sharpening_interpolation_type_NearestNeighbor,
      pan_sharpening_algorithm_Noop,
      0,
      0};
  char exportDirMulti[CUVIS_MAXBUF];
  strcpy(exportDirMulti, exportDir);
  strcat(exportDirMulti, "/multi");
  strcpy(general_settings_multi.export_dir, exportDirMulti);

  CUVIS_EXPORT_GENERAL_SETTINGS general_settings_view = {
      "", //initializer list only takes const char*, leave empty and modify afterwards.
      "all",
      1.0,
      0.0,
      pan_sharpening_interpolation_type_NearestNeighbor,
      pan_sharpening_algorithm_Noop,
      0,
      0};
  char exportDirView[CUVIS_MAXBUF];
  strcpy(exportDirView, exportDir);
  strcat(exportDirView, "/view");
  strcpy(general_settings_view.export_dir, exportDirView);

  CUVIS_EXPORT_CUBE_SETTINGS cube_settings_session = {
      0, 1, 0, 1, 1, OperationMode_Software, 1.0, 64, 128, 60000};
  CUVIS_EXPORT_GENERAL_SETTINGS general_settings_session = {
      "", //initializer list only takes const char*, leave empty and modify afterwards.
      "all",
      1.0,
      0.0,
      pan_sharpening_interpolation_type_NearestNeighbor,
      pan_sharpening_algorithm_Noop,
      0,
      0};
  char exportDirSession[CUVIS_MAXBUF];
  strcpy(exportDirSession, exportDir);
  strcat(exportDirSession, "/session");
  strcpy(general_settings_session.export_dir, exportDirSession);

  printf("loading session ...\n");
  fflush(stdout);
  CUVIS_CHECK(cuvis_session_file_load(sessionLoc, &sess));

  printf("loading measurement ...\n");
  fflush(stdout);
  CUVIS_CHECK(cuvis_session_file_get_mesu(
      sess, 0, session_item_type_frames_no_gaps, &mesu));

  printf("creating envi exporter ...\n");
  fflush(stdout);
  CUVIS_CHECK(
      cuvis_exporter_create_envi(&envi_exporter, general_settings_envi));
  printf(" done.\n");
  fflush(stdout);

  printf("creating single tiff exporter ...\n");
  fflush(stdout);

  single_tiff_settings.compression_mode = tiff_compression_mode_None;
  single_tiff_settings.format = tiff_format_Single;
  CUVIS_CHECK(cuvis_exporter_create_tiff(
      &single_tiff_exporter, general_settings_single, single_tiff_settings));
  printf(" done.\n");
  fflush(stdout);

  printf("creating multi tiff exporter ...\n");
  fflush(stdout);

  multi_tiff_settings.compression_mode = tiff_compression_mode_None;
  multi_tiff_settings.format = tiff_format_MultiChannel;
  CUVIS_CHECK(cuvis_exporter_create_tiff(
      &multi_tiff_exporter, general_settings_multi, multi_tiff_settings));
  printf(" done.\n");
  fflush(stdout);

  printf("creating view exporter ...\n");
  printf("loading plugin ...\n");
  fflush(stdout);

  f = fopen(pluginLoc, "rb");

  if (f)
  {
    fseek(f, 0, SEEK_END);
    length = ftell(f);
    fseek(f, 0, SEEK_SET);
    buffer = malloc(length);
    if (buffer)
    {
      fread(buffer, 1, length, f);
    }
    fclose(f);
  }
  if (!buffer)
  {
    printf("failed to load plugin file\n");
    fflush(stdout);

    return 0;
  }

  view_settings.userplugin = buffer;
  CUVIS_CHECK(cuvis_exporter_create_view(
      &view_exporter, general_settings_view, view_settings));
  printf(" done.\n");
  fflush(stdout);

  printf("creating cube exporter (session) ...\n");
  fflush(stdout);
  CUVIS_CHECK(cuvis_exporter_create_cube(
      &cube_exporter, general_settings_session, cube_settings_session));
  printf(" done.\n");
  fflush(stdout);

  printf("export envi...");
  fflush(stdout);

  CUVIS_CHECK(cuvis_exporter_apply(envi_exporter, mesu));
  printf(" done.\n");
  fflush(stdout);

  printf("export single tiff...");
  fflush(stdout);
  CUVIS_CHECK(cuvis_exporter_apply(single_tiff_exporter, mesu));
  printf(" done.\n");
  fflush(stdout);

  printf("export multi tiff...");
  fflush(stdout);

  CUVIS_CHECK(cuvis_exporter_apply(multi_tiff_exporter, mesu));
  printf(" done.\n");
  fflush(stdout);

  printf("export view...");
  fflush(stdout);

  CUVIS_CHECK(cuvis_exporter_apply(view_exporter, mesu));
  printf("done.\n");
  fflush(stdout);

  printf("export cube (session)...");
  fflush(stdout);

  CUVIS_CHECK(cuvis_exporter_apply(cube_exporter, mesu));
  printf("done.\n");
  fflush(stdout);

  cuvis_measurement_free(&mesu);
  cuvis_session_file_free(&sess);
  cuvis_exporter_free(&envi_exporter);
  cuvis_exporter_free(&single_tiff_exporter);
  cuvis_exporter_free(&multi_tiff_exporter);
  cuvis_exporter_free(&view_exporter);
  cuvis_exporter_free(&cube_exporter);

  free(buffer);
  printf("finished.\n");
  fflush(stdout);

  return 0;
}
