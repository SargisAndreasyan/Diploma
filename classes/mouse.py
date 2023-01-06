from comp_eye import CompEye
import pyautogui as pg

class Mouse(CompEye):
    def __init__(self):
        CompEye.__init__(self)
        pg.FAILSAFE = False
        self.width, self.height = pg.size()

    def show(self):
        while True:
            cords = self.get_cords(8)
            if cords is not None:
                x, y = cords
                x = 1 - x
                pg.moveTo(x * self.width, y * self.height)
