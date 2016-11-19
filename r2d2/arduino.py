import sys, serial, time
# import the necessary packages
from pyimagesearch.facedetector import FaceDetector
from pyimagesearch import imutils
import speech_recognition as sr
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
    print(Arduino.readline().decode())

#### connect
Arduino = connectArduino("/dev/cu.usbmodem1421")
# construct the face detector
# fd = FaceDetector("./cascades/haarcascade_frontalface_default.xml")
# camera = cv2.VideoCapture(0)
# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
try:
    command = r.recognize_google(audio);
    print(command);
    if(command == 'hello'):
        messageArduino("b")
    elif(command == 'listen'):
        messageArduino(command)

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
