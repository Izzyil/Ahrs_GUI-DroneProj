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

clock=pygame.time.Clock()

root = tk.Tk()
root.wm_title("Izzy AHRS")								    
leftSide = Frame(root, width = 1000, height = 1000) 
leftSide.grid(columnspan = 1000, rowspan = 1000) 			
# leftSide.pack(side = LEFT) 									
rightSide = Frame(root, width = 300, height = 1000)	
rightSide.grid(row = 0, column = 1000) 	
# rightSide.pack(side = RIGHT)

os.environ['SDL_WINDOWID'] = str(leftSide.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'

ahrsDisplay = pygame.display.set_mode((1000,1000))
ahrsDisplay.fill(black)
pygame.display.init()
pygame.display.set_caption('Izzy AHRS GUI')
pygame.display.update()

quit = False

def connect():
	lComportStatus.config(text='Connected',foreground="green")
	print("connectiong")

def disconnect():
	lComportStatus.config(text='DisConnected',foreground="red")
	print("disconnecting")

def clearLog():
	AltCanvas.delete("all")
	print("deleting log..\r\n")
	textbox.delete('1.0',END)

rightFrame = Frame(rightSide, width=300, height = 900)
rightFrame.grid(row=0, column=0, padx=0, pady=0)

#########################com frame config
CommFrame = LabelFrame(rightFrame,text='com', width=300, height = 300)
CommFrame.grid(row=0, column=0, padx=5, pady=2,sticky=W+E)

lcomport = Label(CommFrame,width=10,height=2,text="COM Port:")
lcomport.grid(row=0, column=0, padx=0, pady=0)

cbCommPort=ttk.Combobox(CommFrame,width=10)
cbCommPort.grid(row=0, column=1, padx=0, pady=0)
cbCommPort['values']=('COM1','COM2','COM3','COM4','COM5','COM6')

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
ViewFrame = LabelFrame(rightFrame,text='View Setting', width=300, height = 100)
ViewFrame.grid(row=1, column=0, padx=5, pady=2,sticky=W+E)

cbxCamra = Checkbutton(ViewFrame,text='Camera',state=ACTIVE,variable=NONE)
cbxCamra.grid(row=0, column=0, padx=10, pady=2, sticky='w')

chxSetting = Checkbutton(ViewFrame,text='Setting',state=ACTIVE)
chxSetting.grid(row=1, column=0, padx=10, pady=2, sticky='w')

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

###############################################################################


######################consol frame config
ConsleFrame = LabelFrame(rightFrame,text='Console', width=300, height = 600)
ConsleFrame.grid(row=3, column=0, padx=5, pady=2,sticky=W+E)

bClear = Button(ConsleFrame,text="Clear",width=10,command=clearLog)
bClear.grid(row=0, column=0, padx=10, pady=2, sticky='e')

# logLable = Label(ConsleFrame,width=10,height=2,text="Messages..")
# logLable.grid(row=1, column=0, padx=0, pady=0, sticky='w')

textbox = tkscrolledtext.ScrolledText(ConsleFrame, wrap='word', width=40, height=40) 
textbox.grid(row=1, padx=0, pady=0)

###############################################################################

while not quit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True

	pygame.display.update()
	root.update() 
	clock.tick(30)
	
pygame.quit()
quit()
