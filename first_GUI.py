# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 14:39:41 2020

@author: Henry
"""

import tkinter, webbrowser, sys


#Creates the GUI window in the computer memory
window = tkinter.Tk() 

#Set the naem of the window
window.title("Map Search")

#Generates labels in 'window' with text saying "Hello World!"
label = tkinter.Label(window,text = "Enter the place you want to find on google maps!", font=('Arial',11))

#Creates a button (bt) in 'window' with text on top of it saying "Enter"
bt = tkinter.Button(window,text="Enter", fg = 'red',command = clicked)

txt = tkinter.Entry(window, width = 10)
txt.grid(column =1, row=0)

#set the position of 'bt' button in the second column but the first row
bt.grid(column=2,row=0)

window.geometry('550x550')

#sets the position of the label as the first column and the first row
label.grid(column = 0, row = 0)

#the action carried out when the button is click
def clicked():
    #if clicked, the programme searches google maps of the location extered
    if len(txt.get()) > 1: 
        webbrowser.open('https://www.google.co.uk/maps/search/' + str(txt.get()))


#excutes the window
window.mainloop()