cmake_minimum_required(VERSION 2.8.3)
project(demo_install_devel)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  )

catkin_package()

catkin_install_python(PROGRAMS src/show_file_directory.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

install(DIRECTORY launch/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch)

