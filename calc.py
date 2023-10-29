from tkinter import *

equation = ""
def ToEquation(num):
    global equation

    equation = equation + num
    label.config(text=equation)

def Equals():

    global equation
    try:
        result = eval(equation)
        if result % 1 == 0:
            label.config(text=int(result))
            equation = str(int(result))
        else:
            label.config(text=result)
            equation = str(result)
    except ZeroDivisionError:
        label.config(text="Don't divide by 0")
        equation = ""
    except SyntaxError:
        label.config(text="syntax error")
        equation = ""
def ClearEquation():

    global equation
    equation = ""
    label.config(text=equation)

def BackspaceEquation():

    global equation
    equation = equation[:-1]
    label.config(text=equation)

window = Tk()
window.config(height=500, width=500)
window.resizable(height=False, width=False)

label = Label(window, font=('Arial',20), bg='white',borderwidth=2, relief='groove',width=20, height=3)
label.pack()

frame = Frame(window)
frame.pack()
button1 = Button(frame, text="1", height=5,width=10, command=lambda: ToEquation("1")).grid(row=0,column=0)
button2 = Button(frame, text="2",height=5,width=10,command=lambda: ToEquation("2")).grid(row=0,column=1)
button3 = Button(frame, text="3",height=5,width=10, command=lambda: ToEquation("3")).grid(row=0,column=2)
button_plus = Button(frame, text="+",height=5,width=10, command=lambda: ToEquation("+")).grid(row=0,column=3)
button4 = Button(frame, text="4",height=5,width=10, command=lambda: ToEquation("4")).grid(row=1,column=0)
button5 = Button(frame, text="5",height=5,width=10, command=lambda: ToEquation("5")).grid(row=1,column=1)
button6 = Button(frame, text="6",height=5,width=10, command=lambda: ToEquation("6")).grid(row=1,column=2)
button_minus = Button(frame, text="-",height=5,width=10, command=lambda: ToEquation("-")).grid(row=1,column=3)
button7 = Button(frame, text="7",height=5,width=10, command=lambda: ToEquation("7")).grid(row=2,column=0)
button8 = Button(frame, text="8",height=5,width=10, command=lambda: ToEquation("8")).grid(row=2,column=1)
button9 = Button(frame, text="9",height=5,width=10, command=lambda: ToEquation("9")).grid(row=2,column=2)
button_multiply = Button(frame, text="*",height=5,width=10, command=lambda: ToEquation("*")).grid(row=2,column=3)
button0 = Button(frame, text="0",height=5,width=10, command=lambda: ToEquation("0")).grid(row=3,column=0)
button_coma = Button(frame, text=".",height=5,width=10, command=lambda: ToEquation(".")).grid(row=3,column=1)
button_equals = Button(frame, text="=",height=5,width=10, command=Equals).grid(row=3,column=2)
button_divide = Button(frame, text="/",height=5,width=10, command=lambda: ToEquation("/")).grid(row=3,column=3)
button_clear = Button(frame, text="C",height=5,width=22, command=ClearEquation).grid(row=4,column=0,columnspan=2)
button_backspace = Button(frame, text="BACKSPACE",height=5,width=22, command=BackspaceEquation).grid(row=4,column=2,columnspan=2)

window.mainloop()