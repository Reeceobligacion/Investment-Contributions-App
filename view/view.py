"""
The Parent view, connects all the child view modules
"""

try:
	import Tkinter as Tk # python 2
except ModuleNotFoundError:
	import tkinter as Tk # python 3

from view.search import Create_Search
from view.input_fields import Create_Entries
from view.investments_list import Create_List
from view.dashboard import Create_Dashboard
from view.buttons import Create_Buttons 

class View:
	def __init__(self, root):
		self.search_field = Create_Search(root)
		self.entry_fields = Create_Entries(root)
		self.buttons = Create_Buttons(root)
		self.investment_list = Create_List(root)
		self.dashboard = Create_Dashboard(root)