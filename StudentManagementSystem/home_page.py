from tkinter import N, Button, Tk
from enroll_page import EnrollPage
from mark_entry import MarkEntry
from mark_display import MarkDisplay


def HomePage():
    root = Tk()
    root.minsize(400, 300)
    root.title("Student Management System")

    enroll_button = Button(root, text="Add new student", command=EnrollPage, bg="#e38787").place(x=200, y=80, anchor=N)
    mark_entry = Button(root, text="Enter Marks", command=MarkEntry, bg="#e38787").place(x=200, y=130, anchor=N)
    enroll_button = Button(root, text="View Marks", command=MarkDisplay, bg="#e38787").place(x=200, y=180, anchor=N)

    root.mainloop()
