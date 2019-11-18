from tkinter import *


class RootWin() :
    def __init__(self) :
        root = Tk()
        root.title("RegisterWindow")
        root.geometry('200x200')

        label_fname = Label(root, text = "First Name :")
        label_lname = Label(root, text = "Last Name :")
        label_password = Label(root, text = "password :")

        entryTextFn = StringVar()
        entryTextLn = StringVar()
        entryTextPass = StringVar()
        
        entry_boxFn=Entry(root,textvariable = entryTextFn)
        entry_boxLn=Entry(root,textvariable = entryTextLn)
        entry_boxPass=Entry(root,textvariable = entryTextPass,show = "•")

        def printInfo() :
            print("Member name : " + entry_boxFn.get() + " "+ entry_boxLn.get()+ "\n" + "Password : " + entry_boxPass.get() + " ")

        button_OK=Button(root, text ="OK" ,command = printInfo)

        label_fname.grid(row=0,column=0)
        label_lname.grid(row=1,column=0)
        label_password.grid(row=2,column=0)
        
        entry_boxFn.grid(row=0,column=1)
        entry_boxLn.grid(row=1,column=1)
        entry_boxPass.grid(row=2,column=1)

        button_OK.grid(row=3,column=1)

        root.mainloop()

Mainmenu = RootWin()