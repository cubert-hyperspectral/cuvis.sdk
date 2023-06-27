cmake_minimum_required(VERSION 3.20.0)
project(Example)
list(APPEND CMAKE_MODULE_PATH
  "${CMAKE_SOURCE_DIR}/../../SDK/cmake/")
find_package(CuvisCpp REQUIRED)
add_executable(main main.cpp)
target_link_libraries(main PRIVATE cuvis::cpp)