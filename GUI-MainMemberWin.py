from tkinter import *

class LoginWindow() :
    def __init__ (self,title):
        self.cwin = Tk()
        self.cwin.title(title)
        self.cwin.geometry('300x200')

        self.entryText1 =  StringVar()
        self.entryText1.set("")

        self.entryText2 =  StringVar()
        self.entryText2.set("")

        self.label_username = Label(self.cwin,text="Username :")
        self.label_password = Label(self.cwin,text="Password :")
        self.label_status = Label(self.cwin,text="")

        self.entry_username = Entry(self.cwin,textvariable=self.entryText1)
        self.entry_password = Entry(self.cwin,textvariable=self.entryText2)
            
        #for testing only need to send memberID to next step
        #for testing username = 'member' password = 'member' to login
        def login():
            if self.entry_username.get() == "member" and self.entry_password.get() == "member":
                user = "member"
                print(user)
                self.cwin.destroy()
                m1 = MenuWin()
            else:
                print("Error")
                self.entryText1.set("")                
                self.entryText2.set("")
                self.label_status.config(text="Incorrect")

        self.button_login = Button(self.cwin,text="Login",command=login) # need to change to real login compare from database

        self.label_username.grid(row=0,column=0)
        self.entry_username.grid(row=0,column=1)
        self.label_password.grid(row=1,column=0)
        self.entry_password.grid(row=1,column=1)
        self.button_login.grid(row=2,column=1)
        self.label_status.grid(row=3,column=1)
        self.cwin.mainloop()
   

class MenuWin() :
    def __init__(self) :
        root = Tk()
        root.title("Member Main Menu")

        #global variables
        global user,branchLists
        user = ""
        branchLists = ["B1","B2","B3","B4","B5","B6"]

        
        header = Label(root, text="Main Menu")
        header.pack()
        
        searchProductButton = Button(root, text="Search Product by Branch Name and  Product Name", command=self.popSearchProductWin)
        searchProductButton.pack(side=TOP)

        searchPromotionButton = Button(root, text="Search Promotion by Branch Name and Product Name", command=self.popSearchPromotionWin)
        searchPromotionButton.pack(side=TOP)

        root.geometry('500x300')
        root.mainloop()
        
    def popSearchProductWin(self) :
        s1 = SearchProductWin("Product Search")
    def popSearchPromotionWin(self) :
        s2 = SearchPromotionWin("Promotion Search")


class SearchPromotionWin() :
    def __init__(self,title):
        self.cwin = Toplevel()
        self.cwin.title(title)
        self.cwin.geometry('300x200')

        self.branchName = ""

        self.variable = StringVar()
        self.variable.set(branchLists[0])
        self.opt = OptionMenu(self.cwin,self.variable,*branchLists)
        self.variable.trace_add("write",lambda *args : print(self.variable.get()))
        
        #this will get the value of optmenu when submit need to implement to send branchname and productname to DBfunction
        def callback():
            self.branchName = self.variable.get()
            print(self.branchName)
            self.cwin.destroy()

        self.label_branchName = Label(self.cwin,text="Branch Name :")
        
        self.label_name = Label(self.cwin,text="Product Name :")
        self.entry_name = Entry(self.cwin)

        self.label_branchName.grid(row=0,column=0)
        self.opt.grid(row=0,column=1)
        self.label_name.grid(row=1,column=0)
        self.entry_name.grid(row=1,column=1)
        
        self.button_submit=Button(self.cwin, text ="SEARCH", command=callback) #need to add command for search
        self.button_exit=Button(self.cwin, text="EXIT", command=self.cwin.destroy)

        self.button_submit.grid(row=2,column=1)
        self.button_exit.grid(row=3, column=1)



class SearchProductWin() :
    def __init__(self, title) :
        self.cwin = Toplevel()
        self.cwin.title(title)
        self.cwin.geometry('300x200')

        self.branchName = ""
        
        self.label_branch=Label(self.cwin, text="Branch Name :")
        self.label_name=Label(self.cwin, text="Product Name :")

        self.variable = StringVar()
        self.variable.set(branchLists[0])
        self.opt = OptionMenu(self.cwin,self.variable,*branchLists)
        self.variable.trace_add("write",lambda *args : print(self.variable.get()))
        
        #this will get the value of optmenu when submit need to implement to send branchname and productname to DBfunction
        def callback():
            self.branchName = self.variable.get()
            print(self.branchName)
            self.cwin.destroy()

        self.entry_name=Entry(self.cwin)

        self.button_submit=Button(self.cwin, text ="SEARCH", command=callback) #need to add command for search
        self.button_exit=Button(self.cwin, text="EXIT", command=self.cwin.destroy)

        self.label_branch.grid(row=0,column=0)
        self.label_name.grid(row=1,column=0)
        
        self.opt.grid(row=0,column=1)
        self.entry_name.grid(row=1,column=1)

        self.button_submit.grid(row=2,column=1)
        self.button_exit.grid(row=3, column=1)



Mainmenu = LoginWindow("Login")