
import math
from tkinter import *
from turtle import width
root = Tk()
root.title('simple calculator')

e = Entry(root,width=35,borderwidth=5,font='lucida 10 bold')
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
 

def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))

def button_clear():
    e.delete(0,END)
    
def button_equal():
    second_num=e.get()
    e.delete(0,END)
    if math == 'add':
        e.insert(0,fnum + int(second_num))
    if math == 'multiply':
        e.insert(0,fnum*int(second_num))
    if math == 'division':
        e.insert(0,fnum/int(second_num))
    if math == 'subtract':
        e.insert(0,fnum-int(second_num))
    
    



def button_add():
    first_num=e.get()
    global fnum
    global math
    math="add"
    fnum=int(first_num)
    e.delete(0,END)

def button_multiply():
    first_num=e.get()
    global fnum
    global math
    math="multiply"
    fnum=int(first_num)
    e.delete(0,END)

def button_subtract():
    first_num=e.get()
    global fnum
    global math
    math="subtract"
    fnum=int(first_num)
    e.delete(0,END)

def button_division():
    first_num=e.get()
    global fnum
    global math
    math="division"
    fnum=int(first_num)
    e.delete(0,END)



# creating the calculators buttons 
button1= Button(root,text=1,padx=40,pady=20,fg = 'grey',command=lambda:button_click(1))
button2= Button(root,text=2,padx=40,pady=20,fg = 'grey',command=lambda:button_click(2))
button3= Button(root,text=3,padx=40,pady=20,fg = 'grey',command=lambda:button_click(3))
button4= Button(root,text=4,padx=40,pady=20,fg = 'grey',command=lambda:button_click(4))
button5= Button(root,text=5,padx=40,pady=20,fg = 'grey',command=lambda:button_click(5))
button6= Button(root,text=6,padx=40,pady=20,fg = 'grey',command=lambda:button_click(6))
button7= Button(root,text=7,padx=40,pady=20,fg = 'grey',command=lambda:button_click(7))
button8= Button(root,text=8,padx=40,pady=20,fg = 'grey',command=lambda:button_click(8))
button9= Button(root,text=9,padx=40,pady=20,fg = 'grey',command=lambda:button_click(9))
button0=Button(root,text=0,padx=40,pady=20,fg = 'grey',command=lambda:button_click(0))
button_add = Button(root,text="+",padx=40,pady=20,fg = 'brown',command=button_add)
button_clear = Button(root,text="clear",padx=91,pady=20,fg = 'brown',command=button_clear)
button_equal = Button(root,text="=",padx=79,pady=20,fg = 'brown',command=button_equal)


button_multiply = Button(root,text='X',padx=40,pady=20,fg = 'brown',command=button_multiply)
button_division= Button(root,text='%',padx=79,pady=20,fg = 'brown',command=button_division)
button_subtract = Button(root,text='-',padx=40,pady=20,fg = 'brown',command=button_subtract)


# putting the buttons on the screen
# putting these button in down
button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
# putting these button in the middle
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

# putting thses button on top 
button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)


button0.grid(row=4,column=0)

button_add.grid(row=5,column=0)
button_clear.grid(row=4,column=1,columnspan=2)
button_equal.grid(row=5,column=1,columnspan=2)


button_multiply.grid(row=6,column=0)
button_division.grid(row=6,column=1,columnspan=2)
button_subtract.grid(row=7,column=0)










root.mainloop()