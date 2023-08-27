'''
Task description : 
● Make this template and each button display different name
'''

from tkinter import *


def Print1():
    print("Nour")

def Print2():
    print("Shady")

def Print3():
    print("Mohanad")

def Print4():
    print("Hesham")

 #window Init   
window = Tk()
window.title("Display names")
window.geometry("240x78+150+200")
window.configure(background="white")
window.resizable(False, False)

#handlers
button1 = Button(window, text="Button1", fg="black", bg="white", width=10, command=Print1)
button2 = Button(window, text="Button2", fg="black", bg="white", width=10, command=Print2)
button3 = Button(window, text="Button3", fg="black", bg="white", width=10, command=Print3)
button4 = Button(window, text="Button4", fg="black", bg="white", width=10, command=Print4)



# #placing
button1.grid(row=0,column=1)
button2.grid(row=1,column=0)
button3.grid(row=1,column=3)
button4.grid(row=2,column=1)


window.mainloop()
