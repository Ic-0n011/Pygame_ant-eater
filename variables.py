"""все внутреигровые переменные"""
import os

curent_dir = os.path.dirname(__file__)
assert_dir = os.path.join(curent_dir, 'assert')

ROWS = 7
COLS = 11
MIN_ANTHILLS = 1
MAX_ANTHILLS = 4
IMG_CELL = (30, 30, 30)
BUTTONS = ['enter', 'right', 'left', 'up', 'down', 'esc']
FONT = os.path.join(assert_dir, 'font.ttf')
