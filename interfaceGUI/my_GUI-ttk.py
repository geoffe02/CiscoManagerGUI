import random
from tkinter import *
from tkinter import ttk
import tkinter

# Based upon https://www.youtube.com/watch?v=AANqCFjPyRE

class my_GUI(object):
    def __init__(self, parent): #constructor

        #Creating all the button and labels

        parent.title('Cisco Device Manager')
        parent.geometry('300x200')
        
        self.randomResult = StringVar()

        self.mainFrame = ttk.Frame(parent)
        self.mainFrame.grid()

        self.button1 = ttk.Button(self.mainFrame, text='Generate Random', command=self.randomNumGenerator())  # Button will call the method below
        self.button1.grid(row=1,column=0, padx=10,pady=10)

        self.button2 = ttk.Button(self.mainFrame, text='Button 2') # 2nd Button
        self.button2.grid(row=1,column=1,padx=10,pady=10)

        self.button1Result=ttk.Label(self.mainFrame,textvariable=self.randomResult.get())
        self.button1Result.grid(row=0,column=1, padx=10)

        #self.check_state = ttk.
        self.check = ttk.Checkbutton(self.mainFrame, text="checkbox")
        self.check.grid(row=2,column=1,padx=10,pady=10)

    def randomNumGenerator():
        randomNum = random.randint(1,100)
        self.randomResult.set(randomNum)

    def show_message(self):
        print(self.check_state.get())

                                  

        #self.root = tk.Tk()

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
  
#    def show_message(self):
#        print(self.check_state.get())

#my_GUI()

if __name__ == '__main__':
    root = Tk()
    ciscoManagerWindow = my_GUI(root)  #pass 1 parameter which is the root Window
    root.mainloop()  # required to start the Window.




