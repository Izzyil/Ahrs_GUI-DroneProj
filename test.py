import pygame
from tkinter import *
from tkinter import ttk
import tkinter as tk
import math

import tkinter.scrolledtext as tkscrolledtext
from tkinter import filedialog
import serial_rx_tx
import threading
import _thread
import time
import webbrowser
from tkinter import messagebox
import os

black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)

pi = 3.141592653
defualt_pos = 0,0
ImgBack = 0
ImgPitch = 1
ImgHeading = 2 
ImgBack2 = 3
ImgLay = 4
ImgCamera = 5
ImgImnfo = 6
ImgWarning = 7


screen = pygame.display.set_mode((1000,1000))
pygame.display.update()

class Dispay:
	def __init__(self):
		self.Img[ImgBack].show = True
		self.Img[ImgPitch].show = True
		self.Img[ImgHeading].show = True
		self.Img[ImgBack2].show = True
		self.Img[ImgLay].show = True
		self.Img[ImgCamera].show = True
		self.Img[ImgImnfo].show = True
		self.Img[ImgWarning].show = True
		self.Img[ImgBack].img = 'bak1.png'
		self.Img[ImgPitch].img = 'pitchScale.png'
		self.Img[ImgHeading].img = 'headingFrame.png'
		self.Img[ImgBack2].img = 'bak1.png'
		self.Img[ImgLay].img = 'ladyLegs.png'
		self.Img[ImgCamera].img = 'cameraFeed.png'
		self.Img[ImgImnfo].img = 'equipInfo.png'
		self.Img[ImgWarning].img = 'warning.png'
		
		for i in self.Img
			self.Img[i].display = pygame.image.load(self.Img[i])
		for i in self.Img
			self.Img[i].pos = defualt_pos
	
	def darw(self):
		for i in self.Img
			if i.show == True:
				blit(self.Img[i].img,self.Img[i].pos)
		
# clock =pygame.time.Clock()

dispay = Dispay()

# while True:
	# clock.tick(60)
	# for event in pygame.event.get():
			# if event.type == pygame.KEYDOWN:
				# if event.key == pygame.K_RIGHT:
					# degree = -1
				# if event.key == pygame.K_LEFT:
					# degree = 1
				# if event.key == pygame.K_DOWN:
					# up =up+-3
				# if event.key == pygame.K_UP:
					# up = 3
			# if event.type == pygame.KEYUP:
				# if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					# degree = 0
				# if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					# up = 0
	
	
	
# root = tk.Tk()
# root.wm_title("Izzy AHRS")								    
