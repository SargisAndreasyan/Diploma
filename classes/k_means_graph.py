from time import sleep, time

import matplotlib.pyplot as plt

from hand import Hand


def graph3d(cord_x, cord_y, timer):
    ax = plt.figure().add_subplot(projection='3d')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xlabel('X')
    ax.set_ylabel('T')
    ax.set_zlabel('Y')
    ax.plot(cord_x, timer, cord_y)
    return ax


def graph2d(cord_x, cord_y):
    ax = plt.figure().add_subplot()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    return ax


if __name__ == '__main__':
    h1 = Hand()
    h1.start_show()
    while True:
        if h1.get_cords(8):
            cords_x = []
            cords_y = []
            timing = []
            start_time = time()
            while h1.get_cords(8):

                start = time()
                finger_cords = h1.get_cords(8)
                cords_x.append(finger_cords[0] if finger_cords is not None else cords_x[-1])
                cords_y.append(finger_cords[1] if finger_cords is not None else cords_y[-1])
                timing.append(time()-start_time)
            plt.subplot(3,1,1)
            plt.title("X Y")
            plt.plot(cords_x,cords_y)
            plt.subplot(3, 1, 2)
            plt.title("X T")
            plt.plot(cords_x,timing)
            plt.subplot(3, 1, 3)
            plt.title("Y T")
            plt.plot(cords_y,timing)
            graph3d(cords_x,cords_y,timing)
            plt.show()
            cords_x, cords_y, timing = [], [], []


