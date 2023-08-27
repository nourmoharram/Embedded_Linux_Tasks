'''
Task description : 
● Create a graphical application in Python Tkinter that asks
the user to enter two integers and displays their sum
'''

from tkinter import *

result = 1

def Sum():
    global result
    try:
        number1 = int(e1.get())
        number2 = int(e2.get())
        result = number1+number2

        result_label.config(text=f"Result = {number1} + {number2} = {result}")
    except ValueError:
        result_label.config(text="Invalid input")

#window Init
window = Tk()
window.title("Calculate Factorial!")
window.geometry("500x150+150+200")
window.configure(background="white")
window.resizable(False, False)



#handlers
Label1=Label(window, text='Enter the Value of NO1 =', fg="black", bg="white")
Label2=Label(window, text='Enter the value of NO2 =', fg="black", bg="white")
result_label = Label(window, text='The sum  = ', fg="black", bg="white")
calculate_button = Button(window, text="Calculate!", fg="black", bg="white", width=20, command=Sum)
e1 = Entry(window)
e2 = Entry(window)

#placing
calculate_button.place(x=20, y=75)
Label1.place(x=20,y=20)
Label2.place(x=20,y=45)
result_label.place(x=180,y=75)
e1.place(x=160, y=20)
e2.place(x=160, y=45)

window.mainloop()
