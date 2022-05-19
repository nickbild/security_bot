import cv2
import sys
import time


camera = cv2.VideoCapture(0)
start = int(sys.argv[1])
stop = int(sys.argv[2])


for cnt in range(start, stop, 1):
    print(cnt)
    _, image = camera.read()
    cv2.imwrite('image_data/img_{0}.jpg'.format(cnt), image)
    time.sleep(0.5)
