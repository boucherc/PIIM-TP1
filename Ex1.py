import cv2
import numpy as np
import datetime


outpath = 'output_ex1.avi'
fps = 30.0
mirror = False
percentage = 15
cap = cv2.VideoCapture(0)

firstFrame = None
currentFrame = 0

font = cv2.FONT_HERSHEY_DUPLEX

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
totalPixel = int(width * height)

fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter(outpath, fourcc, fps, (int(width), int(height)))

while cap.isOpened():

    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if firstFrame is None:
        firstFrame = gray
        continue

    frameDelta = cv2.absdiff(firstFrame, gray)
    thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]

    thresh = cv2.dilate(thresh, None, iterations=2)

    whitePixel = np.sum(thresh == 255)
    if whitePixel > totalPixel * (percentage / 100):

        print("alarm: {0:.1f}%" .format(int((whitePixel / totalPixel) * 100)))

        percent = (whitePixel / totalPixel) * 100

        cv2.putText(frame, "Diff : {0:.1f}%" .format(percent), (10,20), font, 0.5, (0,0,255), 2)

        cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
            (10, frame.shape[0] - 10), font, 0.5, (0, 0, 255), 1)

        if ret:
            if mirror:
                frame = cv2.flip(frame, 1)
            out.write(frame)
        else:
            break

        cv2.imshow('delta', frameDelta)
        cv2.imshow('thresh', thresh)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    currentFrame += 1
cap.release()
out.release()
cv2.destroyAllWindows()