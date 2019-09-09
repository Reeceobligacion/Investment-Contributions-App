"""
Frame for the entry fields in our application
"""

try:
	import Tkinter as Tk # python 2
except ModuleNotFoundError:
	import tkinter as Tk # python 3

class Create_Entries:
	def __init__(self, root):
		self.entry_frame = Tk.LabelFrame(root, text="Enter Info Here")
		self.entry_frame.pack()

		# Labels for inputs
		self.l1_date = Tk.Label(self.entry_frame, text="Purchase Date")
		self.l2_invname = Tk.Label(self.entry_frame, text="Investment Name")
		self.l3_trdsym = Tk.Label(self.entry_frame, text="Trading Symbol")
		self.l4_amt = Tk.Label(self.entry_frame, text="Principal Amount")
		self.l5_shares = Tk.Label(self.entry_frame, text="# of Shares")
		self.l6_purch_price = Tk.Label(self.entry_frame, text="Purchase Price")
		self.l7_type = Tk.Label(self.entry_frame, text="Investment Type")
		self.l8_broker = Tk.Label(self.entry_frame, text="Broker")

		# Entry Boxes for inputs
		# date_text, invname_text, trdsym_text, amt_text, shares_text, purch_price_text, invtype_text, broker_text
		self.date_text = Tk.StringVar() # Possibly change this input into a date picker
		self.e1_date = Tk.Entry(self.entry_frame, textvariable=self.date_text)
		self.invname_text = Tk.StringVar() 
		self.e2_invname = Tk.Entry(self.entry_frame, textvariable=self.invname_text)
		self.trdsym_text = Tk.StringVar()
		self.e3_trdsym = Tk.Entry(self.entry_frame, textvariable=self.trdsym_text)
		self.amt_text = Tk.StringVar()
		self.e4_amt = Tk.Entry(self.entry_frame, textvariable=self.amt_text)
		self.shares_text = Tk.StringVar()
		self.e5_shares = Tk.Entry(self.entry_frame, textvariable=self.shares_text)
		self.purch_price_text = Tk.StringVar()
		self.e6_purch_price = Tk.Entry(self.entry_frame, textvariable=self.purch_price_text)
		# Creates a dropdown for investment type
		invtype_choices = ['Stock', 'Bond', 'Alternative', 'Crypto']
		self.invtype_text = Tk.StringVar()
		self.invtype_text.set('Stock')
		self.e7_type = Tk.OptionMenu(self.entry_frame, self.invtype_text, *invtype_choices)
		self.broker_text = Tk.StringVar() 
		self.e8_broker = Tk.Entry(self.entry_frame, textvariable=self.broker_text)

		# entry_frame Grid Layout
		self.l1_date.grid(row=0, column=0)
		self.e1_date.grid(row=1, column=0)
		self.l2_invname.grid(row=0, column=1)
		self.e2_invname.grid(row=1, column=1)
		self.l3_trdsym.grid(row=0, column=2)
		self.e3_trdsym.grid(row=1, column=2)
		self.l4_amt.grid(row=0, column=3)
		self.e4_amt.grid(row=1, column=3)
		self.l5_shares.grid(row=2, column=0)
		self.e5_shares.grid(row=3,column=0)
		self.l6_purch_price.grid(row=2, column=1)
		self.e6_purch_price.grid(row=3, column=1)
		self.l7_type.grid(row=2, column=2)
		self.e7_type.grid(row=3, column=2)
		self.l8_broker.grid(row=2, column=3)
		self.e8_broker.grid(row=3, column=3)