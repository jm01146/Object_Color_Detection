import numpy as np
import cv2

# Green color detection limits
green_lower = np.array([50, 50, 50], dtype=np.uint8)
green_upper = np.array([90, 255, 255], dtype=np.uint8)

# filter resolution
kernel = np.ones((25, 25), np.uint8)

# Initializing Video Capture #
cap = cv2.VideoCapture(0)

# Define calibration parameters
frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH) # Auto get max width for area
frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) # Auto get max height for area
total_frame_area = frame_width * frame_height
calibration_area = total_frame_area / 2  # 50% of total frame area
calibration_distance = 88.9  # Distance corresponding to calibration area (in mm)


# Accesses camera and finds the targeted color and displays it
while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, green_lower, green_upper)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask_contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    results = frame.copy()
    results = cv2.drawContours(results, mask_contours, -1, (0, 0, 255), 3)

    # crates a box around the targeted color
    if len(mask_contours) != 0:
        for mask_contours in mask_contours:
            if cv2.contourArea(mask_contours) > 500:
                x, y, w, h = cv2.boundingRect(mask_contours)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
                area = w * h
                z = calibration_distance * calibration_area / area
                print("X:{}, Y:{}, Z:{}".format(x, y, z))

# This shows the photo with the box, the mask, and what the computer will see before putting a box this is for debugging
# purposes
    cv2.imshow('Frame', frame)
    cv2.imshow('HSV', hsv)
    cv2.imshow('Mask', mask)
    cv2.imshow('Results', results)

# Waits for the user to hit the q button to close program #
    if cv2.waitKey(1) == ord('q'):
        break

# Allows to release the picture to free used system resources #
cap.release()
cv2.destroyAllWindows()
