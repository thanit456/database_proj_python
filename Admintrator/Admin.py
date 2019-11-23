import sys
import tkinter as tk
from tkinter import ttk
from tkinter import *

from db_promotion_management  import *

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
        self.label_db_BranchId = Label(self.root,text=("...."*5))
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
        self.label_db_BranchId.grid(row=0,column=1)
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
            ep = EditOrDeletePromotionWin()
        
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

        self.text_product_id =  StringVar()
        self.text_product_id.set("")
        self.text_start_date =  StringVar()
        self.text_start_date.set("")
        self.text_end_date =  StringVar()
        self.text_end_date.set("")
        self.text_percentage =  StringVar()
        self.text_percentage.set("")
        self.text_mempoint =  StringVar()
        self.text_mempoint.set("")

        self.label_product = Label(self.root,text="Product ID :")
        self.label_start = Label(self.root,text="Start Date :")
        self.label_end = Label(self.root,text="End Date :")
        self.label_percentage = Label(self.root,text="Discount :")
        self.label_mempoint = Label(self.root,text="Member point :")

        self.entry_product_id = Entry(self.root,textvariable=self.text_product_id)
        self.entry_start_date = Entry(self.root,textvariable=self.text_start_date)
        self.entry_end_date = Entry(self.root,textvariable=self.text_end_date)
        self.entry_percentage = Entry(self.root,textvariable=self.text_percentage)
        self.entry_mempoint = Entry(self.root,textvariable=self.text_mempoint)

        self.button_ADD = Button(self.root,text="Submit")

        self.label_product.grid(row=0,column=0)
        self.entry_product_id.grid(row=0,column=1)
        self.label_start.grid(row=1,column=0)
        self.entry_start_date.grid(row=1,column=1)
        self.label_end.grid(row=1,column=2)
        self.entry_end_date.grid(row=1,column=3)
        self.label_percentage.grid(row=2,column=0)
        self.entry_percentage.grid(row=2,column=1)
        self.label_mempoint.grid(row=2,column=2)
        self.entry_mempoint.grid(row=2,column=3)

        self.button_ADD.grid(row=3,column=1)

        self.button_ADD.configure(command=self.submitNewPromotion)
        self.root.mainloop()

    def submitNewPromotion(self):
        # self.cwin.title("Submitted")
        dataentry = [
                    self.entry_start_date.get(), 
                    self.entry_end_date.get(), 
                    self.entry_percentage.get(),
                    self.entry_mempoint.get(), 
                    self.entry_product_id.get()
                    ]
        print('Entry: ',dataentry)
        aPromotion = Promotion(dataentry)
        retmsg = aPromotion.write()
        # self.label_status.config(text=retmsg[1])

    
class EditOrDeletePromotionWin() :
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
        self.button_edit = Button(self.root, text="Edit", command=self.goEditPromotion)
        self.button_edit.grid(row=2, column=1)
        self.button_delete = Button(self.root,text="Delete")
        self.button_delete.grid(row=3,column=1)
        

        self.root.mainloop()
    def deletePromotionByID(self):
        dataentry = [self.entry_promotion.get()]


    def goEditPromotion(self):
        editwin = EditPromotionWin(self.entry_promotion.get())
    # # self.cwin.title("Submitted")
    #     dataentry = [self.entry_promotion.get()]
    #     aPromotion = Promotion(dataentry)
    #     retmsg = aPromotion.write()
        
        # self.label_status.config(text=retmsg[1])
class EditPromotionWin() :
    def __init__(self, promotion_id):
        self.root = tk.Tk()
        self.root.title("Edit Promotion")
        self.root.geometry('600x200')

        self.promotion_id = promotion_id

        self.text_product_id =  StringVar()
        self.text_product_id.set("")
        self.text_start_date =  StringVar()
        self.text_start_date.set("")
        self.text_end_date =  StringVar()
        self.text_end_date.set("")
        self.text_percentage =  StringVar()
        self.text_percentage.set("")
        self.text_mempoint =  StringVar()
        self.text_mempoint.set("")

        self.label_product = Label(self.root,text="Product ID :")
        self.label_start = Label(self.root,text="Start Date :")
        self.label_end = Label(self.root,text="End Date :")
        self.label_percentage = Label(self.root,text="Discount :")
        self.label_mempoint = Label(self.root,text="Member point :")

        self.entry_product_id = Entry(self.root,textvariable=self.text_product_id)
        self.entry_start_date = Entry(self.root,textvariable=self.text_start_date)
        self.entry_end_date = Entry(self.root,textvariable=self.text_end_date)
        self.entry_percentage = Entry(self.root,textvariable=self.text_percentage)
        self.entry_mempoint = Entry(self.root,textvariable=self.text_mempoint)

        self.button_EDIT = Button(self.root,text="Submit")

        self.label_product.grid(row=0,column=0)
        self.entry_product_id.grid(row=0,column=1)
        self.label_start.grid(row=1,column=0)
        self.entry_start_date.grid(row=1,column=1)
        self.label_end.grid(row=1,column=2)
        self.entry_end_date.grid(row=1,column=3)
        self.label_percentage.grid(row=2,column=0)
        self.entry_percentage.grid(row=2,column=1)
        self.label_mempoint.grid(row=2,column=2)
        self.entry_mempoint.grid(row=2,column=3)

        self.button_EDIT.grid(row=3,column=2)

        self.button_EDIT.configure(command=self.submitEditPromotion)
        self.root.mainloop()

    def submitEditPromotion(self):
        # self.cwin.title("Submitted")
        dataentry = [
                    self.promotion_id,
                    self.entry_start_date.get(), 
                    self.entry_end_date.get(), 
                    self.entry_percentage.get(),
                    self.entry_mempoint.get(), 
                    self.entry_product_id.get()
                    ]
        aPromotion = Promotion(dataentry)
        retmsg = aPromotion.edit()
        # self.label_status.config(text=retmsg[1])

    
class SearchPromotionWin():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Search Promotion')
        self.root.geometry('720x460')
        
        self.text_promotion = StringVar()
        self.text_promotion.set("")
        self.text_product_id =  StringVar()
        self.text_product_id.set("")

        self.label_promotion = Label(self.root, text="Promotion ID :")
        self.label_product = Label(self.root,text="Product ID :")
        self.entry_promotion = Entry(self.root,textvariable=self.text_promotion)
        self.entry_product_id = Entry(self.root,textvariable=self.text_product_id)

        self.label_promotion.place(x=50,y=70)
        self.entry_promotion.place(x=140,y=70)
        self.label_product.place(x=400,y=70)
        self.entry_product_id.place(x=475,y=70)

        

        def show():
            self.queryList = self.queryPromotion()
            leaf_nodes = tree.get_children()
            for i in leaf_nodes:
                tree.delete(i)
            for promotionid, startdate, enddate, percent, mempoint, productid in self.queryList:
                tree.insert("", "end", values=(promotionid, startdate, enddate, percent, mempoint, productid))
                

        label = tk.Label(self.root, text="Promotion", font=("Arial",24))
        label.place(x=280,y=10)
        # create Treeview with 3 columns
        cols = ('Promotion ID', 'Start Date', 'End Date', 'Discount', 'Member Point', 'ProductID')
        tree = ttk.Treeview(self.root, columns=cols, show='headings',padding=20)
        # set column headings
        for col in cols:
            tree.column(col,width=100,stretch=NO)
            tree.heading(col,text=col)
        tree.place(x=30,y=100,width=660, height=300)

        showDetail = tk.Button(self.root, text="Show Detail", width=15, command=show)
        showDetail.place(x=140,y=420)
        closeButton = tk.Button(self.root, text="Close", width=15, command=exit)
        closeButton.place(x=420,y=420)


        self.root.mainloop()
    def queryPromotion(self):
    # self.cwin.title("Submitted")
        dataentry = [
            self.entry_promotion.get(),
            self.entry_product_id.get()
        ]
        aPromotion = Promotion(dataentry)
        return aPromotion.showTable()
        
    

Mainmenu = SearchPromotionWin()