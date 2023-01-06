import os
import sys

PROJECT_ROOT = os.path.abspath(
    os.path.dirname(__file__)
)
sys.path.append(PROJECT_ROOT)

from classes import Human

if __name__ == '__main__':
    human = Human()
    human.show()
