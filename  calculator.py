import tkinter

from tkinter import ttk

def renov1(event):
    stext.set(stext.get() + '1')
    print('DB' + stext.get())

def renov2(event):
    stext.set(stext.get() + '2')
    print('DB' + stext.get())

def renov3(event):
    stext.set(stext.get() + '3')
    print('DB' + stext.get())  

def renov4(event):
    stext.set(stext.get() + '4')
    print('DB' + stext.get())  

def renov5(event):
    stext.set(stext.get() + '5')  
    print('DB' + stext.get())

def renov6(event):
    stext.set(stext.get() + '6')  
    print('DB' + stext.get())

def renov7(event):
    stext.set(stext.get() + '7')  
    print('DB' + stext.get())

def renov8(event):
    stext.set(stext.get() + '8')  
    print('DB' + stext.get())

def renov9(event):
    stext.set(stext.get() + '9')  
    print('DB' + stext.get())

def renov0(event):
    stext.set(stext.get() + '0')  
    print('DB' + stext.get())

def renovP(event):
    stext.set(stext.get() + '.')  
    print('DB' + stext.get())

def renovB(event):
    stext.set(stext.get() [:-1])  
    print('DB' + stext.get())

def renov_pm(event):
    s = stext.get()
    if s.startswith('-'):
        s = s[1:]
    else:
        s = '-' + s
        stext.set(s)
    print('DB' + stext.get())

LEFT_CLICK = '<Button-1>'

prog = tkinter.Tk()
stext = tkinter.StringVar(value = '')
widtext = ttk.Entry(textvariable = stext)
widtext.grid(column = 0, row = 0, columnspan = 3)

btn1 = ttk.Button(text = '1')
btn1.bind(LEFT_CLICK, renov1)
btn1.grid(column = 0, row = 1)

btn2 = ttk.Button(text = '2')
btn2.bind(LEFT_CLICK, renov2)
btn2.grid(column = 1, row = 1)

btn3 = ttk.Button(text = '3')
btn3.bind(LEFT_CLICK, renov3)
btn3.grid(column = 2, row = 1)

btn4 = ttk.Button(text = '4')
btn4.bind(LEFT_CLICK, renov4)
btn4.grid(column = 0, row = 2)

btn5 = ttk.Button(text = '5')
btn5.bind(LEFT_CLICK, renov5)
btn5.grid(column = 1, row = 2)

btn6 = ttk.Button(text = '6')
btn6.bind(LEFT_CLICK, renov6)
btn6.grid(column = 2, row = 2)

btn7 = ttk.Button(text = '7')
btn7.bind(LEFT_CLICK, renov7)
btn7.grid(column = 0, row = 3)

btn8 = ttk.Button(text = '8')
btn8.bind(LEFT_CLICK, renov8)
btn8.grid(column = 1, row = 3)

btn9 = ttk.Button(text = '9')
btn9.bind(LEFT_CLICK, renov9)
btn9.grid(column = 2, row = 3)

btn0 = ttk.Button(text = '0')
btn0.bind(LEFT_CLICK, renov0)
btn0.grid(column = 1, row = 4)

btnP = ttk.Button(text = '.')
btnP.bind(LEFT_CLICK, renovP)
btnP.grid(column = 2, row = 4)

btnB = ttk.Button(text = '<-')
btnB.bind(LEFT_CLICK, renovB)
btnB.grid(column = 3, row = 1)

btn_pm = ttk.Button(text='-/+')
btn_pm.bind(LEFT_CLICK, renov_pm)
btn_pm.grid(column=0, row=4)

prog.mainloop()