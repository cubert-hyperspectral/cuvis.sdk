#include "cuvis.h"

#include <signal.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

#ifdef WIN32
  #include <Windows.h>
#else
  #include <unistd.h>
#endif

int keepRunning = 1;

void signal_handler(int sig)
{
  printf("\nsignal received. Stopping acquisiton...\n");
  fflush(stdout);
  (void)sig;
  keepRunning = 0;
}

int main(int argc, char* argv[])
{
  if (argc != 7)
  {
    printf("To few Arguments! Please provide:\n");
    printf("user settings directory\n");
    printf("sessionfile\n");
    printf("name of recording directory\n");
    printf("exposure time in ms\n");
    printf("auto exposure [1/0]\n");
    printf("target fps\n");
    fflush(stdout);

    return -1;
  }

  char* const userSettingsDir = argv[1];
  char* const sessionfile = argv[2];
  char* const recDir = argv[3];
  char* const exposureString = argv[4];
  char* const autoExpString = argv[5];
  char* const fpsString = argv[6];

  int exposure_ms = atoi(exposureString);
  bool autoExp = false;
  if (atoi(autoExpString) == 1)
  {
    autoExp = true;
  }
  double fps = atof(fpsString);

  printf("Example 06 video");
  printf("\nUser Settings Dir: ");
  printf(userSettingsDir);
  printf("\Sessionfile: ");
  printf(sessionfile);
  printf("\nRecording Dir: ");
  printf(recDir);
  printf("\nExposure in ms: %d\n", exposure_ms);
  printf("Auto Exposure: %d\n", autoExp);
  printf("Target FPS: %4.2f\n", fps);
  fflush(stdout);

  CUVIS_SESSION_FILE sessFile;
  CUVIS_ACQ_CONT acqCont;
  CUVIS_PROC_CONT procCont;

  printf("loading user settings...\n");
  fflush(stdout);
  CUVIS_CHECK(cuvis_init(userSettingsDir));

  printf("loading session file... \n");
  fflush(stdout);
  CUVIS_CHECK(cuvis_session_file_load(sessionfile, &sessFile));

  printf("loading acquisition context... \n");
  fflush(stdout);
  CUVIS_CHECK(cuvis_acq_cont_create_from_session_file(
      sessFile,
      1,
      &acqCont)); // simulating = true --> use frames from sessionfile instead of real camera

  printf("load processing context \n");
  fflush(stdout);
  CUVIS_CHECK(cuvis_proc_cont_create_from_session_file(sessFile, &procCont));

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
  cube_settings.allow_session_file = 1;
  cube_settings.fps = fps;
  cube_settings.operation_mode = OperationMode_Internal;
  cube_settings.allow_info_file = 1;

  CUVIS_CHECK(cuvis_exporter_create_cube(
      &cube_exporter, general_settings, cube_settings));

  CUVIS_PROC_ARGS procArgs;
  procArgs.allow_recalib = 0;
  procArgs.processing_mode = Cube_Raw;

  CUVIS_SESSION_INFO sess = {"video", 0, 0};
  CUVIS_CHECK(cuvis_acq_cont_set_session_info(acqCont, &sess));

  printf("waiting for simulated camera to become ready...\n");
  fflush(stdout);
  for (;;)
  {
    CUVIS_HARDWARE_STATE state;
    CUVIS_CHECK(cuvis_acq_cont_get_state(acqCont, &state));

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

  CUVIS_CHECK(cuvis_acq_cont_integration_time_set(acqCont, 100));
  CUVIS_CHECK(
      cuvis_acq_cont_operation_mode_set(acqCont, OperationMode_Internal));
  CUVIS_CHECK(cuvis_acq_cont_fps_set(acqCont, fps));
  CUVIS_CHECK(cuvis_acq_cont_queue_size_set(acqCont, 10));
  CUVIS_CHECK(cuvis_acq_cont_continuous_set(acqCont, 0));
  CUVIS_CHECK(cuvis_proc_cont_set_args(procCont, procArgs));

  cuvis_acq_cont_preview_mode_set(acqCont, 1);
  CUVIS_WORKER worker;
  CUVIS_WORKER_SETTINGS worker_settings;
  worker_settings.keep_out_of_sequence = 0;
  worker_settings.poll_interval = 10;
#ifdef _DEBUG
  worker_settings.worker_count = 1;
#else
  worker_settings.worker_count =
      0; // =0 automatically sets the worker to the systems number of V-Cores
#endif

  worker_settings.worker_queue_hard_limit = 20;
  worker_settings.worker_queue_soft_limit = 20 - worker_settings.worker_count;
  worker_settings.can_drop = 1;
  cuvis_worker_create(&worker, worker_settings);

  cuvis_worker_set_acq_cont(worker, acqCont);
  cuvis_worker_set_proc_cont(worker, procCont);
  cuvis_worker_set_exporter(worker, cube_exporter);

  printf("registering signal for CTRL+c (cancel recording) \n");
  fflush(stdout);
  signal(SIGINT, signal_handler);

  printf("recording...\n");
  fflush(stdout);
  CUVIS_CHECK(cuvis_acq_cont_continuous_set(acqCont, 1));

  CUVIS_INT used_queue;
  CUVIS_INT queue_limit;

  while (0 != keepRunning)
  {
    CUVIS_MESU mesu;
    CUVIS_INT hasNext = 0;
    do
    {
      cuvis_worker_has_next_result(worker, &hasNext);

      if (hasNext != 0)
      {
        break;
      }
#ifdef WIN32
      Sleep(10);
#else
      usleep(10000);
#endif
    } while (0 != keepRunning);

    cuvis_worker_get_queue_limits(worker, &queue_limit, NULL);
    cuvis_worker_get_queue_used(worker, &used_queue);
    if (used_queue == queue_limit)
    {
      printf("Worker queue is full! Main() loop can not keep up!");
      fflush(stdout);
    }

    cuvis_acq_cont_queue_size_get(acqCont, &used_queue);
    cuvis_acq_cont_queue_used_get(acqCont, &used_queue);
    if (used_queue == queue_limit)
    {
      printf("Acquisition queue is full! Worker can not keep up!");
      fflush(stdout);
    }

    if (cuvis_worker_get_next_result(acqCont, &mesu, NULL, 0) != status_ok)
    {
      printf("Worker error, details: %s\n", cuvis_get_last_error_msg());
      fflush(stdout);
    }

    if (mesu)
    {
      CUVIS_MESU_METADATA mesu_data;
      CUVIS_CHECK(cuvis_measurement_get_metadata(mesu, &mesu_data));
      printf(
          "\rcurrent handle index: %04d", mesu_data.session_info_sequence_no);
      fflush(stdout);

      cuvis_measurement_free(&mesu);
    }
  }
  signal(SIGINT, SIG_DFL);

  printf("cleaning up\n");
  fflush(stdout);
  cuvis_worker_free(&worker);
  cuvis_exporter_free(&cube_exporter);
  cuvis_acq_cont_free(&acqCont);
  cuvis_proc_cont_free(&procCont);
  cuvis_session_file_free(&sessFile);
  printf("finished \n");
  fflush(stdout);
}
