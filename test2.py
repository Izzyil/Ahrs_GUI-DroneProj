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

pygame.init()

black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)

center = (500,500)
defualt_pos = 0,0
head_pos = (500,330)
info_pos = (610, 710)
scale_pos =(0,500)
out_pos = (1001,1001)
bak_pos = (-500,-500)

pi = 3.141592653
ImgHorizon 	  = 0
ImgBase		  = 1
ImgPitch      = 2
ImgHeadBak    = 3 
ImgHeading    = 4
ImgLayer      = 5
ImgCamera     = 6
ImgImnfo      = 7
ImgWarning    = 8
ImgAltScale   = 9
InfoData 	  = 10
numOfLayers   = 11


screen = pygame.display.set_mode((1000,1000))
screen.fill(black)

show = [True, True, True, True, True, True, True, True, True, True, True]
position = [bak_pos, defualt_pos, defualt_pos, defualt_pos, defualt_pos, defualt_pos, defualt_pos, defualt_pos, defualt_pos, defualt_pos, defualt_pos]
imgae = ['bak2000.png', 'base.png', 'pitch.png', 'head2.png', 'head.png','lady.png', 'cameraFeed.png', 'equipInfo.png', 'warning.png', 'altScale1.png', 'altScale1.png']

# font = pygame.font.SysFont(None, 25)

def rot_center(image):
		size=image.get_size() #Store size
		hSize=[n/2 for n in size] #Half the size
		pos=[center[0]-hSize[0],center[1]-hSize[1]]  #Substract half the size
		return pos

class Dispay:
	def __init__(self, screen, position, image):
		self.screen = screen
		self.alt = 0
		self.pitch = 0
		self.roll = 0
		self.heading = 0
		self.show = []
		self.pos = []
		self.img = []
		self.obj = []
		self.defObj = []
		self.rect =[]

		for i in range (numOfLayers):
			self.show.append(show[i])
			self.pos.append(position[i])
			self.img.append(image[i])
			self.obj.append(pygame.image.load(image[i]))
			self.defObj.append(pygame.image.load(image[i]))
			self.rect.append(self.obj[i].get_rect(topleft=self.pos[i]))
			
	def draw(self):
		for i in range(numOfLayers):
			if self.show[i] == True:
				self.screen.blit(self.obj[i], self.pos[i])
			else:
				self.screen.blit(self.obj[i], out_pos)
	def setShow(self, img, show):
		self.show[img] = show
		print("setting show for %s to %s" %(self.img[img], show))

	def setPos(self, img, pos):
		self.pos[img] = pos

	def getPos(self, img):
		return self.pos[img]

	def setObj(self, img,obj):
		self.obj[img] = obj

	def updateHeading(self):
		# head = pygame.font.Font('Roboto-Bold.ttf', 30)
		self.obj[ImgHeading] = font.render(str(self.heading), True, white)
		self.rect[ImgHeading] = self.obj[ImgHeading].get_rect()
		self.rect[ImgHeading].center = (head_pos)
		self.pos[ImgHeading] = self.rect[ImgHeading]

	def updatePitch(self):
		self.rect[ImgPitch] = self.obj[ImgPitch].get_rect(topleft= self.pos[ImgPitch])
		img = pygame.transform.rotate(self.defObj[ImgPitch], self.roll)
		self.rect[ImgPitch] = img.get_rect(center=self.rect[ImgPitch].center)
		x, y = self.rect[ImgPitch].width/2-150, self.rect[ImgPitch].height/2-150+self.pitch
		self.obj[ImgPitch] = img.subsurface((x, y, 300, 300))
		self.pos[ImgPitch]= 350,350

	def updateRoll(self):
		self.obj[ImgHorizon]= pygame.transform.rotate(self.defObj[ImgHorizon], self.roll)
		change=rot_center(self.obj[ImgHorizon])
		change[1]+=self.alt
		self.pos[ImgHorizon]= change
	
	def updateInfo(self):
		info = pygame.font.Font('Roboto-Regular.ttf', 30)
		data= 'Pitch:'+str(self.pitch)+'\nRoll:'+str(self.roll)+'\nHeading:'+str(self.heading)
		self.obj[InfoData] = info.render(data, True, white)
		self.rect[InfoData] = self.obj[InfoData].get_rect(center =center)
		self.rect[InfoData].center = (info_pos)
		self.pos[InfoData] = info_pos

gameExit = False
up = 0
degree = 0
p = 0
h = 0

font = pygame.font.SysFont('Roboto-Bold.ttf', 50)
display = Dispay(screen, position, imgae)
clock = pygame.time.Clock()

while not gameExit:
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True		
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_p:
					print(display.img[ImgPitch])
				if event.key == pygame.K_w:
					p = -2
				if event.key == pygame.K_s:
					p = 2
				if event.key == pygame.K_d:
					h = -1
				if event.key == pygame.K_a:
					h = 1
				if event.key == pygame.K_RIGHT:
					degree = -0.5
				if event.key == pygame.K_LEFT:
					degree = 0.5
				if event.key == pygame.K_DOWN:
					up = -2
				if event.key == pygame.K_UP:
					up = 2
			
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					degree = 0
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					up = 0
				if event.key == pygame.K_w or event.key == pygame.K_s:
					p = 0
				if event.key == pygame.K_a or event.key == pygame.K_d:
					h = 0

	display.roll += degree
	display.alt += up
	display.pitch +=p
	display.heading +=h

	display.updateRoll()
	display.updatePitch()
	display.updateHeading()
	display.updateInfo()

	display.draw()

	pygame.display.flip()
	clock.tick(30)							    

pygame.quit()
quit()