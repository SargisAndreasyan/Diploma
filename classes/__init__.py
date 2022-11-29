import os
import sys

PROJECT_ROOT = os.path.abspath(
    os.path.dirname(__file__)
)
sys.path.append(PROJECT_ROOT)

from mouse import Mouse
from comp_eye import CompEye
from hand import Hand
