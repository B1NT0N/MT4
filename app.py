import tkinter as tk
from metaapi_cloud_sdk import MetaStats, MetaApi
import asyncio
import time
import os
import json
import requests
import main
from dotenv import load_dotenv
from tkinter import messagebox
load_dotenv()

class App():

    def __init__(self,master=None):
        
        self.account_info=None
        self.positions_info=None
        self.profit=0.0
        # your MetaApi API token
        self.api_token = os.getenv('API_TOKEN')
        # your MetaApi account id
        self.account_id = os.getenv('ACCOUNT_ID')
        # your MetaApi account
        self.account = None
        
        self.label_balance = tk.Label(root, text ="",
                                        font=('Helvetica', 10),
                                        fg='White',
                                        bg='#1e1e1e',
                                        padx=8,)
        self.label_balance.grid(row = 0, column = 0, sticky = 'W',padx=2,pady=2)
        
        self.label_equity = tk.Label(root, text ="",
                                        font=('Helvetica', 10),
                                        fg='White',
                                        bg='#1e1e1e',
                                        padx=8)
        self.label_equity.grid(row = 1, column = 0, sticky = 'W',padx=2,pady=2)
        
        self.label_free_margin = tk.Label(root, text ="",
                                        font=('Helvetica', 10),
                                        padx=8,
                                        fg='White',
                                        bg='#1e1e1e')
        self.label_free_margin.grid(row = 2, column = 0, sticky = 'W',padx=2,pady=2)
        
        self.label_total = tk.Label(root, text ="",
                                        font=('Helvetica', 20),
                                        fg=f"{'Green' if (self.profit>0) else 'Red'}",
                                        bg='#1e1e1e')
        self.label_total.grid(row = 0, column = 1, rowspan = 3,padx=5,pady=10)
        
        self.listbox = tk.Listbox(root,
                                    height=18,
                                    width=45,
                                    bg='#252526',
                                    bd=0,
                                    highlightcolor='#3e3e42',
                                    selectbackground='#007acc'
                                    )
        self.listbox.grid(row = 3, column = 0, columnspan = 3,padx=13,pady=10)
        
    def update_data(self):
        self.account_info = main.get_account_info(self.api_token,self.account_id)
        self.positions_info = main.get_positions_info(self.api_token,self.account_id)
        
        try:
            self.label_balance.config(text=f"Balance --------------->{format(self.account_info['balance'],'.2f')}")
            
            self.label_equity.config(text=f"Equity ----------------->{format(self.account_info['equity'],'.2f')}")
            
            self.label_free_margin.config(text=f"Free Margin --------->{format(self.account_info['freeMargin'],'.2f')}")
            
            if len(self.positions_info)!=0:
                for position in self.positions_info:
                    self.profit+=position['profit']
            else:
                self.profit=0.0

            self.label_total.config(text =f"{format(self.profit,'.2f')}$")
            
            if len(self.positions_info)!=0:
                for position in self.positions_info:
                    self.listbox.insert('end', 
                                        f"{position['symbol']} : {'SELL' if (position['type'] == 'POSITION_TYPE_SELL') else 'BUY'}                                                      {format(position['profit'],'.2f')}",
                                        )
                    self.listbox.itemconfig("end",
                                            bg=f"{'Green' if (position['profit']>0)else 'Red'}",
                                            fg=f"{'Black' if (position['profit']>0)else 'White'}")
            else:
                self.listbox.insert('end', "Null")
            
        except Exception as error:
                tk.messagebox.showerror('error', f'{self.account_info["error"]}')
        
                

root = tk.Tk()

root.geometry('300x400')
root.resizable(False,False)
root.iconbitmap("images/mt4.ico")
root.title("MT4 View")
root.configure(bg='#1e1e1e')

app = App(root)
root.after(6000,app.update_data)
root.mainloop()
