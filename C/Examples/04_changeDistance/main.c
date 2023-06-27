#include "cuvis.h"

#include <stdio.h>

int main(int argc, char* argv[])
{
  if (argc != 5)
  {
    printf("To few Arguments! Please provide:\n");
    printf("user settings directory\n");
    printf("sessionfile (.cu3s)\n");
    printf("new distance\n");
    printf("Name of export directory\n");
    fflush(stdout);

    return -1;
  }

  char* const userSettingsDir = argv[1];
  char* const sessionLoc = argv[2];
  char* const distanceString = argv[3];
  char* const exportDir = argv[4];

  int distance = atoi(distanceString);

  printf("Example 04 change distance cpp \n");
  printf(userSettingsDir);
  printf("\nsessionfile (.cu3s): ");
  printf(sessionLoc);
  printf("\nNew Distance: %d\n", distance);
  printf("Export Dir: ");
  printf(exportDir);
  fflush(stdout);

  CUVIS_SESSION_FILE sess;

  CUVIS_MESU mesu;
  CUVIS_MESU_METADATA mesu_data;

  CUVIS_PROC_CONT procCont;

  CUVIS_INT is_capable;

  printf("\nloading settings... \n");
  fflush(stdout);
  CUVIS_CHECK(cuvis_init(userSettingsDir));
#ifdef _DEBUG
  CUVIS_CHECK(cuvis_set_log_level(loglevel_debug));
#else
  CUVIS_CHECK(cuvis_set_log_level(loglevel_info));
#endif

  printf("\nloading session... \n");
  fflush(stdout);
  CUVIS_CHECK(cuvis_session_file_load(sessionLoc, &sess));

  printf("\nloading measurement... \n");
  fflush(stdout);
  CUVIS_CHECK(cuvis_session_file_get_mesu(
      sess, 0, session_item_type_frames_no_gaps, &mesu));

  CUVIS_CHECK(cuvis_measurement_get_metadata(mesu, &mesu_data));
  printf(
      "data 1 %s %.2f ms mode=%d flags=%d\n",
      mesu_data.name,
      mesu_data.integration_time,
      mesu_data.processing_mode,
      mesu_data.measurement_flags);
  fflush(stdout);

  printf("Load calibration and processing context...");
  fflush(stdout);
  CUVIS_CHECK(cuvis_proc_cont_create_from_session_file(sess, &procCont));
  printf(" done. \n");
  fflush(stdout);

  printf("prepare saving of measurements... \n");
  fflush(stdout);
  CUVIS_EXPORTER cube_exporter;

  CUVIS_EXPORT_GENERAL_SETTINGS general_settings = {
      "", //initializer list only takes const char*, leave empty and modify afterwards.
      "all",
      1.0,
      0.0,
      pan_sharpening_interpolation_type_NearestNeighbor,
      pan_sharpening_algorithm_Noop,
      0,
      0};

  strcpy(general_settings.export_dir, exportDir);

  CUVIS_EXPORT_CUBE_SETTINGS cube_settings;
  cube_settings.allow_fragmentation = 0;
  cube_settings.allow_overwrite = 1;
  cube_settings.allow_session_file = 1;

  cuvis_exporter_create_cube(&cube_exporter, general_settings, cube_settings);

  printf("Set distance ...");
  fflush(stdout);
  //CUVIS_CHECK(cuvis_proc_cont_calc_distance(procCont, distance)); // throws error on pan image
  cuvis_proc_cont_calc_distance(procCont, distance);
  printf(" done. \n");
  fflush(stdout);

  CUVIS_PROC_ARGS args;
  args.processing_mode = Cube_Raw;

  CUVIS_CHECK(cuvis_proc_cont_is_capable(procCont, mesu, args, &is_capable));

  if (1 == is_capable)
  {
    printf("reprocess measurement to Cube_Raw with custom distance mode...");
    fflush(stdout);

    CUVIS_CHECK(cuvis_proc_cont_set_args(procCont, args));
    CUVIS_CHECK(cuvis_proc_cont_apply(procCont, mesu));
    printf(" done. \n");
    fflush(stdout);

    CUVIS_CHECK(cuvis_measurement_get_metadata(mesu, &mesu_data));
    printf(
        "data 1 %s %.2f ms mode=%d flags=%d\n",
        mesu_data.name,
        mesu_data.integration_time,
        mesu_data.processing_mode,
        mesu_data.measurement_flags);
    fflush(stdout);

    cuvis_exporter_apply(cube_exporter, mesu);
  }
  else
  {
    printf("Cannot process to Cube_Raw mode.\n");
    fflush(stdout);
  }

  cuvis_exporter_free(&cube_exporter);
  cuvis_proc_cont_free(&procCont);
  cuvis_measurement_free(&mesu);
  printf("finished.");
  fflush(stdout);
}
