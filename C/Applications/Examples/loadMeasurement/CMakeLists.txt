cmake_minimum_required(VERSION 3.20.0)
project(Example C)
list(APPEND CMAKE_MODULE_PATH
  "${CMAKE_SOURCE_DIR}/../../../SDK/cmake/")
find_package(Cuvis REQUIRED)
add_executable(main main.c)
target_link_libraries(main PRIVATE cuvis::cuvis)