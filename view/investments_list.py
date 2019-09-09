"""
Frame to list out all our entries
"""

try:
    import Tkinter as Tk
    import tkFont
    import ttk
except ImportError: # Python 3
    import tkinter as Tk
    import tkinter.font as tkFont
    import tkinter.ttk as ttk

class Create_List: 
    def __init__(self, root):
        self.investment_list = None
        self.root = root
        self.investment_header = ['Index', 'Purchase Date', 'Investment Name', 'Trading Symbol', 'Principal Amount', '# of Shares', 'Purchase Price', 'Investment Type', 'Broker']
        self.setup_widgets(self.investment_header)

    def setup_widgets(self, investment_header):
        self.listdisplay_frame = Tk.LabelFrame(self.root, text="Investment Entries")
        self.listdisplay_frame.pack(fill=Tk.BOTH)

        self.investment_list = ttk.Treeview(columns=self.investment_header, show="headings")
        scrollbar = ttk.Scrollbar(orient="vertical", command=self.investment_list.yview)
        self.investment_list.configure(yscrollcommand=scrollbar.set)
        self.investment_list.grid(column=0, row=0, sticky='nsew', in_=self.listdisplay_frame)
        scrollbar.grid(column=1, row=0, sticky='ns', in_=self.listdisplay_frame)
        self.listdisplay_frame.grid_columnconfigure(0, weight=1)
        self.listdisplay_frame.grid_rowconfigure(0, weight=1)

    def build_list(self, entry_list):
        for col_header in self.investment_header:
            self.investment_list.heading(col_header, text=col_header.title())
            self.investment_list.column(col_header, width=tkFont.Font().measure(col_header.title()))

        for entry in entry_list:
            self.investment_list.insert('', 'end', values=entry)

            for ix, value in enumerate(entry):
                col_width = tkFont.Font().measure(value)
                if self.investment_list.column(self.investment_header[ix], width=None) < col_width:
                    self.investment_list.column(self.investment_header[ix], width=col_width)
    
    def update_list(self, entry_list):
        for entry in entry_list:
            self.investment_list.insert('', 'end', values=entry)
            
            for ix, value in enumerate(entry):
                col_width = tkFont.Font().measure(value)
                if self.investment_list.column(self.investment_header[ix], width=None) < col_width:
                    self.investment_list.column(self.investment_header[ix], width=col_width)

    def empty_list(self):
        self.listz = self.investment_list.get_children()
        for item in self.listz:
            self.investment_list.delete(item)