from tkinter import * 
from tkinter.ttk import *

class Window(): 
    def __init__(self):
        super().__init__()(self, master)
        master.geometry("320x240")
        frame = Frame(master)
        yscroll = Scrollbar(frame, orient=VERTICAL)
        xscroll = Scrollbar(frame, orient=HORIZONTAL)
        frame.pack(fill=BOTH, expand=YES)
        yscroll.pack(side=RIGHT)
        xscroll.pack(side=BOTTOM)

        canvas = Canvas(frame)
        canvas['yscrollcommand'] = yscroll.set
        canvas['xscrollcommand'] = xscroll.set
        yscroll['command'] = canvas.yview
        xscroll['command'] = canvas.xview
    
        canvas.configure(scrollregion=canvas.bbox("all"))
        for x in range(100):
            Label(frame, text="Label "+str(x)).pack()

Window(Tk())