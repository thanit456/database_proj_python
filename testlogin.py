
# class LoginWindow() :
#     def __init__ (self,title):
#         self.cwin = Toplevel()
#         self.cwin.title(title)
#         self.cwin.geometry('300x200')

#         self.label_username = Label(self.cwin,text="Username :")
#         self.label_password = Label(self.cwin,text="Password :")

#         self.entry_username = Entry(self.cwin)
#         self.entry_password = Entry(self.cwin)
        
#         #for testing only
#         def login():
#             if self.entry_username.get() == "member" and self.entry_password.get() == "member":
#                 user = "member"
#                 print(user)
#                 loginButton.config(text=user)
#                 self.cwin.destroy()
#             else:
#                 loginButton.config(text="Error")
#                 print("Error")
#                 self.cwin.destroy()

#         self.button_login = Button(self.cwin,text="Login",command=login) # need to change to real login compare from database

#         self.label_username.grid(row=0,column=0)
#         self.entry_username.grid(row=0,column=1)
#         self.label_password.grid(row=1,column=0)
#         self.entry_password.grid(row=1,column=1)
#         self.button_login.grid(row=2,column=1)