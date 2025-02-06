import sys
import os

sys.path.append(os.getcwd())

from .calculator import *


__all__ = ["area_rectangle", "area_triangle", "area_circle"]
