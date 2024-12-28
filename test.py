import json
from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
monty = ttk.LabelFrame(text=' Mighty Python ')
monty.grid(column=0, row=0, padx=8, pady=4) 
ttk.Label(monty, text="Choose a number:").grid(column=1, row=0)

numberChosen = ttk.Combobox(monty, width=12, textvariable="")
numberChosen['values'] = (42)
numberChosen.grid(column=1, row=1)
numberChosen.current(0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=5, row=1)
root.mainloop()


with open("/home/machine/Documents/cred.json", "r") as file:
    a = json.load(file)

print(a)