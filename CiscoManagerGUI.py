
import tkinter as tk
from tkinter import Button, Checkbutton, Label, Menu, Toplevel
from tkinter import *
from turtle import title

def openNewWindow():
    newWindow = Toplevel(self)
    newWindow.title("Manage new Cisco device")
    newWindow.geometry("500x500")
    Label(newWindow,text="Enter device parameters here.").pack()
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
    newWindow.textbox = tk.Text(newWindow, height=5, font=('Arial',16))
    newWindow.textbox.pack(padx=10, pady=10)
    #newWindow.check = tk.Checkbutton(newWindow, text="Show Messagebox", font=('Arial',16),variable=newWindow.check_state)
    #newWindow.check.pack(padx=10,pady=10)

    #newWindow.button = tk.Button(newWindow, text="Show Message", font=('Arial', 18), command=newWindow.show_message)
    #newWindow.button.pack(padx=10,pady=10)

        #self.root.mainloop()

        #targetDevice = deviceCiscoModel()
  
def show_message(self):
    print(self.check_state.get())

#def newWindow():
# Main Window

self = tk.Tk()
self.geometry('500x500')
self.title('Cisco Device Manager GUI')

# Set up upper Menu bar
menubar = Menu(self)

Open = Menu(menubar)
menubar.add_cascade(label='Open', menu=Open)
Open.add_command(label='New Device',accelerator="Ctrl_N",command=openNewWindow)
Open.add_separator()
Open.add_command(label='Close and Quit',command=self.destroy)




self.config(menu=menubar)

self.mainloop()





        #self.label = tk.Label(self.root, text="Your Message", font=('Arial',18))
        #self.label.pack(padx=10, pady=10)
        #self.textbox = tk.Text(self.root, height=5, font=('Arial',16))
        #self.textbox.pack(padx=10, pady=10)

        #self.check_state = tk.IntVar()


        #self.check = tk.Checkbutton(self.root, text="Show Messagebox", font=('Arial',16), variable=self.check_state)
        #self.check.pack(padx=10,pady=10)

        #self.button = tk.Button(self.root, text="Show Message", font=('Arial', 18), command=self.show_message)
        #self.button.pack(padx=10,pady=10)

        #self.root.mainloop()

        #targetDevice = deviceCiscoModel()
  
    #def show_message(self):
    #    print(self.check_state.get())
        


# 
# my_GUI()




