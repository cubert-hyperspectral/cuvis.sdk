#include "cuvis.h"
#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#ifdef WIN32
#include <Windows.h>
#else
#include <unistd.h>
#endif

int main(int argc, char* argv[])
{

     if (argc != 6)
  {
    printf("To few Arguments! Please provide:\n");
    printf("user settings directory\n");
    printf("factory directory\n");
    printf("name of recording directory\n");
    printf("exposure time in ms\n");
    printf("number of images\n");
    fflush(stdout);

    return -1;
  }
  char* const userSettingsDir = argv[1];
  char* const factoryDir = argv[2];
  char* const recDir = argv[3];
  char* const exposureString = argv[4];
  char* const nrImagesString = argv[5];


  int exposure_ms = atoi(exposureString);
  int nrImages = atoi(nrImagesString);

    printf("Example 05 record single image\n");
    printf("User Settings Dir: ");
    printf(userSettingsDir);
    printf("\nFactory Dir: "); 
    printf(factoryDir);
    printf("\nRecording Dir: ");
    printf(recDir);
    printf("\nExposure in ms: %d\n", exposure_ms);
    printf("Number of Images: %d\n", nrImages);
    fflush(stdout);
 



  CUVIS_CALIB calib;
  CUVIS_ACQ_CONT acqCont;
  CUVIS_PROC_CONT procCont;


 printf("loading user settings...\n");
  fflush(stdout);
  CUVIS_CHECK(
      cuvis_init(userSettingsDir));


  printf("load calibration...\n");
  fflush(stdout);
  CUVIS_CHECK(cuvis_calib_create_from_path(factoryDir, &calib));

  printf("loading processing context... \n");
  fflush(stdout);
  CUVIS_CHECK(cuvis_proc_cont_create_from_calib(calib, &procCont));

  printf("load acquisition context...\n");
  fflush(stdout);
  CUVIS_CHECK(cuvis_acq_cont_create_from_calib(calib, &acqCont));


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

  strcpy(general_settings.export_dir, recDir);


  CUVIS_EXPORT_CUBE_SETTINGS cube_settings;
  cube_settings.allow_fragmentation = 0;
  cube_settings.allow_overwrite = 1;
  cube_settings.allow_session_file = 0;

  CUVIS_WORKER_SETTINGS worker_settings;
  worker_settings.keep_out_of_sequence = 1;
  worker_settings.poll_interval = 0;
  worker_settings.worker_count = 0;
  worker_settings.worker_queue_size = 0;

  cuvis_exporter_create_cube(&cube_exporter, general_settings, cube_settings);
      
  CUVIS_WORKER worker;
  cuvis_worker_create(&worker, worker_settings);



  CUVIS_PROC_ARGS procArgs;
  procArgs.allow_recalib = 0;
  procArgs.processing_mode = Cube_Raw;



  printf("waiting for camera to become online...\n");
  fflush(stdout);
  for (;;)
  {
    CUVIS_HARDWARE_STATE state;
    cuvis_acq_cont_get_state(acqCont, &state);

    if (state == hardware_state_online)
    {
      printf("\ncamera online\n");
      fflush(stdout);
      break;
    }
    if (state == hardware_state_partially_online)
    {
      printf("\ncamera partially online\n");
      fflush(stdout);
      break;
    }

#ifdef WIN32
    Sleep(1000);
#else
    usleep(1000000);
#endif
    printf(".");
    fflush(stdout);
  }

  printf("component details:\n");
  fflush(stdout);
  CUVIS_INT compCount;
  CUVIS_CHECK(cuvis_acq_cont_get_component_count(acqCont, &compCount));
  for (unsigned compIdx = 0; compIdx < compCount; compIdx++)
  {
    CUVIS_INT online;
    CUVIS_COMPONENT_INFO cinfo;

    CUVIS_CHECK(cuvis_acq_cont_get_component_info(acqCont, compIdx, &cinfo));
    CUVIS_CHECK(cuvis_comp_online_get(acqCont, compIdx, &online));
    printf(" - component '%s' is ", cinfo.displayname);
    fflush(stdout);
    if (online != 0)
    {
      printf("online\n");
      fflush(stdout);
    }
    else
    {
      printf("offline\n");
      fflush(stdout);
    }
    printf(" -- info:        %s\n", cinfo.sensorinfo);
    printf(" -- use:         %s\n", cinfo.userfield);
    printf(" -- pixelformat: %s\n", cinfo.pixelformat);
    fflush(stdout);
  }

  printf("initializing hardware...\n");
  fflush(stdout);
  cuvis_acq_cont_integration_time_set(acqCont, exposure_ms);
  cuvis_acq_cont_operation_mode_set(acqCont, OperationMode_Software);
  ACQ_SET_SINGLE_VALUE(cuvis_acq_cont_auto_exp, CUVIS_INT, 1);


  printf("start recording now\n");
  fflush(stdout);

  for (int k = 0; k < nrImages; k++)
  {
    CUVIS_MESU mesu;
    CUVIS_VIEW view;
    

    printf("trigger image nr. %d/10 (software) \n", k + 1);
    fflush(stdout);
    cuvis_worker_set_acq_cont(worker, acqCont);
    cuvis_worker_set_proc_cont(worker, procCont);
    cuvis_worker_set_exporter(worker, cube_exporter);

    CUVIS_INT hasNext;
    cuvis_worker_has_next_result(worker, &hasNext);

    if (hasNext)
    {
      cuvis_worker_get_next_result(worker, &mesu, &view);
      printf("recorded mesu (id %d)\n", k);
      printf("process mesu  (id %d)\n", k);
      fflush(stdout);
      CUVIS_CHECK(cuvis_proc_cont_set_args(procCont, procArgs));
      CUVIS_CHECK(cuvis_proc_cont_apply(procCont, mesu));



      printf("save to cu3   (id %d) \n", k);
      fflush(stdout);
      //the cube exporter exports the measurement and sets the path in the measurement's meta-data
      cuvis_exporter_apply(cube_exporter, mesu);

      CUVIS_MESU_METADATA mesu_data;
      CUVIS_CHECK(cuvis_measurement_get_metadata(mesu, &mesu_data));

      printf("location: %s/%s.cu3\n", mesu_data.path, mesu_data.name);

      printf("release mesu  (id %d)\n", k);
      fflush(stdout);
      cuvis_measurement_free(&mesu);
    }
    else
    {
#ifdef WIN32
      Sleep(500);
#else
      usleep(50000);
#endif
    }
  }
  printf("done. cleaning up...\n");
  fflush(stdout);


  cuvis_exporter_free(&cube_exporter);
  cuvis_proc_cont_free(&procCont);
  cuvis_acq_cont_free(&acqCont);
  cuvis_calib_free(&calib);
  cuvis_worker_free(&worker);
  printf("finished.\n");
  fflush(stdout);
}
