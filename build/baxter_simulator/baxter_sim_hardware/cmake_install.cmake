# Install script for directory: /home/eloise/catkin-ws/src/baxter_simulator/baxter_sim_hardware

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/eloise/catkin-ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/eloise/catkin-ws/build/baxter_simulator/baxter_sim_hardware/catkin_generated/installspace/baxter_sim_hardware.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/baxter_sim_hardware/cmake" TYPE FILE FILES
    "/home/eloise/catkin-ws/build/baxter_simulator/baxter_sim_hardware/catkin_generated/installspace/baxter_sim_hardwareConfig.cmake"
    "/home/eloise/catkin-ws/build/baxter_simulator/baxter_sim_hardware/catkin_generated/installspace/baxter_sim_hardwareConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/baxter_sim_hardware" TYPE FILE FILES "/home/eloise/catkin-ws/src/baxter_simulator/baxter_sim_hardware/package.xml")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/baxter_sim_hardware/baxter_emulator" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/baxter_sim_hardware/baxter_emulator")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/baxter_sim_hardware/baxter_emulator"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/baxter_sim_hardware" TYPE EXECUTABLE FILES "/home/eloise/catkin-ws/devel/lib/baxter_sim_hardware/baxter_emulator")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/baxter_sim_hardware/baxter_emulator" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/baxter_sim_hardware/baxter_emulator")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/baxter_sim_hardware/baxter_emulator"
         OLD_RPATH "/opt/ros/kinetic/lib:/home/eloise/catkin-ws/devel/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/baxter_sim_hardware/baxter_emulator")
    endif()
  endif()
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/baxter_sim_hardware" TYPE DIRECTORY FILES
    "/home/eloise/catkin-ws/src/baxter_simulator/baxter_sim_hardware/config"
    "/home/eloise/catkin-ws/src/baxter_simulator/baxter_sim_hardware/images"
    "/home/eloise/catkin-ws/src/baxter_simulator/baxter_sim_hardware/include"
    "/home/eloise/catkin-ws/src/baxter_simulator/baxter_sim_hardware/launch"
    )
endif()

