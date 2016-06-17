from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Ecotect result comparison for LEED certification")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

PATH_1 = StringVar()
PATH_2 = StringVar()
path_1_entry = ttk.Entry(mainframe, width=40, textvariable=PATH_1)
path_1_entry.grid(column=2, row=1, sticky=(W, E))
path_2_entry = ttk.Entry(mainframe, width=40, textvariable=PATH_2)
path_2_entry.grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Compare",command = ).grid(column=2, row=3, sticky=W)

ttk.Label(mainframe, width=25,text="first ecotect file:").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, width=25,text="second ecotect file:").grid(column=1, row=2, sticky=W)

#add a little bit padding for each cell.
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()
