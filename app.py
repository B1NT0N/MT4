import tkinter as tk

root = tk.Tk()
root.geometry('300x400',)
root.resizable(False,False)
root.iconbitmap("images/mt4.ico")
root.title("MT4")


label_balance = tk.Label(root, text ="Balance ---------------> 50.00$",font=('Helvetica', 10)).grid(row = 0, column = 0, sticky = 'W',padx=5,pady=2)
label_equity = tk.Label(root, text ="Equity -----------------> 50.00$ ",font=('Helvetica', 10)).grid(row = 1, column = 0, sticky = 'W',padx=5,pady=2)
label_free_margin = tk.Label(root, text ="Free Margin ---------> 50.00$",font=('Helvetica', 10)).grid(row = 2, column = 0, sticky = 'W',padx=5,pady=2)

label_total = tk.Label(root, text ="100.00$", font=('Helvetica', 20)).grid(row = 0, column = 1, rowspan = 3,padx=5,pady=10)



# listbox = tk.Listbox(root)
# listbox.insert(1,"Test")
# listbox.insert(2,"OK")
# listbox.grid(row = 2, column = 0, sticky = 'W', columnspan = 2)

root.mainloop()