include(GNUInstallDirs)

find_library(
    CUVIS_LIBRARY
    NAMES "cuvis"
    HINTS "/lib/cuvis" "$ENV{PROGRAMFILES}/Cuvis/bin")

find_path(CUVIS_INCLUDE_DIR
  NAMES cuvis.h
  HINTS "/usr/include/" "$ENV{PROGRAMFILES}/Cuvis/sdk/cuvis_c")

include(FindPackageHandleStandardArgs)

find_package_handle_standard_args(Cuvis DEFAULT_MSG
                                  CUVIS_LIBRARY
                                  CUVIS_INCLUDE_DIR)

mark_as_advanced(CUVIS_LIBRARY CUVIS_INCLUDE_DIR)

if(Cuvis_FOUND AND NOT TARGET cuvis::cuvis)
  add_library(cuvis::cuvis STATIC IMPORTED)
  set_target_properties(
    cuvis::cuvis
    PROPERTIES
      INTERFACE_INCLUDE_DIRECTORIES "${CUVIS_INCLUDE_DIR}"
      IMPORTED_LOCATION ${CUVIS_LIBRARY})
endif()