# Shield Bot

Shield Bot is an autonomous security robot that listens for suspicious sounds, then goes on patrol to look for intruders.  To conserve energy for when it is needed, the robot sits on its charging dock while it continually samples audio clips with its microphone.  These audio clips are fed into a K-means clustering algorithm that has been trained to recognize normal sounds in its environment (e.g. A/C turning on and off, ice maker, etc.).  When an anomalous sound is detected, Shield Bot backs away from the charging dock, then goes on patrol by roaming about and periodically doing a 360 degree turn, capturing images at 90 degree increments.

Images are processed by a FOMO object detection model that has been trained to recognize people.  If a person is detected, the robot plays a loud police siren sound and flashes a red and blue light to scare the intruder away.  A notification about the incident is also sent to the robot's owner.

## Hardware

The base of the robot is an iRobot Create 3, which is basically a Roomba robot vaccuum without the cleaning components.  It provides a pair of motorized wheels with encoders, several infrared and bump sensors, an accelerometer, a gyroscope, and more to act as the base for any number of robotics projects.  These sensors and actuators are accessible via Robot Operating System 2.

Raspberry Pi 4s and NVIDIA Jetsons are officially supported platforms to control the iRobot, and Shield Bot is controlled with a Raspberry Pi 4.  This computer provides the processing power to run the machine learning algorithms, run the application logic, and interact with the iRobot.

A USB webcam was chosen for capturing images, and it also contains a microphone to sample environmental sounds.  A speaker was connected to the Raspberry Pi to play the alarm sound.  The LED ring built in to the iRobot was used for the flashing lights of the alarm.

## Data Collection

audio anomaly

object detection

deploying

result

conclusion
