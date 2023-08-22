
from ast import Delete, Lambda
import ipaddress

from this import s
import tkinter as tk
from tkinter import Button, Checkbutton, Label, Menu, Toplevel
from tkinter import *
from turtle import title
from typing import Self

import CiscoConnectHandler
import deviceCiscoModel


# Data Object to be manipulated
targetDevice=deviceCiscoModel.deviceCiscoModel
ipaddressText="null"

def openNewWindow(self,targetDevice):
    newWindow = Toplevel(self)
    newWindow.title("Manage new Cisco device")
    newWindow.geometry("500x500")
    Label(newWindow,text="Enter device parameters here.").pack()

    # Local Variables

    

    Label(newWindow,text="Enter IP Address here.").pack(side=LEFT)
    inputTextBox1=tk.Text(newWindow,height=1,width=20)
    #inputTextBox1.grid(row=5,column=0)
    inputTextBox1.pack(side=LEFT)
    buttonSetIPAddr=tk.Button(newWindow,text='Apply',command=lambda: buttonSetIPAddr_onClick(str(inputTextBox1.get("1.0",END))))
    buttonSetIPAddr.pack(side=LEFT)

    Button(newWindow,text='OK',command=newWindow.destroy).pack()



    CheckBoxValue1 = IntVar()
    CheckBoxValue2 = IntVar()
    CheckBoxValue3 = IntVar()

    Button1 = Checkbutton(newWindow, text="button1",
                          variable = CheckBoxValue1,
                          onvalue=1,
                          offvalue=0,
                          height=2,
                          width=10)

    Button1.pack()

    Button2 = Checkbutton(newWindow, text="button2",
                          variable = CheckBoxValue2,
                          onvalue=1,
                          offvalue=0,
                          height=2,
                          width=10)

    Button2.pack()

    Button3 = Checkbutton(newWindow, text="button3",
                          variable = CheckBoxValue3,
                          onvalue=1,
                          offvalue=0,
                          height=2,
                          width=10)

    Button3.pack()

    Checkbox1 = tk.Checkbutton(newWindow,text="checkbox", variable=CheckBoxValue1)



    # Add a Text Box
    #newWindow.textboxOutput = tk.Text(newWindow, height=5, font=('Arial',16))
    #newWindow.textboxOutput.pack(padx=10, pady=10)

#def inputDeviceIPAddr(targetDevice(), IPAddress):
 #   targetDevice.setHostIP(targetDevice, ipaddress)

def show_message(self):
    print(self.check_state.get())

def buttonSetIPAddr_onClick(ipaddressText):
    print("button pressed to show IP address entered")
    targetDevice.setHostIP(targetDevice, ipaddressText)
    print(str(targetDevice.getHostIP(targetDevice)))




def buttonClick1(self):
    targetDevice.deviceShowIPARP(targetDevice)
    self.textboxOutput.insert(1.0, targetDevice.showOutput(targetDevice))
    print("Button Clicked!")

def buttonClick2(self):
    self.textboxOutput.delete('1.0',END)

## End of Definitions/Methods ##

# self = tk.Tk()
# self.geometry('1000x800')
# self.title('Cisco Device Manager GUI')



# # Set up upper Menu bar
# menubar = Menu(self)
# Open = Menu(menubar)
# menubar.add_cascade(label='Open', menu=Open)
# Open.add_command(label='New Device',accelerator="Ctrl_N",command=lambda: openNewWindow(targetDevice))
# Open.add_separator()
# Open.add_command(label='Close and Quit',command=self.destroy)




# # Set of Buttons and Text Boxes

# Label(self, text="No Device Selected", font= ('Helvetica 15 underline'),
# background="gray74").pack(pady=20, side= TOP, anchor="w")

# buttonShowIPARP=Button(self, text='Show IP ARP',bd=5,command=buttonClick1)
# buttonShowIPARP.pack(side='top')



# buttonClear=Button(self,text='Clear',bd=5,command=buttonClick2)
# buttonClear.pack(side='bottom')



# self.config(menu=menubar)
# self.textboxOutput = tk.Text(self, height=30, font=('Arial',16))

# self.textboxOutput.pack(padx=10, pady=10)


# self.mainloop()







