# from .interfaceGUI import my_GUI

#import sys
#sys.path.append(r'C:\Users\geoffe.elias.CEPHAS\source\repos\PythonScreenScraper1') # 'r' added to prevent error

#from .interfaceGUI.my_GUI import my_GUI

from CiscoManagerGUI import *
import tkinter as tk
from tkinter import Button, Label, Menu
from tkinter import *

self = tk.Tk()
self.geometry('1000x800')
self.title('Cisco Device Manager GUI')



# Set up upper Menu bar
menubar = Menu(self)
Open = Menu(menubar)
menubar.add_cascade(label='Open', menu=Open)
Open.add_command(label='New Device',accelerator="Ctrl_N",command=lambda: openNewWindow(self,targetDevice))
Open.add_separator()
Open.add_command(label='Close and Quit',command=self.destroy)




# Set of Buttons and Text Boxes

Label(self, text="No Device Selected", font= ('Helvetica 15 underline'),
background="gray74").pack(pady=20, side= TOP, anchor="w")

buttonShowIPARP=Button(self, text='Show IP ARP',bd=5,command=buttonClick1(self))
buttonShowIPARP.pack(side='top')



buttonClear=Button(self,text='Clear',bd=5,command=buttonClick2(self))
buttonClear.pack(side='bottom')



self.config(menu=menubar)
self.textboxOutput = tk.Text(self, height=30, font=('Arial',16))

self.textboxOutput.pack(padx=10, pady=10)


self.mainloop()