# OPEN CV PROGRAMMING
# INTEL ONEAPI
# SUVAJIT KARMAKAR


# PROJECT IDEA >> To build an openCV application that would automatically detect face and mark attendance for their respective details.
# PROJECT DEPENDENCIES >>
# CODE IDEAS >>
# CODE IMPLEMENTATION >>
# PROJECT TARGET >>


# PROJECT IMPORT MODULES IN THE WORK SPACE
import cv2 as cv
import cvzone as zone
import os
import pickle
import face_recognition
import numpy as num

# BACKGROUND DIMENSION >> 1280 x 480
# WEBCAM DIMENSION >>
# SETTING THE CAMERA CAPTURE VALUES
capture = cv.VideoCapture(0)

capture.set(3, 640)
capture.set(4, 480)
capture.set(cv.CAP_PROP_FPS, 90)

# SETTING THE BACKGROUND AND INTEGRATING WITH THE VIDEO CAPTURE
imageBackground = cv.imread('Resources/BACKGROUND.png')

# STORING THE MODES IN A LIST USING LOOP
folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imageModeList = []

for path in modePathList:
    imageModeList.append(cv.imread(os.path.join(folderModePath, path)))



# LOADING THE ENCODED FILES
print("LOADING ENCODED FILES")
file = open('EncodedFile.p', 'rb')
encodeListKnownWithIds = pickle.load(file)
file.close()

encodeListKnown, studentIds = encodeListKnownWithIds
# print(studentIds)
print("ENCODED FILE SUCCESSFULLY LOADED!")

while True:
    success, image = capture.read()

    # SCALING THE IMAGE
    imageSmall = cv.resize(image, (0, 0), None, 0.25, 0.25)
    imageSmall = cv.cvtColor(imageSmall, cv.COLOR_BGR2RGB)

    # COMPARING THE CURRENT FACE ON FRAME TO THAT OF THE ENCODED VALUES IN ORDER TO VALIDATE
    faceInCurrentFrame = face_recognition.face_locations(imageSmall)
    encodeCurrentFrame = face_recognition.face_encodings(imageSmall, faceInCurrentFrame)

    # OVERLAYING THE IMAGE BACKGROUND AND THE WEBCAM
    imageBackground[125:125+480, 90:90+640] = image
    imageBackground[85:85+550, 861:861+350] = imageModeList[4]

    # LOOPING THROUGH THE ENCODINGS AND COMPARING REAL TIME VALUES
    for encodeFace, faceLoc in zip(encodeCurrentFrame, faceInCurrentFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDistance = face_recognition.face_distance(encodeListKnown, encodeFace)
        matchIndex = num.argmin(faceDistance)

        # MATCHING THE FACE DETECTION
        if matches[matchIndex]:
            print("KNOWN FACE IS DETECTED!")
            print(studentIds[matchIndex])

            # LOCATING THE FACE CO-ORDINATES IN ORDER TO TRACK THE FACE IN REAL TIME
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*3, x2*4, y2*3, x1*4
            boundingBox = 90+x1, 160+y1, x2-x1, y2-y1
            imageBackground = zone.cornerRect(imageBackground, boundingBox, rt=0)

            
            
    # cv.imshow("WEBCAM", image)
    cv.imshow("FACE ATTENDANCE", imageBackground)
    cv.waitKey(1)
