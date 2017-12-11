#ahrs GUI program for embedde drone project
#
#Autor: Izzy
#date: 06\12\17

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

serialPort = serial_rx_tx.SerialPort()
print_lock = threading.Lock()


root = tk.Tk()
root.wm_title("Izzy AHRS")								    
leftSide = Frame(root, width = 1000, height = 1000) 
leftSide.grid(columnspan = 1000, rowspan = 1000) 							
rightSide = Frame(root, width = 300, height = 1000)	
rightSide.grid(row = 0, column = 1000) 	

os.environ['SDL_WINDOWID'] = str(leftSide.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'

ahrsDisplay = pygame.display.set_mode((1000,1000))
ahrsDisplay.fill(black)
pygame.display.init()

quit = False
up=0
upUpdate=0
degree=0
dgreeUpdate=0
center=(500,500)
begin=(0,0)
warningDis= tk.IntVar()
infoDis= tk.IntVar()
cameraDis= tk.IntVar()

		
###############################################################	
def showTkinter():
	global quit
	def OnReceiveSerialData(message):
		buffer = message.decode("utf-8")
		textbox.insert('1.0', buffer)
		
	serialPort.RegisterReceiveCallback(OnReceiveSerialData)
	
	def connect():
		comPort=cbCommPort.get()
		baudrate=lPortRate.get()
		serialPort.Open(comPort, baudrate)
		if (serialPort.IsOpen() == True):
			print("Connecting..\r\n")
			lComportStatus.config(text='Connected',foreground="green")
			textbox.insert('1.0', "Connected..\r\n")
		else:
			textbox.insert('1.0', "Can not connect (no such port)\r\n")
			print("Can not connect\r\n")

	def disconnect():
		if (serialPort.IsOpen() == True):
			serialPort.Close()
			print("DisConnecting..\r\n")
			textbox.insert('1.0', "Disconnected..\r\n")
			lComportStatus.config(text='DisConnected',foreground="red")
		else:
			print("Error: no such port")

	def clearLog():
		print("deleting log..\r\n")
		textbox.delete('1.0',END)
	
	
	rightFrame = Frame(rightSide, width=300, height = 900)
	rightFrame.grid(row=0, column=0, padx=0, pady=0)
	ConsleFrame = LabelFrame(rightFrame,text='Console', width=300, height = 600)
	ConsleFrame.grid(row=3, column=0, padx=5, pady=2,sticky=W+E)
	textbox = tkscrolledtext.ScrolledText(ConsleFrame, wrap='word', width=40, height=40) 
	textbox.grid(row=1, padx=0, pady=0)
	
	#########################com frame config
	CommFrame = LabelFrame(rightFrame,text='Com', width=300, height = 300)
	CommFrame.grid(row=0, column=0, padx=5, pady=2,sticky=W+E)

	lcomport = Label(CommFrame,width=10,height=2,text="COM Port:")
	lcomport.grid(row=0, column=0, padx=0, pady=0)

	cbCommPort=ttk.Combobox(CommFrame,width=10)
	cbCommPort.grid(row=0, column=1, padx=0, pady=0)
	cbCommPort['values']=('COM1','COM2','COM3','COM4','COM5','COM6','COM7','COM8')

	lPortRate = Label(CommFrame,width=10,height=2,text="Baudrate:")
	lPortRate.grid(row=1, column=0, padx=0, pady=0)
	
	lPortRate=Entry(CommFrame,width=10)
	lPortRate.grid(row=1, column=1, padx=10, pady=2)
	lPortRate.insert(END,"9600")

	bConnect = Button(CommFrame,text="Connect",width=10,command=connect)
	bConnect.grid(row=2, column=0, padx=10, pady=2)

	bDisconnect = Button(CommFrame,text="Disconnect",width=10,command=disconnect)
	bDisconnect.grid(row=2, column=1, padx=10, pady=2)

	lComportStatus = Label(CommFrame,width=10,height=2,text="DisConnected",foreground="red")
	lComportStatus.grid(row=2, column=2, padx=10, pady=2)

	###############################################################################

	######################view frame config 
	ViewFrame = LabelFrame(rightFrame,text='View Info', width=300, height = 100)
	ViewFrame.grid(row=1, column=0, padx=5, pady=2,sticky=W+E)
	
	cbxCamra = Checkbutton(ViewFrame,text='Camera',variable=cameraDis,onvalue=1,offvalue=0)
	cbxCamra.grid(row=0, column=0, padx=10, pady=2, sticky='w')

	chxInfo = Checkbutton(ViewFrame,text='Info',variable=infoDis,onvalue=1,offvalue=0)
	chxInfo.grid(row=0, column=1, padx=10, pady=2, sticky='e')

	chxWornings = Checkbutton(ViewFrame,text='Warnings',variable=warningDis,onvalue=1,offvalue=0)
	chxWornings.grid(row=1, column=0, padx=10, pady=2, sticky='w')

	###############################################################################
	
	######################camera config 
	viewFrame = LabelFrame(rightFrame,text='Camera Setting', width=300, height = 200)
	viewFrame.grid(row=2, column=0, padx=5, pady=2,sticky=W+E)

	lZoom= Label(viewFrame,width=10,height=2,text="ZOOM:")
	lZoom.grid(row=0, column=0, padx=0, pady=0)

	cbZoom=ttk.Combobox(viewFrame,width=10)
	cbZoom.grid(row=0, column=1, padx=0, pady=0)
	cbZoom['values']=('0X1','0X2','0X4','0X8(D)')

	lRes= Label(viewFrame,width=10,height=2,text="ZOOM:")
	lRes.grid(row=1, column=0, padx=0, pady=0)

	cbRes=ttk.Combobox(viewFrame,width=10)
	cbRes.grid(row=1, column=1, padx=0, pady=0)
	cbRes['values']=('680x480','1024x720','1920x1080','2K')

	bClear = Button(ConsleFrame,text="Clear",width=10,command=clearLog)
	bClear.grid(row=0, column=0, padx=10, pady=2, sticky='e')	
	
	while not quit:
		pass
		
	###############################################################################

def showPygame():
	global up	
	global degree
	global buffer
	
	clock=pygame.time.Clock()
	def rot_center(image):
		size=image.get_size() #Store size
		hSize=[n/2 for n in size] #Half the size
		pos=[center[0]-hSize[0],center[1]-hSize[1]]  #Substract half the size
		return pos
	def draw(img, pos):
		ahrsDisplay.blit(img,pos)

	def drawHorizon():	
		global dgreeUpdate
		global upUpdate
		global change
		global up	
		global degree
	
		dgreeUpdate +=degree
		upUpdate +=up
		horizonUpdtae= pygame.transform.rotate(horizonFrame, dgreeUpdate)
		change=rot_center(horizonUpdtae)
		change[1]+=upUpdate
		draw(horizonUpdtae,change)

	def drawCamera():
		if cameraDis.get():
			draw(cameraFrame,begin)
		else:
			dpos = (1001,1001)
			draw(cameraFrame,dpos)
	def drawWarning():
		if warningDis.get():
			draw(warningFrame,begin)
		else:
			dpos = (1001,1001)
			draw(warningFrame,dpos)

	def drawInfo():
		if infoDis.get():
			draw(infoFrame,begin)
		else:
			dpos = (1001,1001)
			draw(infoFrame,dpos)
	
	global quit
	horizonFrame = pygame.image.load('horizon.png')
	layerFrame = pygame.image.load('base.png')
	pitchScaleFrame = pygame.image.load('pitchScale.png')
	ladyFrame = pygame.image.load('ladyLegs.png')
	headingFrame = pygame.image.load('headingFrame.png')
	cameraFrame = pygame.image.load('cameraFeed.png')	
	infoFrame = pygame.image.load('equipInfo.png')
	warningFrame = pygame.image.load('warning.png')
	
	while not quit:	
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					degree = -1
				if event.key == pygame.K_LEFT:
					degree = 1
				if event.key == pygame.K_DOWN:
					up =up+-3
				if event.key == pygame.K_UP:
					up = 3
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					degree = 0
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					up = 0
				
		drawHorizon()
		draw(layerFrame,begin)
		draw(pitchScaleFrame,begin)
		draw(ladyFrame,begin)
		draw(headingFrame,begin)
		drawCamera()
		drawInfo()
		drawWarning()
		
		pygame.display.update()
		clock.tick(30)


	
t_tkinter=threading.Thread(target=showTkinter)
t_tkinter.deamon=True
t_tkinter.start()
t_pygame=threading.Thread(target=showPygame)
t_pygame.deamon=True
t_pygame.start()

pygame.display.update()

root.mainloop()
