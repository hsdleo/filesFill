import sys
import pygame
import pygame.camera
import os
import RPi.GPIO as GPIO
import time
from time import sleep
# Pin Definitons:
sensorPin = 23 # Broadcom pin 23 (P1 pin 16)

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(sensorPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Button pin set as input w/ pull-up

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()
pygame.camera.init()

#create fullscreen display 640x480
screen = pygame.display.set_mode((640,480),0)

#find, open and start low-res camera
cam_list = pygame.camera.list_cameras()
webcam = pygame.camera.Camera(cam_list[0],(640,480))
webcam.start()

while True:
    #grab image, scale and blit to screen
    imagen = webcam.get_image()
	#imagem2 = pygame.image.load(os.path.abspath("cat.gif"))
	background = pygame.Surface(screen.get_size())
    imagen = pygame.transform.scale(imagen,(640,480))
	if GPIO.input(sensorPin): # button is released
		imagem = webcam.get_image()
    else: # button is pressed:
		imagem = pygame.image.load(os.path.abspath("cat.gif"))
    screen.blit(imagen,(0,0))
    #draw all updates to display
    pygame.display.update()
	sleep(0.1)


    # check for quit events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
       		 webcam.stop()
       		 pygame.quit()
       		 sys.exit()
