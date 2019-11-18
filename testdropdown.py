from tkinter import *

root = Tk()
branchName = ""
optionLists = ["b1","b2","b3","b4","b5","b6"]
root.geometry('250x300')

variable = StringVar(root)
variable.set(optionLists[0])

label_branch = Label(root,text="Branch :")

opt = OptionMenu(root,variable,*optionLists)

variable.trace_add("write",lambda *args : print(variable.get()))

def callback():
    branchName = variable.get()
    print(branchName)
    root.destroy()
button_exit = Button(root,text="EXIT",command=callback)


label_branch.grid(row=0,column=0)
opt.grid(row=0,column=1)
button_exit.grid(row=1,column=1)
window = root.mainloop()