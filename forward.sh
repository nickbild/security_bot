#!/bin/sh

ros2 action send_goal /drive_distance irobot_create_msgs/action/DriveDistance "{distance: 1.5,max_translation_speed: 0.15}"

