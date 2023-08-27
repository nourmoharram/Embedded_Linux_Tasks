'''
Task description : 
● Toggle Led
'''

from tkinter import *

def Led_ON():
    circle.create_oval(70,70,200,200,fill='red')

def Led_OFF():
    circle.create_oval(70,70,200,200,fill='white')


#window Init   
window = Tk()
window.title("Calculate Factorial!")
window.geometry("300x300+150+200")
window.configure(background="white")
window.resizable(False, False)

circle = Canvas(window,width=500, height=500)
circle.pack()
circle.create_oval(70,70,200,200,fill='white')

# #handlers
button1 = Button(window, text="Led On", fg="black", bg="white", width=10,command=Led_ON )
button2 = Button(window, text="Led Off", fg="black", bg="white", width=10,command=Led_OFF)

#placing
button1.place(x=60,y=250)
button2.place(x=150,y=250)

window.mainloop()
