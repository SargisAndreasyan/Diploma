import cv2
import mediapipe as mp

class CompEye:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands()
        self.mpDraw = mp.solutions.drawing_utils

    @staticmethod
    def convert_to_rgb(img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    @staticmethod
    def show_img(title, img):
        cv2.imshow(title, img)

    @staticmethod
    def get_hands(results):
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                yield handLms

    @staticmethod
    def min_time(prev):
        now = cv2.getTickCount()
        if ((now - prev) / cv2.getTickFrequency()) < 2e-05:
            return False
        else:
            return True

    def read_cap(self):
        "success_flag and frame"
        prev = cv2.getTickCount()
        while not self.min_time(prev):
            self.min_time(prev)
        return self.cap.read()

    def hand_detection(self, image_rgb):
        return self.hands.process(image_rgb)

    def start_show(self):
        while True:
            success, img = self.read_cap()
            image_rgb = self.convert_to_rgb(img)
            result = self.hand_detection(image_rgb)
            img = self.hands_drawing(img, result)
            self.show_img('Frame', img)
            if cv2.waitKey(33) == 27:
                break

    def get_cords(self, finger):
        success, img = self.read_cap()
        image_rgb = self.convert_to_rgb(img)
        result = self.hand_detection(image_rgb)
        if result.multi_hand_landmarks:
            for hand in result.multi_hand_landmarks:
                for i, cord in enumerate(hand.landmark):
                    if finger == i:
                        return cord.x, cord.y

    def hands_drawing(self, image, results):
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                self.mpDraw.draw_landmarks(image, handLms, self.mpHands.HAND_CONNECTIONS)
        return image
