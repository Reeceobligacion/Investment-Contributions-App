"""
Child component to view, holds the frame and components for buttons
"""

try:
	import Tkinter as Tk # python 2
except ModuleNotFoundError:
	import tkinter as Tk # python 3

class Create_Buttons:
    def __init__(self, root):
       self.buttons_frame = Tk.LabelFrame(root, text="Buttons Frame")
       self.buttons_frame.pack()

       # Command buttons
       self.b1_viewall = Tk.Button(self.buttons_frame, text="View All", width=20)
       self.b2_add = Tk.Button(self.buttons_frame, text="Add Entry", width=20)
       self.b3_update = Tk.Button(self.buttons_frame, text="Update Selected", width=20)
       self.b4_delete = Tk.Button(self.buttons_frame, text="Delete Selected", width=20)
       self.b5_close = Tk.Button(self.buttons_frame, text="Close Program", width=20)

       # buttons_frame Grid Layout
       self.b1_viewall.pack(side=Tk.LEFT)
       self.b2_add.pack(side=Tk.LEFT)
       self.b3_update.pack(side=Tk.LEFT)
       self.b4_delete.pack(side=Tk.LEFT)
       self.b5_close.pack(side=Tk.LEFT)