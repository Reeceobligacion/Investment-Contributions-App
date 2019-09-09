"""
This is for the dashboard, allows the user to see an overview of all the contributions they've made
"""

try:
  import Tkinter as Tk # python 2
except ModuleNotFoundError:
  import tkinter as Tk # python 3

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

style.use("ggplot")

class Create_Dashboard:
  def __init__(self, root):
    # This component creates a parent frame and two child frames, one to hold the charts and another to hold the account overview
    self.frame = Tk.Frame(root)
    self.frame.pack()

    # =========== Frame for Dashboard ===========
    self.dash_frame = Tk.LabelFrame(self.frame, text="Account Overview")
    self.dash_frame.pack(side=Tk.RIGHT)

    # =========== Dynamic Descriptive Labels ===========
    self.total_contrib_label = Tk.Label(self.dash_frame)
    self.total_contrib_label.pack()

    self.total_crypto_label = Tk.Label(self.dash_frame)
    self.total_crypto_label.pack()

    self.total_stock_label = Tk.Label(self.dash_frame)
    self.total_stock_label.pack()

    self.total_bond_label = Tk.Label(self.dash_frame)
    self.total_bond_label.pack()

    self.total_alt_label = Tk.Label(self.dash_frame)
    self.total_alt_label.pack()

    # Investment Type Diversification Plot
    self.fig1 = Figure(figsize=(4,4))
    self.ax1 = self.fig1.add_subplot(111)
    self.ax1.set_title('Investment Type Portfolio Diversification')
    
    self.canvas = FigureCanvasTkAgg(self.fig1, master=self.frame)
    self.canvas.get_tk_widget().pack(side=Tk.LEFT)
    self.canvas.draw()
  
  # Update Function for Investment Type Diversification Plot
  def update_chart(self, graph_data, label_data):
    self.ax1.clear()
    print('Clearing graph and recreating')
    self.ax1.pie(graph_data, autopct='%1.0f%%')
    self.ax1.legend(label_data)
