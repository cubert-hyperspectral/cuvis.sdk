include(GNUInstallDirs)

find_library(
    CUVIS_LIBRARY
    NAMES "cuvis"
    HINTS "/lib/cuvis" "$ENV{PROGRAMFILES}/Cuvis/bin")

find_path(CUVIS_INCLUDE_DIR
  NAMES cuvis.h
  HINTS "/usr/include/" "$ENV{PROGRAMFILES}/Cuvis/sdk/cuvis_c")

include(FindPackageHandleStandardArgs)

find_package_handle_standard_args(CuvisCpp DEFAULT_MSG
                                  CUVIS_LIBRARY
                                  CUVIS_INCLUDE_DIR)

mark_as_advanced(CUVIS_LIBRARY CUVIS_INCLUDE_DIR)

if(CuvisCpp_FOUND AND NOT TARGET cuvis::cpp)
	
  add_library(cuvis::cpp STATIC IMPORTED)
  
  #simmilar to the c library, we use the cuvis.dll, howver we add 
  #the cpp interface file as well as force the utilizing target to switch to c++17
  set_target_properties(
    cuvis::cpp
    PROPERTIES
      INTERFACE_INCLUDE_DIRECTORIES "${CUVIS_INCLUDE_DIR};${CMAKE_CURRENT_LIST_DIR}/../interface"
      IMPORTED_LOCATION ${CUVIS_LIBRARY})
    target_compile_features(cuvis::cpp INTERFACE cxx_std_17)
endif()