#!/usr/bin/env python
from tkinter import *
from tkinter import ttk
import os
import signal
from subprocess import Popen, PIPE, run

#Create an instance of Tkinter frame
win = Tk()
#Set the geometry of the Tkinter frame
win.geometry("700x250")

greeting = ttk.Label(text="Welcome to the Digi-Sm launcher!",font=("Arial", 25))
greeting.grid(row=0, column=2, columnspan=2, padx=10, pady=10)

#Define a function to update the entry widget
def entry_update(text):
   
   #This launches a cmd window and runs the server script closing the tkinter window
   if text == "Load existing database":
      run(["python", ".\launchServerScript.py", str(os.getpid()), ""], stdout=PIPE, stderr=PIPE)
   elif text == "Create virgin database":
      run(["python", ".\launchServerScript.py", str(os.getpid()), "virgin"], stdout=PIPE, stderr=PIPE)
   elif text == "Create dummy database":
      run(["python", ".\launchServerScript.py", str(os.getpid()), "dummy"], stdout=PIPE, stderr=PIPE)



#Create Multiple Buttons with different commands
button_dict={}
option = ["Load existing database", "Create virgin database", "Create dummy database"]
answer= ["Loads existing database on launch", "This will launch a virgin database", "This is will load mock data which was used for this project"]
comments = ["This will load the existing database or create a virgin one if none exist", "This will create a brand new empty database, warning will delete existing database", "This will load the user stories used to create this project, warning will delete existing database"]

for i in option:
   def func(x=i):
      return entry_update(x)

   button_dict[i]=ttk.Button(win, text=i, command= func)
   button_dict[i].grid(row=option.index(i)+1, column=2 , padx=10, pady=10, sticky=W)

for comment in comments:
   ttk.Label(win, text=comment).grid(row=comments.index(comment)+1, column=3, padx=10, pady=10, sticky=W)

win.mainloop()