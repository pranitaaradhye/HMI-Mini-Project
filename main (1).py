import tkinter as tk
from tkinter import *
import random
import time

root = Tk()
root.geometry("1300x600+0+0")
root.title(" CHOCOLATE VENDING MACHINE ")
root.configure(bg='powder blue')
lbl_title = tk.Label(root,text="Welcome!! Enter the Quantity of Your Chocolate", bg = 'powder blue')
lbl_title.pack()

text_Input = StringVar()
operator = ""

#==================================Setting the Frame=======================================


Tops = Frame(root, width=1600, height=50, bg="powder blue", relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=1200, height=700, bg="powder blue", relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width=300, height=700, bg="powder blue",relief=SUNKEN)
f2.pack(side=RIGHT)

#==================================Time=======================================

localtime = time.asctime(time.localtime(time.time()))

#==================================System Information=======================================

lblInfo = Label(Tops, font=('Algerian', 40, 'bold'), text="BARS OF BLISS", fg="Steel Blue", bd=10, anchor='w')
lblInfo.grid(row=0, column=0)

lblInfo = Label(Tops, font=('Algerian', 20), text=localtime, fg="Steel Blue",
                bd=10, anchor='w')
lblInfo.grid(row=1, column=0)

def Total():
    AmtOfTwix = (float(Twix.get()))
    AmtOfSnickers = (float(Snickers.get()))
    AmtOfMarsBar = (float(MarsBar.get()))
    AmtOfGodiva = (float(Godiva.get()))

    CostOfTwix = AmtOfTwix * 10.0
    CostOfSnickers = AmtOfSnickers * 20.0
    CostOfMarsBar = AmtOfMarsBar * 30.0
    CostOfGodiva = AmtOfGodiva * 40.0

    CostOfMeal = ("INR" + str('%.2f'% (CostOfTwix + CostOfSnickers + CostOfMarsBar + CostOfGodiva)))
    txtCost.insert(0, CostOfMeal)

def ShowPaid():
    root.destroy()




def qExit():
    root.destroy()
def Reset():
    Twix.set(0)
    Snickers.set(0)
    MarsBar.set(0)
    Godiva.set(0)
    InitialBalance.set(0)
    Cost.set(0)
    FinalBalance.set(0)

#-------------------

Twix=DoubleVar()
Snickers=DoubleVar()
MarsBar=DoubleVar()
Godiva=DoubleVar()

lblTwix = Label(f1, font=('Cambria', 16, 'bold'), text='Twix',bg = 'powder blue',bd=19,anchor='w')
lblTwix.grid(row=2,column=0)
txtTwix = Entry(f1,font=('Cambria',16,'bold'),textvariable=Twix,bd=10,insertwidth=4,
                bg='powder blue',justify='right')
txtTwix.grid(row=2,column=1)

lblSnickers = Label(f1, font=('Cambria', 16, 'bold'), text='Snickers', bg = 'powder blue',bd=19,anchor='w')
lblSnickers.grid(row=4,column=0)
txtSnickers = Entry(f1,font=('Cambria',16,'bold'),textvariable=Snickers,bd=10,insertwidth=4,
                bg='powder blue',justify='right')
txtSnickers.grid(row=4,column=1)

lblSnickers = Label(f1, font=('arial', 16, 'bold'), text='Snickers', bg = 'powder blue',bd=19,anchor='w')
lblSnickers.grid(row=4,column=0)
txtSnickers = Entry(f1,font=('arial',16,'bold'),textvariable=Snickers,bd=10,insertwidth=4,
                bg='powder blue',justify='right')
txtSnickers.grid(row=4,column=1)

lblMarsBar = Label(f1, font=('arial', 16, 'bold'), text='Mars Bar', bg = 'powder blue',bd=19,anchor='w')
lblMarsBar.grid(row=6,column=0)
txtMarsBar = Entry(f1,font=('arial',16,'bold'),textvariable=MarsBar,bd=10,insertwidth=4,
                bg='powder blue',justify='right')
txtMarsBar.grid(row=6,column=1)

lblGodiva = Label(f1,font=('arial',16,'bold'), text="Godiva", bg = 'powder blue',bd=19, anchor='w')
lblGodiva.grid(row=9, column=0)
txtGodiva = Entry(f1,font=('arial',16,'bold'),textvariable=Godiva,bd=10,insertwidth=4,
                bg='powder blue',justify='right')
txtGodiva.grid(row=9,column=1)


#==================================Balance, Cost=======================================

InitialBalance=DoubleVar()
Cost=DoubleVar()
FinalBalance=DoubleVar()
Pay=DoubleVar()

##lblInitialBalance.grid(row=2, column=10)
##txtInitialBalance=Entry(f1,font=('arial',20,'bold'), textvariable=InitialBalance, bd=28, insertwidth=4,
                 ##  bg='powder blue', justify='right')
##txtInitialBalance.grid(row=2, column=12)

lblCost = Label(f1,font=('arial',20,'bold'), text="Total Cost", bg = 'powder blue',bd=29, anchor='w')
lblCost.grid(row=4, column=10)
txtCost=Entry(f1,font=('arial',20,'bold'), textvariable=Cost, bd=28, insertwidth=4,
                   bg='powder blue', justify='right')
txtCost.grid(row=4, column=12)

##lblFinalBalance = Label(f1,font=('arial',20,'bold'), text="Final Balance", bg = 'powder blue',bd=29, anchor='w')
##lblFinalBalance.grid(row=6, column=10)
##txtFinalBalance=Entry(f1,font=('arial',20,'bold'), textvariable=FinalBalance, bd=28, insertwidth=4,
                  ## bg='powder blue', justify='right')
##txtFinalBalance.grid(row=6, column=12)

#==================================More Buttons=======================================

btnTotal = Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',20,'bold'),width=6,text="Total",bg="green",
                  command=Total).grid(row=12,column=5)

btnReset = Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',20,'bold'),width=6,text="Reset",bg="yellow",
                  command=Reset).grid(row=12,column=6)

btnExit = Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',20,'bold'),width=6,text="Exit",bg="red",
                  command=qExit).grid(row=12,column=7)
btnPay = Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',20,'bold'),width=6,text="Pay",bg="orange",
                  command=ShowPaid).grid(row=10,column=12)

#--------------------------------------------------------------

root.mainloop()