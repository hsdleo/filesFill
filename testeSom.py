import pygame
from time import sleep
#pygame.mixer.init(44100, -16, 2, 2048)
pygame.init()
pygame.mixer.init()
s1 = pygame.mixer.Sound("efeito2.wav")
s1.play()
sleep(2)
