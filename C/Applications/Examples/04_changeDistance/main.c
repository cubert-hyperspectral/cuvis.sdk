#include "cuvis.h"

#include <stdio.h>

int main(int argc, char* argv[])
{
  if (argc != 6)
  {
    printf("To few Arguments! Please provide:\n");
    printf("user settings directory\n");
    printf("measurement file (.cu3)\n");
    printf("factory directory\n");
    printf("new distance\n");
    printf("Name of export directory\n");
    fflush(stdout);

    return -1;
  }
  char* const userSettingsDir = argv[1];
  char* const measurementLoc = argv[2];
  char* const factoryDir = argv[3];
  char* const distanceString = argv[4];
  char* const exportDir = argv[5];


  int distance = atoi(distanceString);

  printf("Example 04 change distance cpp \n");
  printf(userSettingsDir);
  printf("\nmeasurement file: ");
  printf(measurementLoc );
  printf( "\nFactory Dir: ");
  printf(factoryDir);
  printf("\nNew Distance: %d\n", distance);
  printf("Export Dir: ");
  printf(exportDir);
  fflush(stdout);







  CUVIS_MESU mesu;
  CUVIS_MESU_METADATA mesu_data;

  CUVIS_CALIB calib;
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


  printf("\nloading measurement... \n");
  fflush(stdout);

  CUVIS_CHECK(cuvis_measurement_load(measurementLoc, &mesu));


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

  CUVIS_CHECK(cuvis_calib_create_from_path(factoryDir, &calib));
  CUVIS_CHECK(cuvis_proc_cont_create_from_calib(calib, &procCont));
  printf(" done. \n");
  fflush(stdout);

  printf("Set distance ...");
  fflush(stdout);

  CUVIS_CHECK(cuvis_proc_cont_calc_distance(procCont, distance));

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

    CUVIS_SAVE_ARGS save_args;
    save_args.allow_fragmentation = 0;
    save_args.allow_overwrite = 1;

    CUVIS_CHECK(cuvis_measurement_save(mesu, exportDir, save_args));
  }
  else
  {
    printf("Cannot process to Cube_Raw mode.\n");
    fflush(stdout);

  }


  cuvis_calib_free(&calib);
  cuvis_proc_cont_free(&procCont);
  cuvis_measurement_free(&mesu);
  printf("finished.");
  fflush(stdout);
}
