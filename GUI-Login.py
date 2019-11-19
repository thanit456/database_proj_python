from tkinter import *
from db_login import *

class LoginWindow() :
    def __init__ (self):
        self.cwin = Tk()
        self.cwin.title("Login")
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
        #for testing username = '' password = '' to login
        # def login():
        #     if self.entry_username.get() == "" and self.entry_password.get() == "":
        #         user = ""
        #         self.cwin.destroy()
        #         m1 = MenuWin()
        #     else:
        #         print("Error")
        #         self.entryText1.set("")                
        #         self.entryText2.set("")
        #         self.label_status.config(text="Incorrect")
        def checklogin() :
            dataentry = [self.entryText1.get(), self.entryText2.get()]
            alogin = Login(dataentry)
        
            retmsg = alogin.login()

            if retmsg[0] == "0" :
                self.cwin.destroy()
                m1 = MenuWin()
            
            else :
                print("Error")
                self.entryText1.set("")               
                self.entryText2.set("")
            self.label_status.config(text=retmsg[1])

        self.button_login = Button(self.cwin,text="Login",command=checklogin) # need to change to real login compare from database

        self.label_username.grid(row=0,column=0)
        self.entry_username.grid(row=0,column=1)
        self.label_password.grid(row=1,column=0)
        self.entry_password.grid(row=1,column=1)
        self.button_login.grid(row=2,column=1)
        self.label_status.grid(row=3,column=1)
        self.cwin.mainloop()

class MenuWin() :
    def __init__(self) :
        self.root = Tk()
        self.root.title("Member Main Menu")
        self.root.geometry('500x300')
        
        self.header = Label(self.root, text="Main Menu")
        self.header.pack()

        self.root.mainloop()

Mainmenu = LoginWindow()