'''
Task description : 
● Write a program that asks the user to type a word
and return him its reverse
'''

from tkinter import *


def Reverse_string():
    String=e1.get() [::-1]
    result_label.config(text=f"{String}")
    

 #window Init   
window = Tk()
window.title("Display names")
window.geometry("400x100+150+200")
window.configure(background="white")
window.resizable(False, False)

#handlers
button1 = Button(window, text="Reverse!", fg="black", bg="white", width=10, command=Reverse_string)
Label1=Label(window, text='Enter the string: ', fg="black", bg="white")
result_label = Label(window, text=' ', fg="black", bg="white")
e1 = Entry(window)



# #placing
Label1.grid(row=1,column=0)
e1.grid(row=1,column=1)
result_label.grid(row=1,column=2)
button1.grid(row=3,column=1)



window.mainloop()
