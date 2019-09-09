"""
The Model knows nothing about Controller or View
The backend of our application
Creates an embedded database to be used personally within our system
"""

import sqlite3
import pandas as pd

class Model:
	def __init__(self, db):
		self.conn = sqlite3.connect(db)
		self.cur = self.conn.cursor()
		self.cur.execute("""CREATE TABLE IF NOT EXISTS investment (
							id INTEGER PRIMARY KEY, 
							purchase_date text, 
							investment_name text, 
							trading_symbol text, 
							principal_amount integer, 
							num_shares integer, 
							purchase_price integer,
							investment_type text, 
							broker text
							)""")
		self.conn.commit()

	def insert(self, purchase_date, investment_name, trading_symbol, principal_amount, num_shares, purchase_price, investment_type, broker):
		self.cur.execute("INSERT INTO investment VALUES (NULL,?,?,?,?,?,?,?,?)",
						(purchase_date, investment_name, trading_symbol, principal_amount, num_shares, purchase_price, investment_type, broker))
		self.conn.commit()

	def view(self):
		self.cur.execute("SELECT * FROM investment")
		rows=self.cur.fetchall()
		return rows
	
	def search(self, search_entry):
		"""
		Possibly use FTS3 or FTS4, this is an extension which allows the user to do a full text search
		"""
		self.cur.execute("SELECT * FROM investment WHERE " + "purchase_date LIKE '%" + search_entry + "%' OR " + "investment_name LIKE '%" + search_entry + "%' OR " + "trading_symbol LIKE '%" + search_entry + "%' OR " + "principal_amount LIKE '%" + search_entry + "%' OR " + "num_shares LIKE '%" + search_entry + "%' OR " + "purchase_price LIKE '%" + search_entry + "%' OR " + "investment_type LIKE '%" + search_entry + "%' OR " + "broker LIKE '%" + search_entry + "%'")
		rows=self.cur.fetchall()
		return rows

	def delete(self,id):
		self.cur.execute("DELETE FROM investment WHERE id=?",(id,))
		self.conn.commit()

	def update(self, id, purchase_date, investment_name, trading_symbol, principal_amount, num_shares, purchase_price, investment_type, broker):
		self.cur.execute("UPDATE investment SET purchase_date=?, investment_name=?, trading_symbol=?, principal_amount=?, num_shares=?, purchase_price=?, investment_type=?, broker=? WHERE id=?", 
						(purchase_date, investment_name, trading_symbol, principal_amount, num_shares, purchase_price, investment_type, broker, id))
		self.conn.commit()

	def invest_dataframe(self): # Creates a pandas dataframe, used for ease of computation
		full_df = pd.read_sql_query("SELECT * FROM investment", self.conn)
		return full_df

	def __del__(self):
		self.conn.close()