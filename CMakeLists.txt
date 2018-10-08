cmake_minimum_required(VERSION 2.8.3)
project(demo_install_devel)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  )

add_message_files(
  FILES
)

add_service_files(
  FILES
)

generate_messages(
  DEPENDENCIES
)

catkin_package()

