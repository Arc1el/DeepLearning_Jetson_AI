import cv2
import mediapipe as mp
from socket import *
import numpy as np
import time

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('172.20.10.3', 7777))
rps_gesture = {0:'mute', 5:'unmute', 9:'capture', 10:'fix'}


#Define Drawing and Hands
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
flag = "none"
gest_flag = "none"
counter = 0

# Gesture recognition model
file = np.genfromtxt('data/gesture_train.csv', delimiter=',')
angle = file[:,:-1].astype(np.float32)
label = file[:, -1].astype(np.float32)
knn = cv2.ml.KNearest_create()
knn.train(angle, cv2.ml.ROW_SAMPLE, label)

cap = cv2.VideoCapture('nvarguscamerasrc ! video/x-raw(memory:NVMM), width=1280, height=720, format=(string)NV12, framerate=(fraction)20/1 ! nvvidconv ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink', cv2.CAP_GSTREAMER)

with mp_hands.Hands(
    max_num_hands = 1,
    min_detection_confidence = 0.5,
    min_tracking_confidence = 0.5) as hands:
    
    while cap.isOpened():
        success, image = cap.read()
        
        if not success:
            print("can't open video")
            continue
        
        #BGR to RGB (opencv = BGR but mediapipe using RGB)
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        results = hands.process(image)
        
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                #thumb data
                thumb = hand_landmarks.landmark[4]
                #index data
                index = hand_landmarks.landmark[8]
                
                diff = abs(index.x - thumb.x)
                
                #set volume value
                volume = int(diff * 500)
                
                if flag is not "stop":
                    print(volume)
                    clientSock.send(str(volume).zfill(8).encode('utf-8'))
                
                cv2.putText(
                    image, text = "volume : %s" % volume, org=(10,30),
                    fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale = 1,
                    color = 255, thickness = 2
                )
                
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS
                )
                
        if results.multi_hand_landmarks is not None:
            for res in results.multi_hand_landmarks:
                joint = np.zeros((21, 3))
                for j, lm in enumerate(res.landmark):
                    joint[j] = [lm.x, lm.y, lm.z]

                # Compute angles between joints
                v1 = joint[[0,1,2,3,0,5,6,7,0,9,10,11,0,13,14,15,0,17,18,19],:] # Parent joint
                v2 = joint[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],:] # Child joint
                v = v2 - v1 # [20,3]
                # Normalize v
                v = v / np.linalg.norm(v, axis=1)[:, np.newaxis]

                # Get angle using arcos of dot product
                angle = np.arccos(np.einsum('nt,nt->n',
                    v[[0,1,2,4,5,6,8,9,10,12,13,14,16,17,18],:], 
                    v[[1,2,3,5,6,7,9,10,11,13,14,15,17,18,19],:])) # [15,]

                angle = np.degrees(angle) # Convert radian to degree

                # Inference gesture
                data = np.array([angle], dtype=np.float32)
                ret, result, neighbours, dist = knn.findNearest(data, 3)
                idx = int(result[0][0])

                # Draw gesture result
                if idx in rps_gesture.keys():
                    
                    print("idx : ", idx)
                    if idx == 0:
                        print("mute")
                        clientSock.send(str(1111).encode('utf-8'))
                        
                    elif idx == 5:
                        print("unmute")
                        clientSock.send(str(2222).encode('utf-8'))
                        
                    elif idx == 9 :
                        print("capture")
                        clientSock.send(str(3333).encode('utf-8'))

                    elif idx == 10 :
                        print("fix")
                        clientSock.send(str(4444).encode('utf-8'))

                    cv2.putText(image, text=rps_gesture[idx].upper(), org=(int(res.landmark[0].x * image.shape[1]), int(res.landmark[0].y * image.shape[0] + 20)), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(255, 255, 255), thickness=2)

                # Other gestures
                # cv2.putText(img, text=gesture[idx].upper(), org=(int(res.landmark[0].x * img.shape[1]), int(res.landmark[0].y * img.shape[0] + 20)), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(255, 255, 255), thickness=2)

                mp_drawing.draw_landmarks(image, res, mp_hands.HAND_CONNECTIONS)
                
                
        cv2.imshow('image', image)
        if cv2.waitKey(1) == ord('q'):
            break
        
    cap.release()