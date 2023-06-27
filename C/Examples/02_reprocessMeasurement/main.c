#include "cuvis.h"

#include <stdio.h>

int main(int argc, char* argv[])
{
  if (argc != 7)
  {
    printf("To few Arguments! Please provide:\n");
    printf("user settings directory\n");
    printf("measurement file (.cu3s)\n");
    printf("dark file (.cu3s)\n");
    printf("white file (.cu3s)\n");
    printf("distance file (.cu3s)\n");
    printf("Name of output directory\n");

    return -1;
  }

  char* const userSettingsDir = argv[1];
  char* const measurementLoc = argv[2];
  char* const darkLoc = argv[3];
  char* const whiteLoc = argv[4];
  char* const distanceLoc = argv[5];
  char* const outDir = argv[6];

  printf("Example 02 reprocess measurement \n");
  printf("user Settings Dir: ");
  printf(userSettingsDir);
  printf("\nmeasurement file (.cu3s): ");
  printf(measurementLoc);
  printf("\ndark file (.cu3s): ");
  printf(darkLoc);
  printf("\nwhite file (.cu3s): ");
  printf(whiteLoc);
  printf("\ndistance file (.cu3s): ");
  printf(distanceLoc);
  printf("\noutput Dir: ");
  printf(outDir);

  CUVIS_SESSION_FILE sessMesu;
  CUVIS_SESSION_FILE sessDark;
  CUVIS_SESSION_FILE sessWhite;
  CUVIS_SESSION_FILE sessDistance;

  CUVIS_MESU mesu;
  CUVIS_MESU_METADATA mesu_data;
  CUVIS_MESU dark;
  CUVIS_MESU white;
  CUVIS_MESU distance;

  CUVIS_PROC_CONT procCont;

  CUVIS_INT is_capable;

  printf("\nloading settings... \n");
  fflush(stdout);
  CUVIS_CHECK(cuvis_init(userSettingsDir));

  printf("loading sessionfiles... \n");
  fflush(stdout);
  CUVIS_CHECK(cuvis_session_file_load(measurementLoc, &sessMesu));
  CUVIS_CHECK(cuvis_session_file_load(darkLoc, &sessDark));
  CUVIS_CHECK(cuvis_session_file_load(whiteLoc, &sessWhite));
  CUVIS_CHECK(cuvis_session_file_load(distanceLoc, &sessDistance));

  printf("loading measurement... \n");
  fflush(stdout);
  CUVIS_CHECK(cuvis_session_file_get_mesu(sessMesu, 0, session_item_type_frames_no_gaps, &mesu));
  CUVIS_CHECK(cuvis_session_file_get_mesu(sessDark, 0, session_item_type_frames_no_gaps, &dark));
  CUVIS_CHECK(cuvis_session_file_get_mesu(sessWhite, 0, session_item_type_frames_no_gaps, &white));
  CUVIS_CHECK(cuvis_session_file_get_mesu(sessDistance, 0, session_item_type_frames_no_gaps, &distance));

  CUVIS_CHECK(cuvis_measurement_get_metadata(mesu, &mesu_data));
  printf(
      "data 1 %s %.2f ms mode=%d flags=%d\n",
      mesu_data.name,
      mesu_data.integration_time,
      mesu_data.processing_mode,
      mesu_data.measurement_flags);
  fflush(stdout);

  printf("Load processing context...\n");
  fflush(stdout);
  CUVIS_CHECK(cuvis_proc_cont_create_from_session_file(sessMesu, &procCont));

  printf("Set references ...\n");
  fflush(stdout);
  CUVIS_CHECK(cuvis_proc_cont_set_reference(procCont, dark, Reference_Dark));
  CUVIS_CHECK(cuvis_proc_cont_set_reference(procCont, white, Reference_White));
  CUVIS_CHECK(cuvis_proc_cont_set_reference(procCont, distance, Reference_Distance));

  printf("Prepare processing and export ...\n");
  CUVIS_PROC_ARGS args;
  args.processing_mode = Cube_Raw;
  args.allow_recalib = 0;
  CUVIS_CHECK(cuvis_proc_cont_is_capable(procCont, mesu, args, &is_capable));

  CUVIS_EXPORT_GENERAL_SETTINGS general_settings = {
    "", //initializer list only takes const char*, leave empty and modify afterwards.
    "all",
    1.0,
    0.0,
    pan_sharpening_interpolation_type_NearestNeighbor,
    pan_sharpening_algorithm_Noop,
    0,
    0};

  CUVIS_EXPORT_CUBE_SETTINGS cube_settings;
  cube_settings.allow_fragmentation = 0;
  cube_settings.allow_overwrite = 1;
  cube_settings.allow_session_file = 1;
  cube_settings.operation_mode = OperationMode_Internal;
  cube_settings.allow_info_file = 0;

  if (1 == is_capable)
  {
    printf("reprocess measurement to Cube_Raw mode...\n");
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

    char exportDirRAW[CUVIS_MAXBUF];
    strcpy(exportDirRAW, outDir);
    strcat(exportDirRAW, "/RAW");

    strcpy(general_settings.export_dir, exportDirRAW);
    CUVIS_EXPORTER cube_exporter;
    CUVIS_CHECK(cuvis_exporter_create_cube(
        &cube_exporter, general_settings, cube_settings));
    CUVIS_CHECK(cuvis_exporter_apply(cube_exporter, mesu));
    cuvis_exporter_free(&cube_exporter);
  }
  else
  {
    printf("Cannot process to Cube_Raw mode.\n");
    fflush(stdout);
  }

  args.processing_mode = Cube_DarkSubtract;
  CUVIS_CHECK(cuvis_proc_cont_is_capable(procCont, mesu, args, &is_capable));

  if (1 == is_capable)
  {
    printf("reprocess measurement to Cube_DarkSubtract mode...");
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

    char exportDirDS[CUVIS_MAXBUF];
    strcpy(exportDirDS, outDir);
    strcat(exportDirDS, "/DS");

    strcpy(general_settings.export_dir, exportDirDS);
    CUVIS_EXPORTER cube_exporter;
    CUVIS_CHECK(cuvis_exporter_create_cube(
        &cube_exporter, general_settings, cube_settings));
    CUVIS_CHECK(cuvis_exporter_apply(cube_exporter, mesu));
    cuvis_exporter_free(&cube_exporter);
  }
  else
  {
    printf("Cannot process to Cube_DarkSubtract mode.\n");
    fflush(stdout);
  }

  args.processing_mode = Cube_Reflectance;
  CUVIS_CHECK(cuvis_proc_cont_is_capable(procCont, mesu, args, &is_capable));

  if (1 == is_capable)
  {
    printf("reprocess measurement to Cube_Reflectance mode...\n");
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

    char exportDirREF[CUVIS_MAXBUF];
    strcpy(exportDirREF, outDir);
    strcat(exportDirREF, "/REF");

    strcpy(general_settings.export_dir, exportDirREF);
    CUVIS_EXPORTER cube_exporter;
    CUVIS_CHECK(cuvis_exporter_create_cube(
        &cube_exporter, general_settings, cube_settings));
    CUVIS_CHECK(cuvis_exporter_apply(cube_exporter, mesu));
    cuvis_exporter_free(&cube_exporter);
  }
  else
  {
    printf("Cannot process to Cube_Reflectance mode.\n");
    fflush(stdout);
  }

  args.processing_mode = Cube_SpectralRadiance;
  CUVIS_CHECK(cuvis_proc_cont_is_capable(procCont, mesu, args, &is_capable));

  if (1 == is_capable)
  {
    printf("reprocess measurement to Cube_SpectralRadiance mode...\n");
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

    char exportDirSPRAD[CUVIS_MAXBUF];
    strcpy(exportDirSPRAD, outDir);
    strcat(exportDirSPRAD, "/SPRAD");

    strcpy(general_settings.export_dir, exportDirSPRAD);
    CUVIS_EXPORTER cube_exporter;
    CUVIS_CHECK(cuvis_exporter_create_cube(
        &cube_exporter, general_settings, cube_settings));
    CUVIS_CHECK(cuvis_exporter_apply(cube_exporter, mesu));
    cuvis_exporter_free(&cube_exporter);
  }
  else
  {
    printf("Cannot process to Cube_SpectralRadiance mode.\n");
    fflush(stdout);
  }

  cuvis_proc_cont_free(&procCont);
  cuvis_measurement_free(&mesu);
  cuvis_measurement_free(&dark);
  cuvis_measurement_free(&white);
  cuvis_measurement_free(&distance);
  cuvis_session_file_free(&sessMesu);
  cuvis_session_file_free(&sessDark);
  cuvis_session_file_free(&sessWhite);
  cuvis_session_file_free(&sessDistance);
}
