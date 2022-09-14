import cv2
import mediapipe as mp


def handsFinder(image, draw=True):
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(imageRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:

            if draw:
                mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)
    return image


cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    imageRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(imageRGB)
    cv2.imshow('img', handsFinder(imageRGB))

    if cv2.waitKey(33) == 27:
        break
