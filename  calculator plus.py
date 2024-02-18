import tkinter

from tkinter import ttk

def renov1(event):
    stext.set(stext.get() + '1')

def getindex(r, c):
    return r * 3 + c

def getbutton(r, c, t):
    btn = ttk.Button(text = t)
    btn.bind('button-1', renov1)
    btn.grid(column = 0, row = 1)
    
prog = tkinter.Tk()
stext = tkinter.StringVar(value = '')
widtext = ttk.Entry(textvariable = stext)
widtext.grid(column = 0, row = 0)
btn1 = ttk.Button(text = '1')
btn1.bind('button-1', renov1)
btn1.grid(column = 0, row = 1)
prog.mainloop()
