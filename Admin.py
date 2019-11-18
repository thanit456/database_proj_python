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

        def BranchDetailPop() :
            self.root.destroy()
            bd = BranchDetailWin()

        def RentPlacePop():
            self.root.destroy()
            rp = RentPlaceWin()

        def PromotionPop():
            self.root.destroy()
            pm = PromotionWin()
        
        header = Label(self.root, text="Main Menu")
        header.pack()
        
        ManageEmployeeButton = Button(self.root, text="Manage Employee")
        ManageEmployeeButton.pack(side=TOP)

        WarehouseButton = Button(self.root, text="Warehouse")
        WarehouseButton.pack(side=TOP)

        RentPlaceButton = Button(self.root, text="Rent Place", command=RentPlacePop)
        RentPlaceButton.pack(side=TOP)

        PromotionButton = Button(self.root, text="Promotion", command=PromotionPop)
        PromotionButton.pack(side=TOP)

        BranchDetail = Button(self.root, text="Branch Detail", command=BranchDetailPop)
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
            tempList = [ ['-','-'], 
                        ['Rented','123344'], 
                        ['-','-'], 
                        ['Rented','47261'] ]
            #tempList.sort(key=lambda e: e[1], reverse=True)

            for i, (status, owner) in enumerate(tempList, start=1):
                tree.insert("", "end", values=(i, status, owner))
                

        #scores = tk.Tk() 
        label = tk.Label(self.root, text="Rent Place", font=("Arial",30)).grid(row=0, columnspan=3)
        # create Treeview with 3 columns
        cols = ('Rent Place ID', 'status', 'Owner', 'Fname', 'Lname', 'Phone', 'start', 'expire', 'cost')
        tree = ttk.Treeview(self.root, columns=cols, show='headings',padding=30)
        # set column headings
        for col in cols:
            tree.column(col,width=100,stretch=NO)
            tree.heading(col,text=col)
            
        tree.grid(row=1, column=0, columnspan=2)

        showDetail = tk.Button(self.root, text="Show Detail", width=15, command=show).grid(row=4, column=0)
        BackButton = tk.Button(self.root, text="Back", width=15, command=returnToMenu).grid(row=4, column=1)


        self.root.mainloop()

class BranchDetailWin():
    def __init__ (self):
        self.root = tk.Tk()
        self.root.title("Branch Detail")
        self.root.geometry('300x200')

        self.label_BranchId = Label(self.root,text="Branch ID :")
        self.label__db_BranchId = Label(self.root,text=("...."*5))
        self.label_Name = Label(self.root,text="Name :")
        self.label_db_Name = Label(self.root,text="......")

        self.label_Address = Label(self.root,text="Address :")
        self.label_db_Address = Label(self.root,text="......")
        self.label_Phone = Label(self.root,text="Phone :")
        self.label_db_Phone = Label(self.root,text="......")

        self.label_Manager = Label(self.root,text="Manager :")
        self.label_db_Manager = Label(self.root,text="......")
        self.label_Start = Label(self.root,text="Start Date :")
        self.label_db_Start = Label(self.root,text="......")

        def backToMenu() :
            self.root.destroy()
            m1 = MenuWin()

        self.button_back = Button(self.root,text="Back",command=backToMenu)
        
        self.label_BranchId.grid(row=0,column=0)
        self.label__db_BranchId.grid(row=0,column=1)
        self.label_Name.grid(row=1,column=0)
        self.label_db_Name.grid(row=1,column=1)

        self.label_Address.grid(row=2,column=0)
        self.label_db_Address.grid(row=2,column=1)
        self.label_Phone.grid(row=3,column=0)
        self.label_db_Phone.grid(row=3,column=1)

        self.label_Manager.grid(row=4,column=0)
        self.label_db_Manager.grid(row=4,column=1)
        self.label_Start.grid(row=5,column=0)
        self.label_db_Start.grid(row=5,column=1)

        self.button_back.grid(row=6,column=1)

        self.root.mainloop()

class PromotionWin():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Promotion")
        self.root.geometry('400x300')

        def backToMenu() :
            self.root.destroy()
            m1 = MenuWin()

        def addPromotion():
            ap = AddPromotionWin()

        def editPromotion():
            ep = EditPromotionWin()
        
        def searchPromotion():
            sp = SearchPromotionWin()

        header = Label(self.root, text="Promotion")
        header.pack()
        
        AddButton = Button(self.root, text="ADD",command=addPromotion)
        AddButton.pack(side=TOP)

        EditButton = Button(self.root,text="Edit",command=editPromotion)
        EditButton.pack(side=TOP)

        SearchButton = Button(self.root, text="Search",command=searchPromotion)
        SearchButton.pack(side=TOP)

        BackButton = Button(self.root, text="Back",command=backToMenu)
        BackButton.pack(side=TOP)

        self.root.mainloop()

class AddPromotionWin() :
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Add Promotion")
        self.root.geometry('460x200')

        self.entryText1 =  StringVar()
        self.entryText1.set("")
        self.entryText2 =  StringVar()
        self.entryText2.set("")
        self.entryText3 =  StringVar()
        self.entryText3.set("")
        self.entryText4 =  StringVar()
        self.entryText4.set("")
        self.entryText5 =  StringVar()
        self.entryText5.set("")

        self.label_product = Label(self.root,text="Product ID :")
        self.label_start = Label(self.root,text="Start Date :")
        self.label_end = Label(self.root,text="End Date :")
        self.label_discount = Label(self.root,text="Discount :")
        self.label_mem_point = Label(self.root,text="Member point :")

        self.entry_product = Entry(self.root,textvariable=self.entryText1)
        self.entry_start = Entry(self.root,textvariable=self.entryText2)
        self.entry_end = Entry(self.root,textvariable=self.entryText3)
        self.entry_discount = Entry(self.root,textvariable=self.entryText4)
        self.entry_mem_point = Entry(self.root,textvariable=self.entryText5)

        self.button_ADD = Button(self.root,text="ADD")

        self.label_product.grid(row=0,column=0)
        self.entry_product.grid(row=0,column=1)
        self.label_start.grid(row=1,column=0)
        self.entry_start.grid(row=1,column=1)
        self.label_end.grid(row=1,column=2)
        self.entry_end.grid(row=1,column=3)
        self.label_discount.grid(row=2,column=0)
        self.entry_discount.grid(row=2,column=1)
        self.label_mem_point.grid(row=2,column=2)
        self.entry_mem_point.grid(row=2,column=3)

        self.button_ADD.grid(row=3,column=1)

        self.root.mainloop()

class EditPromotionWin() :
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Edit Promotion")
        self.root.geometry('300x150')

        self.entryText1 =  StringVar()
        self.entryText1.set("")

        self.label_promotion = Label(self.root,text="Promotion ID :")
        self.entry_promotion = Entry(self.root,textvariable=self.entryText1)
        self.label_promotion.grid(row=0,column=0)
        self.entry_promotion.grid(row=0,column=1)
        self.button_delete = Button(self.root,text="Delete")
        self.button_delete.grid(row=2,column=1)

        self.root.mainloop()

class SearchPromotionWin():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Search Promotion')

        def show():
            tempList = [ ['-','-'], 
                        ['1232','123344'], 
                        ['-','-'], 
                        ['42232','47261'] ]
            #tempList.sort(key=lambda e: e[1], reverse=True)

            for i, (start, end) in enumerate(tempList, start=1):
                tree.insert("", "end", values=(i, start, end))
                

        #scores = tk.Tk() 
        label = tk.Label(self.root, text="Promotion", font=("Arial",24)).grid(row=0, columnspan=3)
        # create Treeview with 3 columns
        cols = ('Promotion ID', 'Start Date', 'End Date', 'Discount', 'Member Point')
        tree = ttk.Treeview(self.root, columns=cols, show='headings',padding=30)
        # set column headings
        for col in cols:
            tree.column(col,width=100,stretch=NO)
            tree.heading(col,text=col)
            
        tree.grid(row=1, column=0, columnspan=2)

        showDetail = tk.Button(self.root, text="Show Detail", width=15, command=show).grid(row=4, column=0)
        closeButton = tk.Button(self.root, text="Close", width=15, command=exit).grid(row=4, column=1)


        self.root.mainloop()

Mainmenu = AdminWindow()