from tkinter import *

class RootWin() :
    def __init__(self) :
           
        root = Tk()
        root.title("ThankWindow")
        root.geometry('200x150+100+100')

        label_thank = Label(root,text = "THANK YOU",font = "Times 14",foreground="red")

        button_home = Button(root,text = "home",command = self.backToHome)

        label_thank.pack()
        button_home.pack()
        root.mainloop()

    def backToHome(self) :
            print("home")
Mainmenu = RootWin()