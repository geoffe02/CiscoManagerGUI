
import tkinter as tk
from tkinter import ttk #Make the buttons look like standard Windows or Mac buttons

#Create Window Tkinter

window = tk.Tk()

window.title("Cisco Manager") 
window.geometry("420x420")
width = window.winfo_screenwidth()               
height = window.winfo_screenheight()               
#window.geometry("%dx%d" % (width, height))
# Create a label widget in Tkinter
label = tk.Label(window, text="Click the Button",
font=('Calibri 15 bold'))
label.pack(pady=20)

# Function to update the label text for first button click in Tkinter
def on_click_btn1():
    label["text"] = "First button clicked"
     
# Function to update the label text for second button click in Tkinter
def on_click_btn2():
    label["text"] = "Second button clicked"

# Entry Box

entry = tk.Entry(fg="yellow", bg="blue", width=50)

# Create 1st Entry Box

# Create 1st button to update the label widget
btn1 = tk.Button(window, text="Button1", command=on_click_btn1)
btn1.pack(pady=20)
 
# Create 2nd button to update the label widget
btn2 = tk.Button(window, text="Button2", command=on_click_btn2)
btn2.pack(pady=40)

window.mainloop()