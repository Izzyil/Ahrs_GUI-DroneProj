#ahrs GUI program for embedde drone project
#
#Autor: Izzy
#date: 06\12\17

import pygame
import tkinter as tk
from tkinter import *
import os


white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)

pi = 3.141592653

clock=pygame.time.Clock()

root = Tk()
root.wm_title("Izzy AHRS")								    
leftSide = tk.Frame(root, width = 1200, height = 1000) 		
leftSide.grid(columnspan = (600), rowspan = 500) 			
leftSide.pack(side = LEFT) 									
rightSide = tk.Frame(root, width = 150, height = 900)
rightSide.pack(side = LEFT)

os.environ['SDL_WINDOWID'] = str(leftSide.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'

ahrsDisplay = pygame.display.set_mode((1000,1000))
ahrsDisplay.fill(black)
pygame.display.init()
pygame.display.set_caption('Izzy AHRS GUI')
pygame.display.update()

quit = False

while not quit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True

	pygame.display.update()
	root.update() 
	clock.tick(30)
	
pygame.quit()
quit()
