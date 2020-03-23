# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 14:39:41 2020

@author: Henry
"""

import tkinter, webbrowser

#Creates the GUI window in the computer memory
window = tkinter.Tk() 
window.geometry('350x150')
#Set the naem of the window
window.title("Henry's Searches")

class Search:
    def __init__(self,label, URL_1, URL_2, rows):
        self.label = label
        self.URL_1 = URL_1
        self.URL_2 = URL_2
        self.rows = rows
        
    def show(self):
                
        shown = tkinter.Label(window,text = self.label, font=('Arial',11))
        shown.grid(row = self.rows, column = 0)
        
        txt = tkinter.Entry(window, width = 15)
        txt.grid(row = self.rows, column = 1)
        
        def clicked():
            if len(txt.get()) > 1:
                webbrowser.open(str(self.URL_1) + txt.get() + str(self.URL_2))
                
        bt = tkinter.Button(window, text = "Enter", command = clicked)
        bt.grid(row = self.rows, column = 2)      
                        
maps = Search('Google maps search', 'https://www.google.co.uk/maps/search/','',0)
maps.show()

netflix = Search('Netflix search','https://www.netflix.com/search?q=','',1)
netflix.show()

prime_video = Search('Amazon Prime video search','https://www.amazon.co.uk/s?i=instant-video&k=','&ref=nb_sb_noss_2&url=search-alias%3Dinstant-video',2)
prime_video.show() 

google_search = Search('Google search','https://www.google.com/search?q=','',3)
google_search.show()

#excutes the window
window.mainloop()

