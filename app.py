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
        
        
        self.label_balance = tk.Label(root, text =f"Balance --------------->{self.account_info['balance']}",
                                    font=('Helvetica', 10),
                                    fg='White',
                                    bg='#1e1e1e',
                                    padx=8,
                                    
                                    ).grid(row = 0, column = 0, sticky = 'W',padx=2,pady=2)
        self.label_equity = tk.Label(root, text =f"Equity ----------------->{self.account_info['equity']}",
                                    font=('Helvetica', 10),
                                    fg='White',
                                    bg='#1e1e1e',
                                    padx=8,
                                    
                                    ).grid(row = 1, column = 0, sticky = 'W',padx=2,pady=2)
        self.label_free_margin = tk.Label(root, text =f"Free Margin --------->{self.account_info['freeMargin']}",
                                    font=('Helvetica', 10),
                                    padx=8,
                                    fg='White',
                                    bg='#1e1e1e',
                                    ).grid(row = 2, column = 0, sticky = 'W',padx=2,pady=2)

        if len(self.positions_info)!=0:
            for position in self.positions_info:
                self.profit+=position['profit']
        else:
            self.profit=0.0

        self.label_total = tk.Label(root,
                                    text =f"{self.profit}$",
                                    font=('Helvetica', 20),
                                    fg=f"{'Green' if (self.profit>0) else 'Red'}",
                                    bg='#1e1e1e'
                                    ).grid(row = 0, column = 1, rowspan = 3,padx=5,pady=10)
        
        self.positions_info = main.get_positions_info(self.api_token, self.account_id)
        self.listbox = tk.Listbox(root,
                                  height=18,
                                  width=45,
                                #   activestyle = 'NONE',
                                  bg='#252526',
                                  bd=0,
                                  highlightcolor='#3e3e42',
                                  selectbackground='#007acc'
                                  )

        if len(self.positions_info)!=0:
            for position in self.positions_info:
                self.listbox.insert('end', 
                                    f"{position['symbol']} : {'SELL' if (position['type'] == 'POSITION_TYPE_SELL') else 'BUY'}                                                      {position['profit']}",
                                    )
                self.listbox.itemconfig("end",
                                        bg=f"{'Green' if (position['profit']>0)else 'Red'}",
                                        fg=f"{'Black' if (position['profit']>0)else 'White'}")
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
root.configure(bg='#1e1e1e')
App(root)
root.mainloop()
