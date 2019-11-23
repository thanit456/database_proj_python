from tkinter import *
from tkinter import ttk
from db_mainmember import *
from db_mainmember  import *

class LoginWindow() :
    def __init__ (self):
        self.cwin = Tk()
        self.cwin.title("Login")
        self.cwin.geometry('315x85')

        #function
        def checklogin() :
            dataentry = [self.entryText1.get(), self.entryText2.get()]
            alogin = Login(dataentry)
        
            retmsg = alogin.login()

            if retmsg[0] == "0" :
                self.cwin.destroy()
                m1 = MenuWithLoginWin()
            
            else :
                print("Error")
                self.entryText1.set("")               
                self.entryText2.set("")
            self.label_status.config(text=retmsg[1])

        def signUp():
                self.cwin.destroy()
                su = SignUpWin()

        def back():
            self.cwin.destroy()
            m1 = MenuWin()

        #create components
        self.entryText1 =  StringVar()
        self.entryText1.set("")
        self.entryText2 =  StringVar()
        self.entryText2.set("")
        self.label_username = Label(self.cwin,text="Username :")
        self.label_password = Label(self.cwin,text="Password :")
        self.label_status = Label(self.cwin,text="")
        self.entry_username = Entry(self.cwin,textvariable=self.entryText1)
        self.entry_password = Entry(self.cwin,textvariable=self.entryText2 ,show = "•")
        self.button_login = Button(self.cwin,text="Login",command=checklogin) # need to change to real login compare from database
        self.button_register = Button(self.cwin,text="Sign up",command=signUp)
        self.button_back = Button(self.cwin,text=" Back",command=back)

        #put every components in window
        self.label_username.grid(row=0,column=0)
        self.entry_username.grid(row=0,column=1)
        self.label_password.grid(row=1,column=0)
        self.entry_password.grid(row=1,column=1)
        self.button_login.grid(row=2,column=1)
        self.button_register.grid(row=2,column=0)
        self.button_back.grid(row=2,column=2)
        self.label_status.grid(row=3,column=1)

        self.cwin.mainloop()

class SignUpWin():
    def __init__(self):
        self.cwin = Tk()
        self.cwin.title("RegisterWindow")
        self.cwin.geometry('265x170')

        #function
        def back() :
            self.cwin.destroy()
            l1 = LoginWindow()
        
        def addMember():
            dataentry = [self.entryTextFn.get(), self.entryTextLn.get(),self.entryTextUn.get(),self.entryTextPass.get()]
            aregister = Register(dataentry)
        
            retmsg = aregister.register()

            if retmsg[0] == "0" :
                self.cwin.destroy()
                sw1 = SucessWin()
            else:
                self.entryTextFn.set("")
                self.entryTextLn.set("")
                self.entryTextUn.set("")
                self.entryTextPass.set("")
                print('Error')
                self.label_status.config(text=retmsg[1])

        #create components
        self.label_fname = Label(self.cwin, text = "First Name :")
        self.label_lname = Label(self.cwin, text = "Last Name :")
        self.label_username = Label(self.cwin,text = "username :")
        self.label_password = Label(self.cwin, text = "password :")
        self.label_status = Label(self.cwin,text="")
        self.entryTextFn = StringVar()
        self.entryTextLn = StringVar()
        self.entryTextUn = StringVar()
        self.entryTextPass = StringVar()
        self.entry_boxFn = Entry(self.cwin,textvariable = self.entryTextFn)
        self.entry_boxLn = Entry(self.cwin,textvariable = self.entryTextLn)
        self.entry_boxUn = Entry(self.cwin,textvariable= self.entryTextUn)
        self.entry_boxPass = Entry(self.cwin,textvariable = self.entryTextPass,show = "•")
        self.button_back = Button(self.cwin,text="Back",command=back)
        self.button_OK=Button(self.cwin, text ="Sign up" ,command = addMember)

        #put every components in window
        self.label_fname.grid(row=0,column=0)
        self.label_lname.grid(row=1,column=0)
        self.label_username.grid(row=2,column=0)
        self.label_password.grid(row=3,column=0)
        self.entry_boxFn.grid(row=0,column=1)
        self.entry_boxLn.grid(row=1,column=1)
        self.entry_boxUn.grid(row=2,column=1)
        self.entry_boxPass.grid(row=3,column=1)
        self.button_OK.grid(row=4,column=1)
        self.button_back.grid(row=5,column=1)

        self.cwin.mainloop()

class SucessWin():
    def __init__(self):
        self.cwin = Tk()
        self.cwin.title("Sucess sign up")
        self.cwin.geometry('350x100')

        #function
        def goback():
            self.cwin.destroy()
            l1 = LoginWindow()

        #create components
        self.label_indent = Label(self.cwin,text="")
        self.label_show_message = Label(self.cwin,text="You are now member of Too's Superstore.")
        self.button_ok = Button(self.cwin,text="OK, back to Login",command=goback)
        
        #put every components in window
        self.label_indent.pack()
        self.label_show_message.pack()
        self.button_ok.pack()

        self.cwin.mainloop()



class MenuWin() :
    def __init__(self) :
        self.root = Tk()
        self.root.title("Member Main Menu")
        self.root.geometry('375x120')
        
        #function
        def popSearchProductWin() :
            s1 = SearchProductWin("Product Search")
        def popSearchPromotionWin() :
            s2 = SearchPromotionWin("Promotion Search")
        def login():
            self.root.destroy()
            l1 = LoginWindow()
        
        #create components
        self.header = Label(self.root, text="Member Main Menu")
        self.searchProductButton = Button(self.root, text="Search Product", command=popSearchProductWin)
        self.searchPromotionButton = Button(self.root, text="Search Promotion", command=popSearchPromotionWin)
        self.loginButton = Button(self.root,text="Log in",command=login)
        
        #put every components in window
        self.header.pack()
        self.searchProductButton.pack(side=TOP)
        self.searchPromotionButton.pack(side=TOP)
        self.loginButton.pack(side=TOP)

        self.root.mainloop()

class MenuWithLoginWin() :
    def __init__(self) :
        self.root = Tk()
        self.root.title("Customer Main Menu")
        self.root.geometry('370x150')
      
        #function
        def popSearchProductWin() :
            s1 = SearchProductWin("Product Search")
        def popSearchPromotionWin() :
            s2 = SearchPromotionWin("Promotion Search")
        def showMemberInfo():
            self.root.destroy()
            sm1 = ShowMemInfo("MemberInfo")
        def logout():
            self.root.destroy()
            l1 = MenuWin()
        
        #create components
        self.header = Label(self.root, text="Customer Main Menu")
        self.searchProductButton = Button(self.root, text="Search Product", command=popSearchProductWin)
        self.searchPromotionButton = Button(self.root, text="Search Promotion", command=popSearchPromotionWin)
        self.showMemberInfoButton = Button(self.root,text="Member Info",command=showMemberInfo)
        self.LogoutButton = Button(self.root,text="Log out",command=logout)

        #put every components in window
        self.header.pack()
        self.searchProductButton.pack(side=TOP)
        self.searchPromotionButton.pack(side=TOP)
        self.showMemberInfoButton.pack(side=TOP)
        self.LogoutButton.pack(side=TOP)

        self.root.mainloop()
        
    
        

class ShowMemInfo() :
    def __init__(self,title):
        self.cwin = Tk()
        self.cwin.title(title)
        self.cwin.geometry('450x200')

        #function
        def backToMenu() :
            self.cwin.destroy()
            m1 = MenuWithLoginWin()

        #create components
        self.label_name = Label(self.cwin,text="Name :")
        self.label_mem_name = Label(self.cwin,text="Pasit")
        self.label_lname = Label(self.cwin,text="Last Name :")
        self.label_mem_lname = Label(self.cwin,text="Laohawarutchai")
        self.label_sdate = Label(self.cwin,text="Start Date :")
        self.label_mem_sdate = Label(self.cwin,text="30/09/1998")
        self.label_edate = Label(self.cwin,text="Expired date :")
        self.label_mem_edate = Label(self.cwin,text="30/09/1999")
        self.button_purchaseHis = Button(self.cwin,text="Show Purchase History",command = self.cwin.destroy) #need to change command to go to history page of that user
        self.button_back = Button(self.cwin,text="Back",command=backToMenu)
        
        #put every components in window
        self.label_name.grid(row=0,column=0)
        self.label_mem_name.grid(row=0,column=1)
        self.label_lname.grid(row=1,column=0)
        self.label_mem_lname.grid(row=1,column=1)
        self.label_sdate.grid(row=2,column=0)
        self.label_mem_sdate.grid(row=2,column=1)
        self.label_edate.grid(row=3,column=0)
        self.label_mem_edate.grid(row=3,column=1)
        self.button_purchaseHis.grid(row=4,column=0)
        self.button_back.grid(row=5,column=0)

        self.cwin.mainloop()

class SearchPromotionWin() :
    def __init__(self,title):
        self.cwin = Tk()
        self.cwin.title(title)
        self.cwin.geometry('500x500')
        
        #create components
        self.label_pname = Label(self.cwin,text="Product Name :")
        self.text_pname = StringVar()
        self.text_pname.set("")
        self.entry_pname = Entry(self.cwin,textvariable=self.text_pname)
        self.label_pname.grid(row=1,column=0)
        self.entry_pname.grid(row=1,column=1)

        

        #function
        def show():
            self.queryList = self.queryPromotion() #query
            self.leaf_nodes = self.tree.get_children()
            for i in self.leaf_nodes:
                self.tree.delete(i)
            for i,(promotionid,productid,productname,startdate,enddate,mempoint,oldprice,discount,newprice) in enumerate(self.queryList,start=1):
                self.tree.insert("","end", values=(i,promotionid,productid,productname,startdate,enddate,mempoint,oldprice,discount,newprice))
        
        self.table_label = Label(self.cwin,text="Promotion")
        self.table_label.grid(row=0,columnspan=3)
        #table component
        self.cols = ('No.','Promotion ID','Product ID','Product Name','Start Date','End Date','Member Points','Original Price','Percent Discount','Discount Price')
        self.tree = ttk.Treeview(self.cwin,column=self.cols,show='headings',padding=30)
        for col in self.cols:
            self.tree.column(col,width=100,stretch=NO)
            self.tree.heading(col,text=col)
        self.tree.grid(row=2,column=0,columnspan=2)

        #button components
        self.button_submit=Button(self.cwin, text ="SEARCH", command=show)
        self.button_exit=Button(self.cwin, text="EXIT", command=self.cwin.destroy)
        self.button_submit.grid(row=5,column=0)
        self.button_exit.grid(row=5, column=1)

        self.cwin.mainloop()

    def queryPromotion(self):
        dataentry = [
            self.entry_pname.get()
        ]
        aPromotion = Promotion(dataentry)
        return aPromotion.showTable()



class SearchProductWin() :
    def __init__(self, title) :
        self.cwin = Toplevel()
        self.cwin.title(title)
        self.cwin.geometry('300x100')
        
        #function
        def callback():
            self.cwin.destroy()

        #create components
        self.label_name=Label(self.cwin, text="Product Name :")
        self.entry_name=Entry(self.cwin)
        self.button_submit=Button(self.cwin, text ="SEARCH", command=callback) #need to add command for search
        self.button_exit=Button(self.cwin, text="EXIT", command=self.cwin.destroy)

        #put every components in window
        self.label_name.grid(row=0,column=0)
        self.entry_name.grid(row=0,column=1)
        self.button_submit.grid(row=1,column=1)
        self.button_exit.grid(row=2, column=1)




Mainmenu = MenuWin()