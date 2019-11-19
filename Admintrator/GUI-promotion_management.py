from tkinter import *
from db_promotion_management import *

class RootWin() :
    def __init__(self) :
        root = Tk()
        
        header = Label(root, text="Promotion management")
        header.pack()
        
        addButton = Button(root, text="Add New Promotion", command=self.popAddWin)
        addButton.pack(side=TOP)
        searchButton = Button(root, text="Search by Promotion ID", command=self.popSearchWin)
        searchButton.pack(side=TOP)
        searchNameButton = Button(root, text="Search by Product Name", command=self.popSearchNameWin)
        searchNameButton.pack(side=TOP)
        exitButton = Button(root, text="Exit", command=self.exitProgram)
        exitButton.pack(side=BOTTOM)
        deleteButton = Button(root, text="Delete by Promotion ID", command=self.popDeleteWin)
        deleteButton.pack(side=TOP)
        root.geometry('200x150+100+100')
        root.mainloop()
        
    def popAddWin(self) :
        r1 = RegisterWin("Promotion Registration")
    def popSearchWin(self) :
        s1 = SearchWin("Promotion Search")
    def popSearchNameWin(self) :
        s1 = SearchNameWin("Search by Product Name")
    def exitProgram(self) :
        exit()
    def popDeleteWin(self):
        d1 = DeleteWin("Delete by Promotion ID")

class PromotionWindow() :
    def __init__(self, title) :
        self.cwin = Toplevel()
        self.cwin.title(title)
        self.cwin.geometry('400x300+100+100')
        
        # self.label_promotionid = Label(self.cwin, text="Promotion ID :")
        self.label_productid = Label(self.cwin, text="Product ID :")
        self.label_startdate = Label(self.cwin, text="Start Date :")
        self.label_enddate = Label(self.cwin, text="End Date :")
        self.label_percentage = Label(self.cwin, text="Percentage :")
        self.label_memberpointcost = Label(self.cwin, text="Member Point Cost :")
        #self.label_productname = Label(self.cwin, text="Product Name :")

        # self.entry_promotionid = Entry(self.cwin)
        self.entry_productid = Entry(self.cwin)
        self.entry_startdate = Entry(self.cwin)
        self.entry_enddate = Entry(self.cwin)
        self.entry_percentage = Entry(self.cwin)
        self.entry_memberpointcost = Entry(self.cwin)
        #self.entry_productname = Entry(self.cwin)


        self.button_submit=Button(self.cwin, text ="SUBMIT", command=self.cwin.destroy)
        self.button_exit=Button(self.cwin, text="EXIT", command=self.cwin.destroy)


        # ! no productname

        # self.label_promotionid.grid(row=0,column=0)
        self.label_productid.grid(row=0,column=0)
        self.label_startdate.grid(row=1,column=0)
        self.label_enddate.grid(row=2,column=0)
        self.label_percentage.grid(row=3,column=0)
        self.label_memberpointcost.grid(row=4,column=0)
        #self.label_productname.grid(row=10, column=0)
        
        # self.entry_promotionid.grid(row=0,column=1)
        self.entry_productid.grid(row=0,column=1)
        self.entry_startdate.grid(row=1,column=1)
        self.entry_enddate.grid(row=2,column=1)
        self.entry_percentage.grid(row=3,column=1)
        self.entry_memberpointcost.grid(row=4,column=1)
        #self.entry_productname.grid(row=10, column=1)

        self.button_submit.grid(row=5,column=1)
        self.button_exit.grid(row=6, column=1)

        self.label_status=Label(self.cwin, text="")
        self.label_status.grid(row=8, columnspan=2)

class LookingPromotionWindow():
    def __init__(self, title) :
        self.cwin = Toplevel()
        self.cwin.title(title)
        self.cwin.geometry('350x100+100+100')
        
        self.label_promotionid = Label(self.cwin, text="Promotion ID :")
        
        self.entry_promotionid = Entry(self.cwin)
        
        self.button_submit=Button(self.cwin, text ="SUBMIT", command=self.cwin.destroy)
        self.button_exit=Button(self.cwin, text="EXIT", command=self.cwin.destroy)

        self.label_promotionid.grid(row=0,column=0)
    
        self.entry_promotionid.grid(row=0,column=1)
    
        self.button_submit.grid(row=5,column=1)
        self.button_exit.grid(row=6, column=1)

        self.label_status=Label(self.cwin, text="")
        self.label_status.grid(row=8, columnspan=2)

class LookingProductWindow():
    def __init__(self, title) :
        self.cwin = Toplevel()
        self.cwin.title(title)
        self.cwin.geometry('350x100+100+100')
        
        self.label_productname = Label(self.cwin, text="Promotion ID :")
        
        self.entry_productname = Entry(self.cwin)
        
        self.button_submit=Button(self.cwin, text ="SUBMIT", command=self.cwin.destroy)
        self.button_exit=Button(self.cwin, text="EXIT", command=self.cwin.destroy)

        self.label_productname.grid(row=0,column=0)
    
        self.entry_productname.grid(row=0,column=1)
    
        self.button_submit.grid(row=5,column=1)
        self.button_exit.grid(row=6, column=1)

        self.label_status=Label(self.cwin, text="")
        self.label_status.grid(row=8, columnspan=2)

class TableWindow():
    def __init__(self, title):
        self.cwin = Toplevel()
        self.cwin.title(title)
        self.cwin.geometry('350x100+100+100')


        # STILL NOT FIX
        # scores = tk.Tk() 
        # label = tk.Label(scores, text="High Scores", font=("Arial",30)).grid(row=0, columnspan=3)
        # # create Treeview with 3 columns
        # cols = ('Position', 'Name', 'Score')
        # listBox = ttk.Treeview(scores, columns=cols, show='headings')
        # # set column headings
        # for col in cols:
        #     listBox.heading(col, text=col)    
        # listBox.grid(row=1, column=0, columnspan=2)

        # showScores = tk.Button(scores, text="Show scores", width=15, command=show).grid(row=4, column=0)
        # closeButton = tk.Button(scores, text="Close", width=15, command=exit).grid(row=4, column=1)

        
        
class RegisterWin(PromotionWindow) :
    def __init__(self, title) :
        super().__init__(title)
        self.button_submit.configure(text="AddNew", command=self.submitNewPromotion)
        
    def submitNewPromotion(self) :
        self.cwin.title("Submitted")
        dataentry = [self.entry_productid.get(), 
                    self.entry_startdate.get(),
                    self.entry_enddate.get(),
                    self.entry_percentage.get(),
                    self.entry_memberpointcost.get()]
        aPromotion = Promotion(dataentry)
        retmsg = aPromotion.write()
        self.label_status.config(text=retmsg[1])
       

class SearchWin(LookingPromotionWindow) :
    def __init__(self, title) :
        super().__init__(title)
        self.button_submit.config(text="Search", command=self.searchPromotion)
        self.button_submit=Button(self.cwin)
        
    def searchPromotion(self) :
        self.cwin.title("Searched")
        dataentry = [self.entry_promotionid.get(), self.entry_productid.get()]
        aPromotion = Promotion(dataentry)
        
        retmsg = aPromotion.search()

        if retmsg[0] == "0" :
            self.entry_promotionid.delete(0, END)
            self.entry_promotionid.insert(0, aPromotion.getInfo()[0])
            self.entry_productname.delete(0, END)
            self.entry_productname.insert(0, aPromotion.getInfo()[1])
            
        else :
            self.entry_productname.delete(0, END)
            self.entry_productname.insert(0, "?????")
        self.label_status.config(text=retmsg[1])
        

#Exercise Search by Name
class SearchNameWin(LookingProductWindow) :
    def __init__(self, title) :
        super().__init__(title)
        self.button_submit.config(text="Search", command=self.searchNameProduct)
        self.button_submit=Button(self.cwin)
        
    def searchNameProduct(self) :
        self.cwin.title("Searched")
        dataentry = [self.entry_promotionid.get(), self.entry_productname.get()]
        aPromotion = Promotion(dataentry)
        
        retmsg = aPromotion.searchName()
        self.label_status.config(text=retmsg[1])

class DeleteWin(PromotionWindow) :
    def __init__(self, title) :
        super().__init__(title)
        self.button_submit.config(text="Delete", command=self.deletePromotion)
        self.button_submit=Button(self.cwin)
    
    def deletePromotion(self) :
        self.cwin.title("Deleted")
        dataentry = [self.entry_promotionid.get(), self.entry_productname.get()]
        aPromotion = Promotion(dataentry)
        retmsg = aPromotion.delete()
        self.label_status.config(text=retmsg[1])


class ShowWin(TableWindow):
    def __init__(self, title):
        super().__init__(title)
        self.button_submit.config(text="Show", command=self.showTable)
        self.button_submit = Button(self.cwin)
    def showTable(self):
        self.cwin.title("Shown")
        dataentry = list()
        aPromotion = Promotion(dataentry)
        retmsg = aPromotion.showTable()
        cols = aPromotion.columns
        records = aPromotion.records




Mainmenu = RootWin()
