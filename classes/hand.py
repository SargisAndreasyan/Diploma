import cv2
import threading
from comp_eye import CompEye
import mediapipe as mp


class Hand(CompEye):
    def __init__(self):
        super(Hand, self).__init__()
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands()
        self.mpDraw = mp.solutions.drawing_utils

    @staticmethod
    def get_hands(results):
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                yield handLms

    def _hand_detection(self, image_rgb):
        return self.hands.process(image_rgb)

    def start_show(self):
        def func():
            while True:
                success, img = self.read_cap()
                image_rgb = self.convert_to_rgb(img)
                result = self._hand_detection(image_rgb)
                img = self.hands_drawing(img, result)
                self.show_img('Frame', img)
                if cv2.waitKey(33) == 27:
                    break

        t1 = threading.Thread(target=func)
        t1.start()

    def get_cords(self, finger):
        success, img = self.read_cap()
        image_rgb = self.convert_to_rgb(img)
        result = self._hand_detection(image_rgb)
        if result.multi_hand_landmarks:
            for hand in result.multi_hand_landmarks:
                for i, cord in enumerate(hand.landmark):
                    if finger == i:
                        return round(cord.x,3), round(cord.y,3)

    def hands_drawing(self, image, results):
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                self.mpDraw.draw_landmarks(image, handLms, self.mpHands.HAND_CONNECTIONS)
        return image
