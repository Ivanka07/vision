cmake_minimum_required(VERSION 2.8 FATAL_ERROR)
project(noise_removal)

set(CMAKE_CXX_FLAGS "-std=c++0x ${CMAKE_CXX_FLAGS}")

find_package(PCL 1.3 REQUIRED)

include_directories(${PCL_INCLUDE_DIRS})
link_directories(${PCL_LIBRARY_DIRS})
add_definitions(${PCL_DEFINITIONS})

add_executable (pcl_handle_detection pcl_handle_detection.cpp)
target_link_libraries (pcl_handle_detection ${PCL_LIBRARIES})