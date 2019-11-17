from tkinter import *

class RootWin() :
    def __init__(self) :
        root = Tk()
        root.title("Member Main Menu")
        global user
        user = "none"
        
        header = Label(root, text="Main Menu")
        header.pack()
        
        global loginButton
        loginButton = Button(root, text = "Login",command=self.popLogin)
        loginButton.pack(side=TOP)
        
        searchProductButton = Button(root, text="Search Product by Branch Name and  Product Name", command=self.popSearchProductWin)
        searchProductButton.pack(side=TOP)

        searchPromotionButton = Button(root, text="Search Promotion by Branch Name and Product Name", command=self.popSearchPromotionWin)
        searchPromotionButton.pack(side=TOP)

        root.geometry('300x200')
        root.mainloop()
        
    def popSearchProductWin(self) :
        s1 = SearchProductWin("Product Search")
    def popSearchPromotionWin(self) :
        s2 = SearchPromotionWin("Promotion Search")
    def popLogin(self) :
        l1 = LoginWindow("Login")

class LoginWindow() :
    def __init__ (self,title):
        self.cwin = Toplevel()
        self.cwin.title(title)
        self.cwin.geometry('300x200')

        self.label_username = Label(self.cwin,text="Username :")
        self.label_password = Label(self.cwin,text="Password :")

        self.entry_username = Entry(self.cwin)
        self.entry_password = Entry(self.cwin)
        
        #for testing only
        def login():
            if self.entry_username.get() == "member" and self.entry_password.get() == "member":
                user = "member"
                print(user)
                loginButton.config(text=user)
                self.cwin.destroy()
            else:
                loginButton.config(text="Error")
                print("Error")
                self.cwin.destroy()

        self.button_login = Button(self.cwin,text="Login",command=login) # need to change to real login compare from database

        self.label_username.grid(row=0,column=0)
        self.entry_username.grid(row=0,column=1)
        self.label_password.grid(row=1,column=0)
        self.entry_password.grid(row=1,column=1)
        self.button_login.grid(row=2,column=1)

class SearchPromotionWin() :
    def __init__(self,title):
        self.cwin = Toplevel()
        self.cwin.title(title)
        self.cwin.geometry('300x200')

        def popupSelect():
            self.sbwin = Tk()
            self.sbwin.title("Select Branch Name")
            self.sbwin.geometry("250x250")
            self.scrollbar = Scrollbar(self.sbwin)
            self.scrollbar.pack(side=RIGHT, fill=Y)
            self.lbl = Label(self.sbwin,text = "A list of Branch Name.")
            self.lbl.pack(side = TOP)    
            self.branchList = Listbox(self.sbwin,yscrollcommand = self.scrollbar.set)

            for line in range(30):  
                self.branchList.insert(END, "Number " + str(line)) 

            self.branchList.pack(side = LEFT)  
            #this button will delete the selected item from the list
            def getSelect():
                self.x = self.branchList.get(ANCHOR)
                print(self.x)
                self.button_select.config(text=self.x,command = popupSelect)
                self.sbwin.destroy()

            self.button_selectBranch = Button(self.sbwin, text = "select", command = getSelect)  
            self.button_selectBranch.pack(side = RIGHT)  

        self.label_branchName = Label(self.cwin,text="Branch Name :")
        self.button_select = Button(self.cwin,text="Select Branch",command = popupSelect)
        self.label_name = Label(self.cwin,text="Product Name :")
        self.entry_name = Entry(self.cwin)

        self.label_branchName.grid(row=0,column=0)
        self.button_select.grid(row=0,column=1)
        self.label_name.grid(row=1,column=0)
        self.entry_name.grid(row=1,column=1)
        
        self.button_submit=Button(self.cwin, text ="SEARCH", command=self.cwin.destroy) #need to add command for search
        self.button_exit=Button(self.cwin, text="EXIT", command=self.cwin.destroy)

        self.button_submit.grid(row=2,column=1)
        self.button_exit.grid(row=3, column=1)



class SearchProductWin() :
    def __init__(self, title) :
        self.cwin = Toplevel()
        self.cwin.title(title)
        self.cwin.geometry('300x200')

        self.x = 0
        
        self.label_branch=Label(self.cwin, text="Branch Name :")
        self.label_name=Label(self.cwin, text="Product Name :")

        def popupSelect():
            self.sbwin = Tk()
            self.sbwin.title("Select Branch Name")
            self.sbwin.geometry("250x250")
            self.scrollbar = Scrollbar(self.sbwin)
            self.scrollbar.pack(side=RIGHT, fill=Y)
            self.lbl = Label(self.sbwin,text = "A list of Branch Name.")
            self.lbl.pack(side = TOP)    
            self.branchList = Listbox(self.sbwin,yscrollcommand = self.scrollbar.set)

            for line in range(30):  
                self.branchList.insert(END, "Number " + str(line)) 

            self.branchList.pack(side = LEFT)  
            #this button will delete the selected item from the list
            def getSelect():
                self.x = self.branchList.get(ANCHOR)
                print(self.x)
                self.button_select.config(text=self.x,command = popupSelect)
                self.sbwin.destroy()

            self.button_selectBranch = Button(self.sbwin, text = "select", command = getSelect)  
            self.button_selectBranch.pack(side = RIGHT)  

        self.button_select = Button(self.cwin,text="Select Branch",command = popupSelect)
        self.entry_name=Entry(self.cwin)

        self.button_submit=Button(self.cwin, text ="SEARCH", command=self.cwin.destroy) #need to add command for search
        self.button_exit=Button(self.cwin, text="EXIT", command=self.cwin.destroy)

        self.label_branch.grid(row=0,column=0)
        self.label_name.grid(row=1,column=0)
        
        self.button_select.grid(row=0,column=1)
        self.entry_name.grid(row=1,column=1)

        self.button_submit.grid(row=2,column=1)
        self.button_exit.grid(row=3, column=1)



Mainmenu = RootWin()