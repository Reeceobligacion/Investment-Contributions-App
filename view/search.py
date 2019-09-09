"""
Frame to search the DB
"""

try:
	import Tkinter as Tk # python 2
except ModuleNotFoundError:
	import tkinter as Tk # python 3


class Create_Search:
    def __init__(self, root):
        self.search_frame = Tk.LabelFrame(root, text="Search Entries Here")
        self.search_frame.pack()

        self.search_text = Tk.StringVar()
        self.search_entry = Tk.Entry(self.search_frame, textvariable=self.search_text)
        self.search_button = Tk.Button(self.search_frame, text="Search", width=20)
        self.search_entry.pack(side=Tk.LEFT)
        self.search_button.pack(side=Tk.RIGHT)
