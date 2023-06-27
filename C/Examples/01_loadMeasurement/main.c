#include "cuvis.h"

#include <assert.h>
#include <stdint.h>
#include <stdio.h>

int main(int argc, char* argv[])
{
  if (argc != 3)
  {
    printf("To few Arguments! Please provide:\n");
    printf("user settings directory\n");
    printf("sessionfile (.cu3s)\n");

    return -1;
  }

  char* const userSettingsDir = argv[1];
  char* const sessionLoc = argv[2];

  CUVIS_SESSION_FILE sess;
  CUVIS_MESU mesu1;
  unsigned chn;

  unsigned x;
  unsigned y;

  const uint16_t* cube16bit;
  //const uint16_t* info_ptr;

  printf("Example 01 load measurement\n");
  printf("\nUser Settings Dir: ");
  printf(userSettingsDir);
  printf("\nsessionfile (.cu3s): ");
  printf(sessionLoc);

  printf("\nloading user settings...\n");
  CUVIS_CHECK(cuvis_init(userSettingsDir));
  CUVIS_CHECK(cuvis_set_log_level(loglevel_info));

  printf("loading session...\n");
  CUVIS_CHECK(cuvis_session_file_load(sessionLoc, &sess));

  printf("loading measurement...\n");
  CUVIS_CHECK(cuvis_session_file_get_mesu(
      sess, 0, session_item_type_frames_no_gaps, &mesu1));

  CUVIS_MESU_METADATA mesu_data;
  CUVIS_CHECK(cuvis_measurement_get_metadata(mesu1, &mesu_data));
  printf(
      "data 1 %s %.2f ms mode=%d flags=%d\n",
      mesu_data.name,
      mesu_data.integration_time,
      mesu_data.processing_mode,
      mesu_data.measurement_flags);

  assert(
      mesu_data.processing_mode == Cube_Raw &&
      "This example requires raw mode");

  CUVIS_IMBUFFER cube;
  CUVIS_CHECK(
      cuvis_measurement_get_data_image(mesu1, CUVIS_MESU_CUBE_KEY, &cube));
  CUVIS_IMBUFFER iminfo;
  cuvis_measurement_get_data_image(mesu1, CUVIS_MESU_CUBE_INFO_KEY, &iminfo);

  CUVIS_CHECK(cuvis_measurement_get_metadata(mesu1, &mesu_data));
  if (mesu_data.measurement_flags & CUVIS_MESU_FLAG_OVERILLUMINATED)
  {
    printf("-- is overilluminated --\n");
  }
  else
  {
    printf("-- is NOT overilluminated --\n");
  }

  if (mesu_data.measurement_flags & CUVIS_MESU_FLAG_POOR_REFERENCE)
  {
    printf("-- has poor reference --\n");
  }
  else
  {
    printf("-- has GOOD reference --\n");
  }

  printf("INFO cube No of channels: %d\n", iminfo.channels);
  printf("INFO cube width: %d\n", iminfo.width);
  printf("INFO cube height: %d\n", iminfo.height);
  printf("DATA cube width: %d\n", cube.width);
  printf("DATA cube height: %d\n", cube.height);
  printf("INFO cube type: %d\n", iminfo.format);
  printf("INFO cube bytes: %d\n", iminfo.bytes);
  printf("DATA cube type: %d\n", cube.format);
  printf("DATA cube bytes: %d\n", cube.bytes);

  assert(
      cube.format == imbuffer_format_uint16 &&
      "16 bit cube required for this example");

  //reinterpret as uint16
  cube16bit = (const uint16_t*)(cube.raw);
  //info_ptr = (const uint16_t*)(iminfo.raw);

  x = 120;
  y = 200;

  assert(x < cube.width && "x index exceeds cube width");
  assert(y < cube.height && "x index exceeds cube width");

  printf("lambda [nm]; raw counts [au]; pixel info \n");
  for (chn = 0; chn < cube.channels; chn++)
  {
    // memory layout:
    //unsigned index = (y * cube.width + x) * cube.channels + chn;
    //uint16_t value = cube16bit[index];

    uint16_t value = IMBUFFER_GET(cube16bit, x, y, chn, cube);
    //only works with v3.X CUVIS data
    //auto pixel_info = IMBUFFER_GET(info_ptr, x, y, 0, iminfo);
    unsigned lambda = cube.wavelength[chn];

    printf(
        "%d; %d \n",
        //"%d; %d; %d \n",
        lambda,
        value
        //pixel_info);
    );
  }
  printf(" \n");

  //for (x = 0; x < cube.width; x++)
  //{
  //  for (y = 0; y < cube.height; y++)
  //  {
  // memory layout:
  //unsigned index = (y * cube.width + x) * cube.channels + chn;
  //uint16_t value = cube16bit[index];

  //auto pixel_info = IMBUFFER_GET(info_ptr, x, y, 0, iminfo);

  //printf("%d; ", pixel_info);
  //  }
  //  printf(" \n");
  //}

  cuvis_measurement_free(&mesu1);
  cuvis_session_file_free(&sess);
  printf("finished.\n");
}
