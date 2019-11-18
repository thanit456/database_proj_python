from tkinter import *


class RootWin() :
    def __init__(self) :
        root = Tk()
        root.title("BuyProduct")
        root.geometry('250x250')

        name = "name of product"
        price = 5

        label_name = Label(root,text = name)
        label_price = Label(root,text = price)
        label_bath = Label(root,text = "bath")

        entryTextPrice = StringVar()
        entryTextPrice.set(str(price))
        entryTextBox = Entry(root,textvariable=entryTextPrice)

        def minus() :
            x = int(entryTextPrice.get())
            entryTextPrice.set(str(x-price))
        def plus() :
            x = int(entryTextPrice.get())
            entryTextPrice.set(str(x+price))

        button_minus = Button(root,text = "-",command = minus)
        button_plus = Button(root,text = "+",command = plus)


        label_name.grid(row=0,column =0)
        label_price.grid(row=0,column =1)
        label_bath.grid(row=0,column =2)
    
        button_minus.grid(row=1,column =0)
        entryTextBox.grid(row=1,column =1)
        button_plus.grid(row=1,column =2)

        root.mainloop()

Mainmenu = RootWin()