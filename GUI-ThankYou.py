from tkinter import *

class RootWin() :
    def __init__(self) :
           
        root = Tk()
        root.title("ThankWindow")
        root.geometry('200x150+100+100')

        label_thank = Label(root,text = "THANK YOU")

        button_home = Button(root,text = "home",command = self.backToHome)

        label_thank.pack()
        button_home.pack()
        root.mainloop()

        #Destroy non complete

        # self.cwin = Tk()
        # self.cwin.title("ThankWindow")
        # self.cwin.geometry('200x150+100+100')

        # label_thank = Label(self.cwin,text = "THANK YOU")

        # button_home = Button(self.cwin,text = "home",command = self.backToHome)

        # label_thank.pack()
        # button_home.pack()
        # self.cwin.mainloop()

    def backToHome(self) :
            #r1 = Home("")
            #self.cwin.destroy()
            r2 = RegisterWin("")

class Home() :
    def __init__(self,title) :
        super().__init__(title)
        #root = Tk()
        
        #self.header = Label(text="Main Menu")
        #header.pack()
        
        self.addButton.configure(text="Add New Customer", command=self.popAddWin)
        #addButton.pack(side=TOP)
        self.searchButton.configure(text="Search by ID", command=self.popSearchWin)
        #searchButton.pack(side=TOP)
        self.searchNameButton.configure( text="Search by Name", command=self.popSearchNameWin)
        #searchNameButton.pack(side=TOP)
        self.exitButton.configure( text="Exit", command=self.exitProgram)
        #exitButton.pack(side=BOTTOM)
        self.deleteButton.configure(text="Delete by ID", command=self.popDeleteWin)
        #deleteButton.pack(side=TOP)
        #root.geometry('200x150+100+100')
        #root.mainloop()
        
    def popAddWin(self) :
        r1 = RegisterWin("Customer Registration")
    def popSearchWin(self) :
        s1 = SearchWin("Customer Search")
    def popSearchNameWin(self) :
        s1 = SearchNameWin("Search by Name")
    def exitProgram(self) :
        exit()
    def popDeleteWin(self):
        d1 = DeleteWin("Delete by ID")

class CustomerWindow() :
    def __init__(self, title) :
        self.cwin = Toplevel()
        self.cwin.title(title)
        self.cwin.geometry('200x150+100+100')
        
        self.label_id=Label(self.cwin, text="Id = ")
        self.label_name=Label(self.cwin, text="Name = ")

        self.entry_id=Entry(self.cwin)
        self.entry_name=Entry(self.cwin)

        self.button_submit=Button(self.cwin, text ="SUBMIT", command=self.cwin.destroy)
        self.button_exit=Button(self.cwin, text="EXIT", command=self.cwin.destroy)

        self.label_id.grid(row=0,column=0)
        self.label_name.grid(row=1,column=0)
        
        self.entry_id.grid(row=0,column=1)
        self.entry_name.grid(row=1,column=1)

        self.button_submit.grid(row=2,column=1)
        self.button_exit.grid(row=3, column=1)

        self.label_status=Label(self.cwin, text="")
        self.label_status.grid(row=5, columnspan=2)
        


        
class RegisterWin(CustomerWindow) :
    def __init__(self, title) :
        super().__init__(title)
        self.button_submit.configure(text="AddNew", command=self.submitNewCust)
        
    def submitNewCust(self) :
        self.cwin.title("Submitted")
        dataentry = [self.entry_id.get(), self.entry_name.get()]
        aCustomer = Customer(dataentry)
        retmsg = aCustomer.write()
        self.label_status.config(text=retmsg[1])
                

class SearchWin(CustomerWindow) :
    def __init__(self, title) :
        super().__init__(title)
        self.button_submit.config(text="Search", command=self.searchCust)
        self.button_submit=Button(self.cwin)
        
    def searchCust(self) :
        self.cwin.title("Searched")
        dataentry = [self.entry_id.get(), self.entry_name.get()]
        aCustomer = Customer(dataentry)
        
        retmsg = aCustomer.search()

        if retmsg[0] == "0" :
            self.entry_id.delete(0, END)
            self.entry_id.insert(0, aCustomer.getInfo()[0])
            self.entry_name.delete(0, END)
            self.entry_name.insert(0, aCustomer.getInfo()[1])
            
        else :
            self.entry_name.delete(0, END)
            self.entry_name.insert(0, "?????")
        self.label_status.config(text=retmsg[1])
        

#Exercise Search by Name
class SearchNameWin(CustomerWindow) :
    def __init__(self, title) :
        super().__init__(title)
        self.button_submit.config(text="Search", command=self.searchNameCust)
        self.button_submit=Button(self.cwin)
        
    def searchNameCust(self) :
        self.cwin.title("Searched")
        dataentry = [self.entry_id.get(), self.entry_name.get()]
        aCustomer = Customer(dataentry)
        
        retmsg = aCustomer.searchName()
        self.label_status.config(text=retmsg[1])

class DeleteWin(CustomerWindow) :
    def __init__(self, title) :
        super().__init__(title)
        self.button_submit.config(text="Delete", command=self.deleteCust)
        self.button_submit=Button(self.cwin)
    
    def deleteCust(self) :
        self.cwin.title("Deleted")
        dataentry = [self.entry_id.get(), self.entry_name.get()]
        aCustomer = Customer(dataentry)
        retmsg = aCustomer.delete()
        self.label_status.config(text=retmsg[1])

Mainmenu = RootWin()
