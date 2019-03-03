import pygame
import time
from picamera import PiCamera
from time import sleep   

def capture(fN):
    camera.capture(fN)


camera = PiCamera()
In=1
pygame.init()
w = 640
h = 480
size=(w,h)
screen = pygame.display.set_mode(size) 
#c = pygame.time.Clock() # create a clock object for timing

while In == 1:
    filename = "/home/pi/Desktop/" + str(In)+".jpg" # ensure filename is correct
    capture(filename) 
    img = pygame.image.load(filename) 
    screen.blit(img,(0,0))
    pygame.display.flip() # update the display
    #c.tick(3) # only three images per second
    #sleep(0.05)

    




#camera.resolution = (2592, 1944)
#camera.framerate = 15
#camera.start_preview()
#sleep(5)
#camera.capture('/home/pi/Desktop/max.jpg')
#camera.stop_preview()
