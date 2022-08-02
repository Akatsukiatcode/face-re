from operator import length_hint
from unicodedata import name
from cv2 import VideoCapture
import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime
import os

VideoCapture = cv2.VideoCapture(0)
#photos = (amarsir.jpg , bhudevsir.jpg , rahul.jpg , rakeshsir.jpg)

amarsir_image =face_recognition.load_image_file("photos/amarsir.jpg")
amarsir_encodings = face_recognition.face_encodings(amarsir_image)[0]
if len(amarsir_encodings) > 0:
        unknown_face_encoding = amarsir_encodings[0]

#obama_image = face_recognition.load_image_file("photos/obama.jpg")
#obama_encodings = face_recognition.face_encodings(obama_image)[0]

rahul_image = face_recognition.load_image_file("photos/rahul.jpg")
rahul_encodings = face_recognition.face_encodings(rahul_image)[0]
if len(rahul_encodings) > 0:
        unknown_face_encoding = rahul_encodings[0]

#rakeshsir_image = face_recognition.load_image_file("photos/rakeshsir.jpg")
#rakeshsir_encodings = face_recognition.face_encodings(rakeshsir_image)[0]

known_face_encodings = [
    amarsir_encodings , #obama_encodings ,
    rahul_encodings , #rakeshsir_encodings
]

known_faces_name = [
    "amarsir", "obama", "rahul", "rakeshsir"
]

students = known_faces_name.copy()

face_locations = []
known_face_encodings = []
face_names = []
s=True

now = datetime.now()
current_date = now.strftime("%Y-%m-%d")


f=open(current_date+'.csv','w+',newline = '')
lnwriter = csv.writer(f)

while True:
    _,frame = VideoCapture.read()
    small_frame= cv2.resize(frame , (0,0),fx=0.25, fy=0.25)
    rgb_small_frame = cv2.resize [::,::-1]
    if s:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings =face_recognition.face_encodings( rgb_small_frame , face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings , face_encoding)
            name = ""
            face_distance = face_recognition.face_distance(known_face_encodings,face_encoding)
            best_match_index =np.argmin(face_distance)
            if matches[best_match_index]:
                name=known_faces_name[best_match_index]

                face_names.append(name)
                if name in known_face_encodings:
                    if name in students:
                        students.remove(name)
                        print(students)
                        current_time = now.strftime("%H-%M-$S")
                        lnwriter.writerow([name.current_time])

                cv2.imshow("attendence system" , frame)
                if cv2.waitKey(1) & 0xFF ==ord('q'):
                    break

                VideoCapture.release()
                cv2.destroyAllWindows()
                f.close()       

