import cv2
import numpy as np
import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portsList = []

for onePort in ports:
    portsList.append(str(onePort))
    print(str(onePort))

val = input('Select Port: COM')

for x in range(0, len(portsList)):
    if portsList[x].startswith('COM' + str(val)):
        portVar = 'COM' + str(val)
        print(portVar)

serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()

green_lower = np.array([70, 100, 100], dtype=np.uint8)
green_upper = np.array([90, 255, 255], dtype=np.uint8)

kernel = np.ones((25, 25), np.uint8)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, green_lower, green_upper)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    segemented_color = cv2.bitwise_and(frame, frame, mask=mask)
    mask_contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(mask_contours) != 0:
        for mask_contours in mask_contours:
            if cv2.contourArea(mask_contours) > 500:
                x, y, w, h = cv2.boundingRect(mask_contours)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)
                # print("X:{}, Y:{}".format(x, y))
                command = f"{x},{y}\n"
                serialInst.write(command.encode())

    results = cv2.drawContours(segemented_color, mask_contours, -1, (0, 0, 255), 3)

    cv2.imshow('Frame', frame)
    cv2.imshow('HSV', hsv)
    cv2.imshow('Mask', mask)
    cv2.imshow('Results', results)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
