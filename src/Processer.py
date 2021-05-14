import cv2
import numpy as np
from pyzbar.pyzbar import decode
from item_info import get_item_info
import keyboard

WINDOW_NAME = 'frame'

class Processer:
    def __init__(self):
        self.cap_cam = cv2.VideoCapture(1)
        cv2.namedWindow(WINDOW_NAME)
        if not self.cap_cam.isOpened():
            exit(1)


    def run(self):
        have_read = []
        while True:
            ret, frame = self.cap_cam.read()
            if not ret:
                break

            cv2.imshow(WINDOW_NAME, frame)
            gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            codes = decode(gray_scale)
            if len(codes) == 0:
                continue

            code = codes[0][0].decode('utf-8', 'ignore')
            if code in have_read:
                continue

            info = get_item_info(code)
            if info is None:
                continue
            
            keyboard.write(info)
            keyboard.send('enter')
            have_read.append(code)
