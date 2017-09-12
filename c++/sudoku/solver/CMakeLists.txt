cmake_minimum_required(VERSION 2.8)

project(solver)

set( project_sources
   main.cpp
   test.cpp
)

add_executable(${PROJECT_NAME} ${project_sources})
