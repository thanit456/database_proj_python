import sys
import tkinter as tk
from tkinter import ttk
from tkinter import *

class AdminWindow() :
    def __init__ (self):
        self.cwin = Tk()
        self.cwin.title("Admin")
        self.cwin.geometry('210x80')

        self.entryText1 =  StringVar()
        self.entryText1.set("")

        self.label_branch = Label(self.cwin,text="Branch :")

        self.entry_branch = Entry(self.cwin,textvariable=self.entryText1)
            
        #for testing only need to send memberID to next step
        #for testing username = 'member' password = 'member' to login
        def login():
            if self.entry_branch.get() == "":
                self.cwin.destroy()
                m1 = MenuWin()

        self.button_ok = Button(self.cwin,text="Ok",command=login) # need to change to real login compare from database

        self.label_branch.grid(row=0,column=0)
        self.entry_branch.grid(row=0,column=1)
        self.button_ok.grid(row=2,column=1)
        self.cwin.mainloop()

class MenuWin() :
    def __init__ (self):
        self.root = Tk()
        self.root.title("Admin Main Menu")
        self.root.geometry('400x300')

        def BranchDetailWin() :
            self.root.destroy()

        def RentPlacePop():
            self.root.destroy()
            rp = RentPlaceWin()
        
        header = Label(self.root, text="Main Menu")
        header.pack()
        
        ManageEmployeeButton = Button(self.root, text="Manage Employee")
        ManageEmployeeButton.pack(side=TOP)

        WarehouseButton = Button(self.root, text="Warehouse")
        WarehouseButton.pack(side=TOP)

        RentPlaceButton = Button(self.root, text="Rent Place", command=RentPlacePop)
        RentPlaceButton.pack(side=TOP)

        PromotionButton = Button(self.root, text="Promotion")
        PromotionButton.pack(side=TOP)

        BranchDetail = Button(self.root, text="Branch Detail", command=BranchDetailWin)
        BranchDetail.pack(side=TOP)

        OrderButton = Button(self.root, text="Order")
        OrderButton.pack(side=TOP)

        BackButton = Button(self.root, text="Back")
        BackButton.pack(side=TOP)



        self.root.mainloop()

class RentPlaceWin():
    def __init__ (self):
        self.root = tk.Tk()
        self.root.title("Rent Place")
        #self.root.geometry('700x350')

        def returnToMenu():
            self.root.destroy()
            mn = MenuWin()

        def show():
            tempList = [['rent', '0.72'], ['-', '0.67'], ['-', '0.67'], ['-', '0.5']]
            #tempList.sort(key=lambda e: e[1], reverse=True)

            for i, (name, score) in enumerate(tempList, start=1):
                listBox.insert("", "end", values=(i, name, score))
                

        #scores = tk.Tk() 
        label = tk.Label(self.root, text="Rent Place", font=("Arial",30)).grid(row=0, columnspan=3)
        # create Treeview with 3 columns
        cols = ('Rent Place ID', 'status', 'ID', 'Fname', 'Lname', 'Phone', 'start', 'expire', 'cost')
        listBox = ttk.Treeview(self.root, columns=cols, show='headings')
        # set column headings
        for col in cols:
            listBox.heading(col, text=col)
        listBox.grid(row=1, column=0, columnspan=2)

        showScores = tk.Button(self.root, text="Show scores", width=15, command=show).grid(row=4, column=0)
        BackButton = tk.Button(self.root, text="Back", width=15, command=returnToMenu).grid(row=4, column=1)


        self.root.mainloop()





Mainmenu = AdminWindow()