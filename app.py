import tkinter as tk
from tkinter import ttk
import main
import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

class App():

    def __init__(self,master=None):
        
        self.profit=0.0
        
        self.api_token = os.getenv('API_TOKEN')
        self.account_id = os.getenv('ACCOUNT_ID')
        self.account_info = main.get_account_info(self.api_token, self.account_id)
        self.positions_info = main.get_positions_info(self.api_token, self.account_id)
        
        
        self.label_balance = tk.Label(root, text =f"Balance --------------->{self.account_info['balance']}",font=('Helvetica', 10),padx=8).grid(row = 0, column = 0, sticky = 'W',padx=2,pady=2)
        self.label_equity = tk.Label(root, text =f"Equity ----------------->{self.account_info['equity']}",font=('Helvetica', 10),padx=8).grid(row = 1, column = 0, sticky = 'W',padx=2,pady=2)
        self.label_free_margin = tk.Label(root, text =f"Free Margin --------->{self.account_info['freeMargin']}",font=('Helvetica', 10),padx=8).grid(row = 2, column = 0, sticky = 'W',padx=2,pady=2)

        if len(self.positions_info)!=0:
            for positions in self.positions_info:
                self.profit+=self.positions_info['profit']
        else:
            self.profit=0.0

        self.label_total = tk.Label(root, text =f"{self.profit}$", font=('Helvetica', 20)).grid(row = 0, column = 1, rowspan = 3,padx=5,pady=10)

        self.positions_info = main.get_positions_info(self.api_token, self.account_id)
        self.listbox = tk.Listbox(root,height=18,width=45,activestyle = 'dotbox')

        if len(self.positions_info)!=0:
            for positions in self.positions_info:
                self.listbox.insert('end', "ok")
        else:
            self.listbox.insert('end', "Null")
        
        self.listbox.grid(row = 3, column = 0, columnspan = 3,padx=13,pady=10)
        
        def update(self):
            
            self.account_info = main.get_account_info(self.api_token, self.account_id)
            self.positions_info = main.get_positions_info(self.api_token, self.account_id)
            
       
        
        
        
        
    

root = tk.Tk()

root.geometry('300x400')
root.resizable(False,False)
root.iconbitmap("images/mt4.ico")
root.title("MT4 View")
App(root)
root.mainloop()
