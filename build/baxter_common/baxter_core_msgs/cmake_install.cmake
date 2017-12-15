# Install script for directory: /home/eloise/catkin-ws/src/baxter_common/baxter_core_msgs

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/baxter_core_msgs/msg" TYPE FILE FILES
    "/home/eloise/catkin-ws/src/baxter_common/baxter_core_msgs/msg/AnalogIOState.msg"
    "/home/eloise/catkin-ws/src/baxter_common/baxter_core_msgs/msg/AnalogIOStates.msg"
    "/home/eloise/catkin-ws/src/baxter_common/baxter_core_msgs/msg/AnalogOutputCommand.msg"
    "/home/eloise/catkin-ws/src/baxter_common/baxter_core_msgs/msg/AssemblyState.msg"
    "/home/eloise/catkin-ws/src/baxter_common/baxter_core_msgs/msg/AssemblyStates.msg"
    "/home/eloise/catkin-ws/src/baxter_common/baxter_core_msgs/msg/CameraControl.msg"
    "/home/eloise/catkin-ws/src/baxter_common/baxter_core_msgs/msg/CameraSettings.msg"
    "/home/eloise/catkin-ws/src/baxter_common/baxter_core_msgs/msg/CollisionAvoidanceState.msg"
    "/home/eloise/catkin-ws/src/baxter_common/baxter_core_msgs/msg/CollisionDetectionState.msg"
    "/home/eloise/catkin-ws/src/baxter_common/baxter_core_msgs/msg/DigitalIOState.msg"
    "/home/eloise/catkin-ws/src/baxter_common/baxter_core_msgs/msg/DigitalIOStates.msg"
    "/home/eloise/catkin-ws/src/baxter_common/baxter_core_msgs/msg/DigitalOutputCommand.msg"
    "/home/eloise/catkin-ws/src/baxter_common/baxter_core_msgs/msg/EndEffectorCommand.msg"
    "/home/eloise/catkin-ws/src/baxter_common/baxter_core_msgs/msg/EndEffectorProperties.msg"
    "/home/eloise/catkin-ws/src/baxter_common/baxter_core_msgs/msg/EndEffectorState.msg"
    "/home/eloise/catkin-ws/src/baxter_common/baxter_core_msgs/msg/EndpointState.msg"
    "/home/eloise/catkin-ws/src/baxter_common/baxter_core_msgs/msg/EndpointStates.msg"
    "/home/eloise/catkin-ws/src/baxter_common/baxter_core_msgs/msg/HeadPanCommand.msg"
    "/home/eloise/catkin-ws/src/baxter_common/baxter_core_msgs/msg/HeadState.msg"
    "/home/eloise/catkin-ws/src/baxter_common/baxter_core_msgs/msg/JointCommand.msg"
    "/home/eloise/catkin-ws/src/baxter_common/baxter_core_msgs/msg/NavigatorState.msg"
    "/home/eloise/catkin-ws/src/baxter_common/baxter_core_msgs/msg/NavigatorStates.msg"
    "/home/eloise/catkin-ws/src/baxter_common/baxter_core_msgs/msg/RobustControllerStatus.msg"
    "/home/eloise/catkin-ws/src/baxter_common/baxter_core_msgs/msg/SEAJointState.msg"
    "/home/eloise/catkin-ws/src/baxter_common/baxter_core_msgs/msg/URDFConfiguration.msg"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/baxter_core_msgs/srv" TYPE FILE FILES
    "/home/eloise/catkin-ws/src/baxter_common/baxter_core_msgs/srv/CloseCamera.srv"
    "/home/eloise/catkin-ws/src/baxter_common/baxter_core_msgs/srv/ListCameras.srv"
    "/home/eloise/catkin-ws/src/baxter_common/baxter_core_msgs/srv/OpenCamera.srv"
    "/home/eloise/catkin-ws/src/baxter_common/baxter_core_msgs/srv/SolvePositionIK.srv"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/baxter_core_msgs/cmake" TYPE FILE FILES "/home/eloise/catkin-ws/build/baxter_common/baxter_core_msgs/catkin_generated/installspace/baxter_core_msgs-msg-paths.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/eloise/catkin-ws/devel/include/baxter_core_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/eloise/catkin-ws/devel/share/roseus/ros/baxter_core_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/eloise/catkin-ws/devel/share/common-lisp/ros/baxter_core_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/eloise/catkin-ws/devel/share/gennodejs/ros/baxter_core_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  execute_process(COMMAND "/usr/bin/python" -m compileall "/home/eloise/catkin-ws/devel/lib/python2.7/dist-packages/baxter_core_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/eloise/catkin-ws/devel/lib/python2.7/dist-packages/baxter_core_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/eloise/catkin-ws/build/baxter_common/baxter_core_msgs/catkin_generated/installspace/baxter_core_msgs.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/baxter_core_msgs/cmake" TYPE FILE FILES "/home/eloise/catkin-ws/build/baxter_common/baxter_core_msgs/catkin_generated/installspace/baxter_core_msgs-msg-extras.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/baxter_core_msgs/cmake" TYPE FILE FILES
    "/home/eloise/catkin-ws/build/baxter_common/baxter_core_msgs/catkin_generated/installspace/baxter_core_msgsConfig.cmake"
    "/home/eloise/catkin-ws/build/baxter_common/baxter_core_msgs/catkin_generated/installspace/baxter_core_msgsConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/baxter_core_msgs" TYPE FILE FILES "/home/eloise/catkin-ws/src/baxter_common/baxter_core_msgs/package.xml")
endif()

