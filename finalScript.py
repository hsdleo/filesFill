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
pygame.mixer.init()

som1 = pygame.mixer.Sound("efeito4.wav")
som2 = pygame.mixer.Sound("efeito3.wav")
#create fullscreen display 640x480
screen = pygame.display.set_mode((1024,600),0)

#find, open and start low-res camera
cam_list = pygame.camera.list_cameras()
webcam = pygame.camera.Camera(cam_list[0],(1024,600))
webcam.start()
cameraAberta = False
tocarSom = False
flagSom = True
tocarSom2 = True
flagSom2 = True
while True:
	
	if(cameraAberta):
		tocarSom = True
		flagSom2 = True
		if(flagSom and tocarSom):
			som1.play()
			flagSom = False
			sleep(1)
    	imagen = webcam.get_image()
    else:
		flagSom = True
        tocarSom2 = True
        if(flagSom2 and tocarSom2):
			som2.play()
			sleep(1)
			flagSom2 = False
		imagen = pygame.image.load(os.path.abspath("logo3.png"))
    imagen = pygame.transform.scale(imagen,(1024,600))
    if GPIO.input(sensorPin):
		cameraAberta  = True
	else:
		cameraAberta = False
	screen.blit(imagen,(0,0))
    #draw all updates to display
    pygame.display.update()
	#sleep(0.1)

    # check for quit events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
       		 webcam.stop()
       		 pygame.quit()
       		 sys.exit()
