"""
This Controller connects the View with the Model
The Controller understands both the Model and Controller
Whereas the Model and View know nothing about each other
"""

try:
	import Tkinter as Tk # python 2
except ModuleNotFoundError:
	import tkinter as Tk # python 3

from model.model import Model
from view.view import View

class Controller:
	def __init__(self):
		self.root = Tk.Tk()
		self.model = Model("investment.db")
		self.view = View(self.root) 
		self.view.search_field.search_button.config(command=self.search_command)
		self.view.buttons.b1_viewall.config(command=self.view_command)
		self.view.buttons.b2_add.config(command=self.add_command)
		self.view.buttons.b3_update.config(command=self.update_command)
		self.view.buttons.b4_delete.config(command=self.delete_command)
		self.view.buttons.b5_close.config(command=self.root.destroy)

		# Builds the listbox with all the entries on init
		self.view.investment_list.build_list(self.model.view())
		self.view.investment_list.investment_list.bind('<<TreeviewSelect>>', self.selectedItem)

		# Create a Dataframe for ease of computation
		self.total_df = self.model.invest_dataframe() 
		self.invtype_total_df = self.total_df.groupby('investment_type')

		# Dashboard Labels on init
		self.dashboard_summary_labels('Create')

		# Chart on init
		self.view.dashboard.update_chart(self.invtype_total_df['principal_amount'].sum(), self.invtype_total_df.groups.keys())

	# =========== Functions ===========
	def start(self):
		"""
		Activation function to start the mainloop
		"""
		self.root.title("Principal Contributions Tracker")
		self.root.mainloop()

	def selectedItem(self, event): # the "event" parameter is needed since we binded this function to investment list
		"""
		Puts the selected entry in focus and populates the entry fields with the items data
		"""
		try:
			curItem = self.view.investment_list.investment_list.focus()
			self.selected_tuple = self.view.investment_list.investment_list.item(curItem)['values']
			self.view.entry_fields.e1_date.delete(0, Tk.END)
			self.view.entry_fields.e1_date.insert(Tk.END, self.selected_tuple[1])
			self.view.entry_fields.e2_invname.delete(0, Tk.END)
			self.view.entry_fields.e2_invname.insert(Tk.END, self.selected_tuple[2])
			self.view.entry_fields.e3_trdsym.delete(0, Tk.END)
			self.view.entry_fields.e3_trdsym.insert(Tk.END, self.selected_tuple[3])
			self.view.entry_fields.e4_amt.delete(0, Tk.END)
			self.view.entry_fields.e4_amt.insert(Tk.END, self.selected_tuple[4])
			self.view.entry_fields.e5_shares.delete(0, Tk.END)
			self.view.entry_fields.e5_shares.insert(Tk.END, self.selected_tuple[5])
			self.view.entry_fields.e6_purch_price.delete(0, Tk.END)
			self.view.entry_fields.e6_purch_price.insert(Tk.END, self.selected_tuple[6])
			self.view.entry_fields.invtype_text.set(self.selected_tuple[7])
			self.view.entry_fields.e8_broker.delete(0, Tk.END)
			self.view.entry_fields.e8_broker.insert(Tk.END, self.selected_tuple[8])
		except:
			pass # In case that investment_list is empty, this function will not run	

	def view_command(self):
		"""
		Views all of the entries
		"""
		self.view.investment_list.empty_list()
		self.view.investment_list.update_list(self.model.view())
		
	def search_command(self):
		"""
		Search through all entries and populates with matching entries
		"""
		self.view.investment_list.empty_list()
		self.view.investment_list.update_list(self.model.search(self.view.search_field.search_text.get()))
	
	def add_command(self):
		"""
		Adds a new entry
		"""
		# Adds new entry into DB
		self.model.insert(self.view.entry_fields.date_text.get(), self.view.entry_fields.invname_text.get(), 
						self.view.entry_fields.trdsym_text.get(), self.view.entry_fields.amt_text.get(), self.view.entry_fields.shares_text.get(), 
						self.view.entry_fields.purch_price_text.get(), self.view.entry_fields.invtype_text.get(), self.view.entry_fields.broker_text.get())

		# Renders an updated list/dashboard after adding entry
		self.update_dataframes()
		self.view.dashboard.update_chart(self.invtype_total_df['principal_amount'].sum(), self.invtype_total_df.groups.keys())
		self.dashboard_summary_labels('Update')
		self.view_command()

	def update_command(self):
		"""
		Updates entry in focus
		"""
		# Updates selected entry in DB
		self.model.update(self.selected_tuple[0], self.view.entry_fields.date_text.get(), self.view.entry_fields.invname_text.get(), 
						self.view.entry_fields.trdsym_text.get(), self.view.entry_fields.amt_text.get(), self.view.entry_fields.shares_text.get(), 
						self.view.entry_fields.purch_price_text.get(), self.view.entry_fields.invtype_text.get(), self.view.entry_fields.broker_text.get())

		# Renders an updated list/dashboard after updating selected entry
		self.update_dataframes()
		self.view.dashboard.update_chart(self.invtype_total_df['principal_amount'].sum(), self.invtype_total_df.groups.keys())
		self.dashboard_summary_labels('Update')
		self.view_command()

	def delete_command(self):
		"""
		Deletes entry in focus
		"""
		# Deletes selected entry from DB
		self.model.delete(self.selected_tuple[0]) 

		# Renders an updated list/dashboard after deleting selected entry
		self.update_dataframes() 
		self.view.dashboard.update_chart(self.invtype_total_df['principal_amount'].sum(), self.invtype_total_df.groups.keys())
		self.dashboard_summary_labels('Update')
		self.view_command() 
	
	def dashboard_summary_labels(self, action): 
		"""
		Summarizes the contributions in dashboard
		"""
		if action == 'Create':
			self.view.dashboard.total_contrib_label.config(text=f"Total Principal Contributions: ${self.total_df['principal_amount'].sum()}")
			self.view.dashboard.total_crypto_label.config(text=f"Crypto Total Contributions: ${self.total_df[self.total_df.investment_type == 'Crypto']['principal_amount'].sum()}")
			self.view.dashboard.total_stock_label.config(text=f"Stock Total Contributions: ${self.total_df[self.total_df.investment_type == 'Stock']['principal_amount'].sum()}")
			self.view.dashboard.total_bond_label.config(text=f"Bond Total Contributions: ${self.total_df[self.total_df.investment_type == 'Bond']['principal_amount'].sum()}")
			self.view.dashboard.total_alt_label.config(text=f"Alternative Total Contributions: ${self.total_df[self.total_df.investment_type == 'Alternative']['principal_amount'].sum()}")
		elif action == 'Update':
			self.view.dashboard.total_contrib_label["text"] = f"Total Principal Contributions: ${self.total_df['principal_amount'].sum()}" # Updates that total principal contributions when add
			self.view.dashboard.total_crypto_label["text"] = f"Crypto Total Contributions: ${self.total_df[self.total_df.investment_type == 'Crypto']['principal_amount'].sum()}" # Updates the total crypto contributions when add
			self.view.dashboard.total_stock_label["text"] = f"Stock Total Contributions: ${self.total_df[self.total_df.investment_type == 'Stock']['principal_amount'].sum()}" # Updates the total stock contributions when add
			self.view.dashboard.total_bond_label["text"] = f"Bond Total Contributions: ${self.total_df[self.total_df.investment_type == 'Bond']['principal_amount'].sum()}" # Updates the total stock contributions when add
			self.view.dashboard.total_alt_label["text"] = f"Alternative Total Contributions: ${self.total_df[self.total_df.investment_type == 'Alternative']['principal_amount'].sum()}" # Updates the total stock contributions when add
		else:
			pass

	def update_dataframes(self): 
		"""
		Updates pandas dataframe for ease of computation
		"""
		# Updates the total DF and the investment type DF
		self.total_df = self.model.invest_dataframe() 
		self.invtype_total_df = self.total_df.groupby('investment_type')