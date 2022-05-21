#!/bin/sh

ros2 action send_goal /led_animation irobot_create_msgs/action/LedAnimation "{animation_type: 1, lightring: { leds: [{red: 255, green: 0, blue: 0},{red: 255, green: 0, blue: 0},{red: 255, green: 0, blue: 0},{red: 0, green: 0, blue: 255},{red: 0, green: 0, blue: 255},{red: 0, green: 0, blue: 255}]  } , max_runtime: {sec: 15, nanosec: 0} }"

