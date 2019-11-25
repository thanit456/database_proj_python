from tkinter import *
from tkinter import ttk
from db_mainmember import *
from db_mainmember  import *

class LoginWindow() :
    def __init__ (self):
        self.cwin = Tk()
        self.cwin.title("Login")
        self.cwin.geometry('300x160')
        self.cwin.resizable(0,0)

        #function
        def checklogin() :
            dataentry = [self.entryText1.get(), self.entryText2.get()]
            alogin = Login(dataentry)
        
            retmsg = alogin.login()

            if retmsg[0] == "0" :
                self.cwin.destroy()
                m1 = MenuWithLoginWin(retmsg[2])
            
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
        self.label_status = Label(self.cwin,text="",foreground="red")
        self.entry_username = Entry(self.cwin,textvariable=self.entryText1)
        self.entry_password = Entry(self.cwin,textvariable=self.entryText2 ,show = "•")
        self.button_login = Button(self.cwin,text=" Login ",command=checklogin) # need to change to real login compare from database
        self.button_register = Button(self.cwin,text="Sign up",command=signUp)
        self.button_back = Button(self.cwin,text=" Back",command=back)

        #put every components in window
        self.label_username.place(x=40,y=25)
        self.entry_username.place(x=110,y=25)
        self.label_password.place(x=40,y=50)
        self.entry_password.place(x=110,y=50)
        self.button_login.place(x=160,y=80)
        self.button_register.place(x=185,y=120)
        self.button_back.place(x=240,y=120)
        self.label_status.place(x=40,y=125)

        self.cwin.mainloop()

class SignUpWin():
    def __init__(self):
        self.cwin = Tk()
        self.cwin.title("RegisterWindow")
        self.cwin.geometry('340x220')
        self.cwin.resizable(0,0)
        #function
        def back() :
            self.cwin.destroy()
            l1 = LoginWindow()
        
        def addMember():
            dataentry = [self.entryTextFn.get(), self.entryTextLn.get(),self.entryTextId.get(),self.entryTextUn.get(),self.entryTextPass.get()]
            aregister = Register(dataentry)

            retmsg = aregister.register()

            if retmsg[0] == "0" :
                self.cwin.destroy()
                sw1 = SucessWin()
            else:
                print('Error')
                self.label_status.config(text=retmsg[1])

        #create components
        self.label_fname = Label(self.cwin, text = "First Name :")
        self.label_lname = Label(self.cwin, text = "Last Name :")
        self.label_id = Label(self.cwin, text="Identification Number :")
        self.label_username = Label(self.cwin,text = "username :")
        self.label_password = Label(self.cwin, text = "password :")
        self.label_status = Label(self.cwin,text="",foreground="red")
        self.entryTextFn = StringVar()
        self.entryTextLn = StringVar()
        self.entryTextId = StringVar()
        self.entryTextUn = StringVar()
        self.entryTextPass = StringVar()
        self.entry_boxFn = Entry(self.cwin,textvariable = self.entryTextFn)
        self.entry_boxLn = Entry(self.cwin,textvariable = self.entryTextLn)
        self.entry_boxId = Entry(self.cwin,textvariable = self.entryTextId)
        self.entry_boxUn = Entry(self.cwin,textvariable= self.entryTextUn)
        self.entry_boxPass = Entry(self.cwin,textvariable = self.entryTextPass,show = "•")
        self.button_back = Button(self.cwin,text=" Back ",command=back)
        self.button_OK=Button(self.cwin, text =" Sign up " ,command = addMember)

        #put every components in window
        self.label_fname.place(x=10,y=10)
        self.label_lname.place(x=10,y=40)
        self.label_id.place(x=10,y=70)
        self.label_username.place(x=10,y=100)
        self.label_password.place(x=10,y=130)
        self.entry_boxFn.place(x=150,y=10)
        self.entry_boxLn.place(x=150,y=40)
        self.entry_boxId.place(x=150,y=70)
        self.entry_boxUn.place(x=150,y=100)
        self.entry_boxPass.place(x=150,y=130)
        self.label_status.place(x=20,y=170)
        self.button_OK.place(x=180,y=170)
        self.button_back.place(x=250,y=170)

        self.cwin.mainloop()

class SucessWin():
    def __init__(self):
        self.cwin = Tk()
        self.cwin.title("Sucess sign up")
        self.cwin.geometry('350x100')
        self.cwin.resizable(0,0)

        #function
        def goback():
            self.cwin.destroy()
            l1 = LoginWindow()

        #create components
        self.label_show_message = Label(self.cwin,text="You are now member of Too's Superstore.")
        self.button_ok = Button(self.cwin,text="OK, back to Login",command=goback)
        
        #put every components in window
        self.label_show_message.place(x=60,y=20)
        self.button_ok.place(x=120,y=50)

        self.cwin.mainloop()



class MenuWin():
    def __init__(self) :
        self.root = Tk()
        self.root.title("Customer Main Menu")
        self.root.geometry('360x200')
        self.root.resizable(0,0)
        
        #function
        def popSearchProductWin() :
            s1 = SearchProductWin("Product Search")
        def popSearchPromotionWin() :
            s2 = SearchPromotionWin("Promotion Search")
        def login():
            self.root.destroy()
            l1 = LoginWindow()
        
        #create components
        self.header = Label(self.root, text="Customer Main Menu", font=("Arial",14))
        self.searchProductButton = Button(self.root, text="Search Product", command=popSearchProductWin)
        self.searchPromotionButton = Button(self.root, text="Search Promotion", command=popSearchPromotionWin)
        self.loginButton = Button(self.root,text="Log in",command=login)
        
        #put every components in window
        self.header.place(x=90,y=10)
        self.searchProductButton.place(x=135,y=55)
        self.searchPromotionButton.place(x=127,y=95)
        self.loginButton.place(x=160,y=150)

        self.root.mainloop()

class MenuWithLoginWin() :
    def __init__(self,user) :
        self.root = Tk()
        self.user = user
        self.root.title("Member Main Menu")
        self.root.geometry('360x200')
        self.root.resizable(0,0)
      
        #function
        def popSearchProductWin() :
            s1 = SearchProductWin("Product Search")
        def popSearchPromotionWin() :
            s2 = SearchPromotionWin("Promotion Search")
        def popMemberInfo():
            dataentry = [self.user]
            ameminfo = SelectMemInfo(dataentry)
            records = ameminfo.showmeminfo()
            self.root.destroy()
            sm1 = ShowMemInfo("MemberInfo",records,self.user)
        def logout():
            self.root.destroy()
            l1 = MenuWin()
        
        #create components
        self.header = Label(self.root, text="Member Main Menu", font=("Arial",14))
        self.searchProductButton = Button(self.root, text="Search Product", command=popSearchProductWin)
        self.searchPromotionButton = Button(self.root, text="Search Promotion", command=popSearchPromotionWin)
        self.showMemberInfoButton = Button(self.root,text="Member Info",command=popMemberInfo)
        self.LogoutButton = Button(self.root,text="Log out",command=logout)

        #put every components in window
        self.header.place(x=90,y=10)
        self.searchProductButton.place(x=135,y=55)
        self.searchPromotionButton.place(x=127,y=95)
        self.showMemberInfoButton.place(x=140,y=135)
        self.LogoutButton.place(x=280,y=160)

        self.root.mainloop()
        
    
class ShowMemInfo() :
    def __init__(self,title,records,user):
        self.cwin = Tk()
        self.user = user
        self.records = records
        self.cwin.title(title)
        self.cwin.geometry('360x200')
        self.cwin.resizable(0,0)

        #function
        def backToMenu() :
            self.cwin.destroy()
            m1 = MenuWithLoginWin(self.user)

        #create components
        self.label_name = Label(self.cwin,text="Name :")
        self.label_mem_name = Label(self.cwin,text=self.records[1])
        self.label_lname = Label(self.cwin,text="Last Name :")
        self.label_mem_lname = Label(self.cwin,text=self.records[2])
        self.label_sdate = Label(self.cwin,text="Start Date :")
        self.label_mem_sdate = Label(self.cwin,text=self.records[3])
        self.label_edate = Label(self.cwin,text="Expired date :")
        self.label_mem_edate = Label(self.cwin,text=self.records[4])
        self.label_points = Label(self.cwin,text="Member Points :")
        self.label_mem_points = Label(self.cwin,text=self.records[5])
        # self.button_purchaseHis = Button(self.cwin,text="Show Purchase History",command = self.cwin.destroy) #need to change command to go to history page of that user
        self.button_back = Button(self.cwin,text=" Back ",command=backToMenu)
        
        #put every components in window
        self.label_name.place(x=10,y=10)
        self.label_mem_name.place(x=150,y=10)
        self.label_lname.place(x=10,y=40)
        self.label_mem_lname.place(x=150,y=40)
        self.label_sdate.place(x=10,y=70)
        self.label_mem_sdate.place(x=150,y=70)
        self.label_edate.place(x=10,y=100)
        self.label_mem_edate.place(x=150,y=100)
        self.label_points.place(x=10,y=130)
        self.label_mem_points.place(x=150,y=130)
        # self.button_purchaseHis.place(x=80,y=160)
        self.button_back.place(x=280,y=160)

        self.cwin.mainloop()

class SearchPromotionWin() :
    def __init__(self,title):
        self.cwin = Tk()
        self.cwin.title(title)
        self.cwin.geometry('1160x460')
        
        #create components
        self.label_pname = Label(self.cwin,text="Product Name :")
        self.text_pname = StringVar()
        self.text_pname.set("")
        self.entry_pname = Entry(self.cwin,textvariable=self.text_pname)
        self.label_pname.place(x=30,y=70)
        self.entry_pname.place(x=120,y=70)

        #function
        def show():
            self.queryList = self.queryPromotion() #query
            self.leaf_nodes = self.tree.get_children()
            for i in self.leaf_nodes:
                self.tree.delete(i)
            for i,(promotionid,productid,productname,startdate,enddate,mempoint,oldprice,discount,newprice) in enumerate(self.queryList,start=1):
                self.tree.insert("","end", values=(i,promotionid,productid,productname,startdate,enddate,mempoint,oldprice,discount,newprice))
        
        self.table_label = Label(self.cwin,text="Promotion", font=("Arial",24))
        self.table_label.place(x=480,y=10)
        
        #table component
        self.cols = ('No.','Promotion ID','Product ID','Product Name','Start Date','End Date','Member Points','Original Price','Percent Discount','Discount Price')
        self.tree = ttk.Treeview(self.cwin,column=self.cols,show='headings',padding=30)
        for col in self.cols:
            self.tree.column(col,width=100,stretch=NO)
            self.tree.heading(col,text=col)
        self.tree.place(x=30,y=100,width=1100, height=300)

        #button components
        self.button_submit=Button(self.cwin, text ="SEARCH", command=show)
        self.button_exit=Button(self.cwin, text=" Close ", command=self.cwin.destroy)
        self.button_submit.place(x=250,y=67)
        self.button_exit.place(x=520,y=420)

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
        self.cwin.geometry('890x460')
        
        #function
        def callback():
            self.cwin.destroy()

        def show():
            self.queryList = self.queryProduct() #query
            self.leaf_nodes = self.tree.get_children()
            for i in self.leaf_nodes:
                self.tree.delete(i)
            for i,(p,n,d,b,q,m) in enumerate(self.queryList,start=1):
                self.tree.insert("","end", values=(i,p,n,d,b,q,m))
        
        self.table_label = Label(self.cwin,text="Product", font=("Arial",24))
        self.table_label.place(x=360,y=10)
        
        #table component
        self.cols = ('No.','Product ID','Name','Description','Branch','Quantity','Point gain')
        self.tree = ttk.Treeview(self.cwin,column=self.cols,show='headings',padding=30)
        for col in self.cols:
            self.tree.column(col,width=100,stretch=NO)
            self.tree.heading(col,text=col)
        self.tree.place(x=30,y=100,width=800, height=300)

        #create components
        self.label_name=Label(self.cwin, text="Product Name :")
        self.entry_name=Entry(self.cwin)
        self.button_submit=Button(self.cwin, text ="SEARCH", command=show) #need to add command for search
        self.button_exit=Button(self.cwin, text=" Close ", command=self.cwin.destroy)

        #put every components in window
        self.label_name.place(x=30,y=70)
        self.entry_name.place(x=120,y=70)
        self.button_submit.place(x=250,y=67)
        self.button_exit.place(x=380,y=420)
    
    def queryProduct(self):
        dataentry = [
            self.entry_name.get()
        ]
        aProduct = Product(dataentry)
        return aProduct.showTable()

Mainmenu = MenuWin()