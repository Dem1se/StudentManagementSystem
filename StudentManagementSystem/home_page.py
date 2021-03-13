from tkinter import TOP, BOTTOM, Frame, Button, Toplevel
from enroll_page import EnrollPage
from mark_entry import MarkEntry
class HomePage(Frame):
    # TODO: force only one toplevel window at a time
    # currently multiple instances are allowed

    def __init__(self, master=None):
        Frame.__init__(self, master, width=400, height=400)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.enroll_button = Button(self, text="Add new student", command=EnrollPage)
        self.enroll_button.pack(side=TOP, pady=5, fill="x")
                
        self.MarkEntry = Button(self, text="Enter Marks", command=MarkEntry)
        self.MarkEntry.pack(side=TOP, pady=5)
        
        self.enroll_button = Button(self, text="View Marks")
        self.enroll_button.pack(side=BOTTOM, pady=5)

