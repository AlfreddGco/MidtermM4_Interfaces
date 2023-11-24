#!/usr/bin/env python3
import rclpy
from rclpy.node import Node 
from std_msgs.msg import Int32MultiArray

import cv2 
import numpy as np 

import ctypes
from ctypes.util import find_library

rclpy.init()
nh = Node("detection_node")
publisher = nh.create_publisher(Int32MultiArray, '/coordinates', 10)

def publish_coordinates(array):
  msg = Int32MultiArray()
  msg.data = array
  publisher.publish(msg)
  print(array)


def main():
  cap = cv2.VideoCapture(0)
  library = ctypes.cdll.LoadLibrary(find_library("multiplicador"))
  multiply = library.multiplicar_por_100
  
  while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    low_blue = np.array([86, 191, 118])
    high_blue = np.array([133, 255, 255])
    mask = cv2.inRange(hsv, low_blue, high_blue)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
      aproximation = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt,True),True)
      area = cv2.contourArea(cnt)

      if area > 400:
        cv2.drawContours(frame, [cnt], 0, (0,0,0), 5)

        if len(aproximation) == 4:
            M = cv2.moments(cnt)
            if M['m00'] != 0:
              cx = int(M['m10'] / M['m00'])
              cy = int(M['m01'] / M['m00'])
              cv2.drawContours(frame, [cnt], -1, (0, 255, 0), 2)
              cv2.circle(frame, (cx, cy), 7, (0, 0, 255), -1)
              cv2.putText(frame, "center", (cx - 20, cy - 20),
              cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
              publish_coordinates([multiply(cx), multiply(cy)])

    cv2.imshow("video",frame)
    cv2.imshow("mask", mask)
    if (cv2.waitKey(30) == 27):
      break
    
  try:
    rclpy.spin(nh)
  except:
    pass
  finally:
    cv2.destroyAllWindows()
    cap.release()
    nh.destroy_node()
    rclpy.shutdown()

  
if __name__ == '__main__':
  main()