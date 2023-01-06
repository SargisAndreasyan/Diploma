import cv2
import mediapipe as mp


class CompEye:
    def __init__(self):
        self.cv = cv2
        self.cap = cv2.VideoCapture(0)

    @staticmethod
    def convert_to_rgb(img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    @staticmethod
    def show_img(title, img):
        cv2.imshow(title, img)

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

    def start(self):
        while True:
            success, img = self.read_cap()
            yield img

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()
