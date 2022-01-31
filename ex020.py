#cant open it because mp3 file and ogg file are not recognized
import pygame
from pygame import mixer
mixer.init()
mixer.music.load('not.mp3')
mixer.music.play(loops=5)
input('Musica é vida!')