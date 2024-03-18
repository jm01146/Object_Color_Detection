import numpy as np
import cv2


def xy_corr(green_lower, green_upper, kernel, cap):
    # Accesses camera and finds the targeted color and displays it
    while True:
        ret, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # This is the process for the color detection the range from one HSV target to another.
        mask = cv2.inRange(hsv, green_lower, green_upper)
        # This filters out noises such as background and light noises
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

        # Contour definition this allows you to define your detection without glitching effect
        mask_contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # crates a box around the targeted color
        if len(mask_contours) != 0:
            for mask_contours in mask_contours:
                if cv2.contourArea(mask_contours) > 500:
                    x, y, w, h = cv2.boundingRect(mask_contours)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    # print("X:{}, Y:{}".format(x, y))
                    return x, y


# from Color_Coor import *
#
# green_lower = np.array([50, 50, 50], dtype=np.uint8)
# green_upper = np.array([90, 255, 255], dtype=np.uint8)
# kernel = np.ones((25, 25), np.uint8)
#
# # Initializing Video Capture #
# cap = cv2.VideoCapture(0)
#
# while True:
#     print(xy_corr(green_lower, green_upper, kernel, cap))
