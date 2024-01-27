"""все внутреигровые переменные"""
import os

curent_dir = os.path.dirname(__file__)
assert_dir = os.path.join(curent_dir, 'assert')

ROWS = 7
COLS = 11
MIN_ANTHILLS = 1
MAX_ANTHILLS = 4
IMG_PLAYER = (255, 255, 255)  # os.path.join(assert_dir, 'ant-eater.ttf')
IMG_ANT = (30, 255, 30)  # os.path.join(assert_dir, 'ant.ttf')
IMG_ANTHILL = (255, 30, 30)  # os.path.join(assert_dir, 'anthill.ttf')
IMG_CELL = (30, 30, 30)
BUTTONS = ['enter', 'right', 'left', 'up', 'down', 'esc']
FONT = os.path.join(assert_dir, 'font.ttf')
