# importing whole module
from tkinter import *
from tkinter.ttk import *

# importing strftime function to
# retrieve system's time
from time import strftime

# creating tkinter window
root = Tk()
root.title('Clock')


# Placing clock at the centre
# of the tkinter window
lbl.pack(anchor='center')
time()

mainloop()
