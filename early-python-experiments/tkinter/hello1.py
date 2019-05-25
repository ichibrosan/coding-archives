#!/usr/bin/python
# hello1.py

# We start by importing the Tkinter module. It contains all classes, 
# functions and other things needed to work with the Tk toolkit. 
# In most cases, you can simply import everything from Tkinter into 
# your module's namespace
from Tkinter import *

# To initialize Tkinter, we have to create a Tk root widget. 
# This is an ordinary window, with a title bar and other decoration 
# provided by your window manager. You should only create one
# root widget for each program, and it must be created before any
# other widgets.
root = Tk()

# A Label widget can display either text or an icon or other image. 
# In this case, we use the text option to specify which text to display. 
w = Label(root, text="Hello, world!")

# Next, we call the pack method on this widget, which tells it to size 
# itself to fit the given text, and make itself visible. But before this 
# happens, we have to enter the Tkinter event loop
w.pack()

# The program will stay in the event loop until we close the window. 
# The event loop doesn't only handle events from the user (such as 
# mouse clicks and key presses) or the windowing system (such as 
# redraw events and window configuration messages), it also handle 
# operations queued by Tkinter itself. Among these operations are 
# geometry management (queued by the pack method) and display 
# updates. This also means that the application window will not appear 
# before you enter the main loop.
root.mainloop()
