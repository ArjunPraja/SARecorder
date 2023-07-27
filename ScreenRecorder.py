import cv2
import pyautogui
import numpy as np
from win32api import GetSystemMetrics
import time

def ScreenRecorder(t):
    width = GetSystemMetrics(0)
    height = GetSystemMetrics(1)
    dim = (width, height)

    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    output = cv2.VideoWriter("test.mp4", fourcc, 30.0, dim)  # Corrected the frame rate value.

    now_time = time.time()
    duration = t  # Renamed 'dur' to 'duration' for clarity.
    end_time = now_time + duration

    while True:
        image = pyautogui.screenshot()
        frame_1 = np.array(image)
        frame = cv2.cvtColor(frame_1, cv2.COLOR_BGR2RGB)
        output.write(frame)

        current_time = time.time()  # Renamed 'c_time' to 'current_time' for clarity.
        if current_time > end_time:
            break
    print("Finished Screen Recording")
    output.release()
   