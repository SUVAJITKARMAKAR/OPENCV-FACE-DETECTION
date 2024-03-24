import cv2 as cv
import face_recognition
import face_recognition as face
import pickle
import os

# IMPORTING THE STUDENT IMAGES
folderPath = 'Images'
PathList = os.listdir(folderPath)
imageList = []
studentIds = []

for path in PathList:
    imageList.append(cv.imread(os.path.join(folderPath, path)))
    studentIds.append(os.path.splitext(path)[0])


# FUNCTION >> FACE ENCODING SYSTEM FUNCTION
def findEncodings(imageList):
    encodeList = []
    for image in imageList:
        image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(image)[0]
        encodeList.append(encode)

    return encodeList


# CALLING THE ENCODING FUNCTION TO ENCODE THE IMAGES FROM THE IMAGE LIST
print("ENCODING IN PROGRESS")
encodeListKnown = findEncodings(imageList)
encodingListKnownWithIds = [encodeListKnown, studentIds]
print("ENCODING COMPLETED")

# GENERATING THE PICKLE FILE
file = open("EncodedFile.p", 'wb')
pickle.dump(encodingListKnownWithIds, file)
file.close()
print("FILE IS SAVED!")
