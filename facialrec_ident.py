import numpy as np
import cv2
import pickle

face_cascade = cv2.CascadeClassifier('/home/kandarpkakkad/OpenCV-Python-Series/src/cascades/data/haarcascade_frontolface_alt2.xml')



cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors = 5)
    for (x,y,w,h) in faces:
        print(x,y,w,h)

    cv2.imshow('frame', frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
