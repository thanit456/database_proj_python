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
            if self.entry_branch.get() == "salaya":
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
        
        header = Label(self.root, text="Main Menu")
        header.pack()
        
        ManageEmployeeButton = Button(self.root, text="Manage Employee")
        ManageEmployeeButton.pack(side=TOP)

        WarehouseButton = Button(self.root, text="Warehouse")
        WarehouseButton.pack(side=TOP)

        RentPlaceButton = Button(self.root, text="Rent Place")
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


Mainmenu = AdminWindow()