import pygame
from threading import Thread


def play_music():
    pygame.init()
    pygame.mixer.pre_init(frequency=44100, size=2, channels=1) 
    sound = pygame.mixer.Sound('melody.wav')
    while True:
        sound.play()


def start_muzic():
    Thread(target=play_music).start()

start_muzic()