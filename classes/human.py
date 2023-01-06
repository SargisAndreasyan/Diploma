import cv2
import imutils

from comp_eye import CompEye


class Human(CompEye):
    def __init__(self):
        super(Human, self).__init__()
        self.hog = cv2.HOGDescriptor()
        self.hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    def show(self):
        while self.cap.isOpened():
            # Reading the video stream
            success, image = self.read_cap()
            if success:
                image = imutils.resize(image,
                                       width=min(400, image.shape[1]))
                (regions, _) = self.hog.detectMultiScale(image,
                                                         winStride=(4, 4),
                                                         padding=(4, 4),
                                                         scale=1.05)
                for (x, y, w, h) in regions:
                    cv2.rectangle(image, (x, y),
                                  (x + w, y + h),
                                  (0, 0, 255), 2)
                cv2.imshow("Image", image)
                if cv2.waitKey(33) == 27:
                    break
            else:
                self.release()
                break
