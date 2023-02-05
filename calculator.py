# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 19:50:50 2023

@author: SONAL
"""

from tkinter import *

win=Tk()
win.geometry('500x500')

e1=Entry(win,width=45,borderwidth=5)
e1.grid(row=0,column=0)

def click(no):
    result = e1.get()
    e1.delete(0,END)
    e1.insert(0,str(result)+str(no))
    
def add():
    n1 = e1.get()
    global math
    math='addition'
    global k 
    k = int(n1)
    e1.delete(0,END)

    
def sub():
    n1 = e1.get()
    global math
    math='Subtraction'
    global k 
    k = int(n1)
    e1.delete(0,END)
    
def mul():
    n1 = e1.get()
    global math
    math='Multiplication'
    global k 
    k = int(n1)
    e1.delete(0,END)
    

def div():
    n1 = e1.get()
    global math
    math='Division'
    global k 
    k = int(n1)
    e1.delete(0,END)
    

def eq():
    n2= e1.get()
    e1.delete(0,END)
    if math=='addition':
        e1.insert(0,k+int(n2))
    elif math=='Subtraction':
        e1.insert(0,k-int(n2))
    elif math=='Multiplication':
        e1.insert(0,k*int(n2))
    elif math=='Division':
        e1.insert(0,k/int(n2))


def cl():
    e1.delete(0,END)
    
    
b=Button(win,text='1',width=12,command=lambda:click(1))
b.place(x=10,y=60)


b=Button(win,text='2',width=12,command=lambda:click(2))
b.place(x=80,y=60)


b=Button(win,text='3',width=12,command=lambda:click(3))
b.place(x=170,y=60)


b=Button(win,text='4',width=12,command=lambda:click(4))
b.place(x=10,y=120)


b=Button(win,text='5',width=12,command=lambda:click(5))
b.place(x=80,y=120)

b=Button(win,text='6',width=12,command=lambda:click(6))
b.place(x=170,y=120)

b=Button(win,text='7',width=12,command=lambda:click(7))
b.place(x=10,y=180)

b=Button(win,text='8',width=12,command=lambda:click(8))
b.place(x=80,y=180)

b=Button(win,text='9',width=12,command=lambda:click(9))
b.place(x=170,y=180)

b=Button(win,text='0',width=12,command=lambda:click(0))
b.place(x=10,y=240)

b=Button(win,text='+',width=12,command=lambda:add())
b.place(x=80,y=240)

b=Button(win,text='-',width=12,command=lambda:sub())
b.place(x=170,y=240)

b=Button(win,text='/',width=12,command=lambda:div())
b.place(x=10,y=300)

b=Button(win,text='=',width=12,command=lambda:eq())
b.place(x=80,y=300)

b=Button(win,text='*',width=12,command=lambda:mul())
b.place(x=170,y=300)

b=Button(win,text='clear',width=12,command=lambda:cl())
b.place(x=10,y=350)

win.mainloop()