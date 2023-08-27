'''
Task description : 
● Write a program in Python that displays a window to the user that asks them to enter an integer
N and displays its factorial
'''

from tkinter import *

result = 1

def Calculate_Factorial():
    global result
    try:
        number = int(e1.get())
        result = 1
        for x in range(1, number + 1):
            result *= x
        result_label.config(text=f"Factorial = {result}")
    except ValueError:
        result_label.config(text="Invalid input")

window = Tk()
window.title("Calculate Factorial!")
window.geometry("300x150+150+200")
window.configure(background="white")
window.resizable(False, False)

#handlers
Label1=Label(window, text='Number =', fg="black", bg="white")
calculate_button = Button(window, text="Calculate!", fg="black", bg="white", width=20, command=Calculate_Factorial)
result_label = Label(window, text='Result = ', fg="black", bg="white")
e1 = Entry(window)


#placing
Label1.place(x=20,y=20)
e1.place(x=100, y=20)
calculate_button.place(x=20, y=65)
result_label.place(x=20, y=45)

window.mainloop()
