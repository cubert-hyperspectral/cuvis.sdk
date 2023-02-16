#include "cuvis.h"

#include <stdio.h>


int main(int argc, char* argv[])
{
  if (argc != 8)
  {
    printf("To few Arguments! Please provide:\n");
    printf("user settings directory\n");
    printf("measurement file (.cu3)\n");
    printf("dark file (.cu3)\n");
    printf("white file (.cu3)\n");
    printf("distance file (.cu3)\n");
    printf("factory directory\n");
    printf("Name of output directory\n");

    return -1;
  }
  char* const userSettingsDir = argv[1];
  char* const measurementLoc = argv[2];
  char* const darkLoc = argv[3];
  char* const whiteLoc = argv[4];
  char* const distanceLoc = argv[5];
  char* const factoryDir = argv[6];
  char* const outDir = argv[7];

  printf("Example 02 reprocess measurement \n");
  printf("user Settings Dir: ");
  printf(userSettingsDir);
   printf("\nmeasurement file: ");
   printf(measurementLoc );
   printf("\ndark file (.cu3): ");
   printf(darkLoc );
  printf("\nwhite file (.cu3): ");
  printf(whiteLoc );
  printf("\ndistance file (.cu3): ");
  printf(distanceLoc );
   printf("\nFactory Dir: ");
  printf(factoryDir);
  printf("\noutput Dir: " );
  printf(outDir );
  


  CUVIS_MESU mesu;
  CUVIS_MESU_METADATA mesu_data;

  CUVIS_MESU dark;
  CUVIS_MESU white;
  CUVIS_MESU distance;

  CUVIS_CALIB calib;
  CUVIS_PROC_CONT procCont;

  CUVIS_INT is_capable;

  CUVIS_SAVE_ARGS save_args;

    
   printf("\nloading settings... \n");
  fflush(stdout);

  CUVIS_CHECK(cuvis_init(userSettingsDir));

  printf("loading measurement... \n");
  fflush(stdout);

  CUVIS_CHECK(cuvis_measurement_load(measurementLoc,
      &mesu));
  CUVIS_CHECK(cuvis_measurement_load(darkLoc, &dark));
  CUVIS_CHECK(cuvis_measurement_load(whiteLoc, &white));
  CUVIS_CHECK(cuvis_measurement_load(distanceLoc,
      &distance));


  CUVIS_CHECK(cuvis_measurement_get_metadata(mesu, &mesu_data));
  printf(
      "data 1 %s %.2f ms mode=%d flags=%d\n",
      mesu_data.name,
      mesu_data.integration_time,
      mesu_data.processing_mode,
      mesu_data.measurement_flags);
  fflush(stdout);



  printf("Load calibration and processing context...\n");
  fflush(stdout);

  CUVIS_CHECK(
      cuvis_calib_create_from_path(factoryDir, &calib));
  CUVIS_CHECK(cuvis_proc_cont_create_from_calib(calib, &procCont));

  printf("Set references ...\n");
  fflush(stdout);


  CUVIS_CHECK(cuvis_proc_cont_set_reference(procCont, dark, Reference_Dark));
  CUVIS_CHECK(
      cuvis_proc_cont_set_reference(procCont, white, Reference_White));
  CUVIS_CHECK(
      cuvis_proc_cont_set_reference(procCont, distance, Reference_Distance));

  CUVIS_PROC_ARGS args;
  args.processing_mode = Cube_Raw;
  args.allow_recalib = 0;
  CUVIS_CHECK(cuvis_proc_cont_is_capable(procCont, mesu, args, &is_capable));

  save_args.allow_fragmentation = 0;
  save_args.allow_overwrite = 1;

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
    CUVIS_CHECK(cuvis_measurement_save(mesu, exportDirRAW, save_args));
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

    CUVIS_CHECK(cuvis_measurement_save(mesu, exportDirDS, save_args));
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
    CUVIS_CHECK(cuvis_measurement_save(mesu, exportDirREF, save_args));
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
    CUVIS_CHECK(cuvis_measurement_save(mesu, exportDirSPRAD, save_args));
  }
  else
  {
    printf("Cannot process to Cube_SpectralRadiance mode.\n");
    fflush(stdout);

  }


  cuvis_calib_free(&calib);
  cuvis_proc_cont_free(&procCont);
  cuvis_measurement_free(&mesu);
  cuvis_measurement_free(&dark);
  cuvis_measurement_free(&white);
  cuvis_measurement_free(&distance);
  ;
}
