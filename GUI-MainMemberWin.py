from tkinter import *

class RootWin() :
    def __init__(self) :
        root = Tk()
        
        header = Label(root, text="Main Menu")
        header.pack()
        
        searchButton = Button(root, text="Search by ID", command=self.popSearchWin)
        searchButton.pack(side=TOP)

        root.geometry('300x200')
        root.mainloop()
        
    def popSearchWin(self) :
        s1 = SearchWin("Product Search")

class SearchWin() :
    def __init__(self, title) :
        self.cwin = Toplevel()
        self.cwin.title(title)
        self.cwin.geometry('300x200')

        self.x = 0
        
        self.label_id=Label(self.cwin, text="Branch Name :")
        self.label_name=Label(self.cwin, text="Product Name :")

        self.entry_id=Entry(self.cwin)

        def popupSelect():
            self.sbwin = Tk()
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

        self.button_submit=Button(self.cwin, text ="SEARCH", command=self.cwin.destroy)
        self.button_exit=Button(self.cwin, text="EXIT", command=self.cwin.destroy)

        self.label_id.grid(row=0,column=0)
        self.label_name.grid(row=1,column=0)
        
        self.button_select.grid(row=0,column=1)
        self.entry_name.grid(row=1,column=1)

        self.button_submit.grid(row=2,column=1)
        self.button_exit.grid(row=3, column=1)

        self.label_status=Label(self.cwin, text="")
        self.label_status.grid(row=5, columnspan=2)


Mainmenu = RootWin()