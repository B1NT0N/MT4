import tkinter as tk

root = tk.Tk()
root.geometry('300x400',)
root.resizable(False,False)
root.iconbitmap("images/mt4.ico")
root.title("MT4 View")


label_balance = tk.Label(root, text ="Balance ---------------> 50.00$",font=('Helvetica', 10),padx=8).grid(row = 0, column = 0, sticky = 'W',padx=2,pady=2)
label_equity = tk.Label(root, text ="Equity -----------------> 50.00$ ",font=('Helvetica', 10),padx=8).grid(row = 1, column = 0, sticky = 'W',padx=2,pady=2)
label_free_margin = tk.Label(root, text ="Free Margin ---------> 50.00$",font=('Helvetica', 10),padx=8).grid(row = 2, column = 0, sticky = 'W',padx=2,pady=2)

label_total = tk.Label(root, text ="100.00$", font=('Helvetica', 20)).grid(row = 0, column = 1, rowspan = 3,padx=5,pady=10)

listbox = tk.Listbox(root,height=18,width=45,activestyle = 'dotbox')

for values in range(100):
    listbox.insert('end', values)
    
listbox.grid(row = 3, column = 0, columnspan = 3,padx=13,pady=10)

root.mainloop()