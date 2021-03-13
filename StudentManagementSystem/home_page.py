from tkinter import TOP, BOTTOM, Frame, Button, Toplevel
from enroll_page import EnrollPage

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
                
        self.MarkEntry = Button(self, text="Enter Marks", command=self.mark_in_page)
        self.MarkEntry.pack(side=TOP, pady=5)
        
        self.enroll_button = Button(self, text="View Marks", command=self.mark_out_page)
        self.enroll_button.pack(side=BOTTOM, pady=5)
    
    def mark_in_page(self):
        window = Toplevel(height=500, width=400)
        window.title("Enter Student's Marks")
        
    def mark_out_page(self):
        window = Toplevel(height=500, width=400)
        window.title("View Student's Marks")
