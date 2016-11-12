import sys, serial, time
# import the necessary packages
from pyimagesearch.facedetector import FaceDetector
from pyimagesearch import imutils
import cv2


def detectFace(camera, fd):
    (grabbed, frame) = camera.read()
    frame = imutils.resize(frame, width = 300)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faceRects = fd.detect(gray, scaleFactor = 1.1, minNeighbors = 5,
		minSize = (30, 30))
    # frameClone = frame.copy()
    #
    # for (fX, fY, fW, fH) in faceRects:
    #     cv2.rectangle(frameClone, (fX, fY), (fX + fW, fY + fH), (0, 255, 0), 2)
    #
    # cv2.imshow("Face", frameClone)

    return len(faceRects)

def connectArduino (port):
    serArduino = serial.Serial(port, 9600)
    serArduino.close()
    serArduino.open()

    if not serArduino.isOpen():
        print ('Error: Could not connect to Arduino')
        sys.exit()
    else:
        print ('Arduino is connected.')
        return serArduino


def messageArduino(message):
    Arduino.write((message).encode())
    print (Arduino.readline().decode())

commands = {"scale": "a",
            "r2D2": "b",
            "closeEncounters": "c",
            "ariel": "d",
            "laugh2": "e",
            "squeak": "f",
            "waka": "g",
            "catcall": "h",
            "ohhh": "i",
            "uhoh": "j",
            "laugh": "k"}

#### connect
Arduino = connectArduino("/dev/cu.usbmodem1411")
# construct the face detector
fd = FaceDetector("./cascades/haarcascade_frontalface_default.xml")
camera = cv2.VideoCapture(0)

while True:
    numberOfFace = detectFace(camera, fd);
    print(numberOfFace);
    if(numberOfFace == 1):
        messageArduino(commands["laugh"])
    elif(numberOfFace == 2):
        messageArduino(commands["closeEncounters"])
    # messageArduino(commands["laugh"])
    time.sleep(1)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
