import os
import json
from tkinter import NW, Label, Toplevel, Button, Entry, messagebox, StringVar


def MarkDisplay():

    phy = StringVar()
    chem = StringVar()
    maths = StringVar()
    eng = StringVar()
    comp = StringVar()

    def update_labels():
        dir_path = f"./StudentManagementSystem/data/marks"
        if (not os.path.exists(dir_path)):
            os.makedirs(dir_path)
        try:
            with open(f"./StudentManagementSystem/data/marks/{id_box.get()}.json", "r") as f:
                marks = json.loads(f.read())
                phy.set(marks["Physics"])
                chem.set(marks["Chemistry"])
                maths.set(marks["Maths"])
                eng.set(marks["English"])
                comp.set(marks["ComputerScience"])
        except FileNotFoundError:
            messagebox.showerror(
                title="ID Not Found",
                message="Marks for student of given ID not found. Please re-check or enter the marks first.")

    window = Toplevel(height=300, width=500)
    window.title("View marks of students")

    Label(window, text="ID :", fg="#cc3333").place(anchor=NW, x=120, y=20)
    id_box = Entry(window)
    id_box.place(x=200, y=20)

    ok_button = Button(window, text="View", command=update_labels)
    ok_button.place(x=330, y=15, width=90)

    Label(window, text="Phyics :").place(anchor=NW, x=120, y=50)
    phy_box = Label(window, textvariable=phy)
    phy_box.place(x=250, y=50)
    Label(window, text="/100").place(x=300, y=50)

    Label(window, text="Chemistry :").place(anchor=NW, x=120, y=80)
    chem_box = Label(window, textvariable=chem)
    chem_box.place(x=250, y=80)
    Label(window, text="/100").place(x=300, y=80)

    Label(window, text="Maths :").place(anchor=NW, x=120, y=110)
    math_box = Label(window, textvariable=maths)
    math_box.place(x=250, y=110)
    Label(window, text="/100").place(x=300, y=110)

    Label(window, text="English :").place(anchor=NW, x=120, y=140)
    eng_box = Label(window, textvariable=eng)
    eng_box.place(x=250, y=140)
    Label(window, text="/100").place(x=300, y=140)

    Label(window, text="Comp Sci :").place(anchor=NW, x=120, y=170)
    comp_box = Label(window, textvariable=comp)
    comp_box.place(x=250, y=170)
    Label(window, text="/100").place(x=300, y=170)

    cancel_button = Button(window, text="Close", command=window.destroy)
    cancel_button.place(x=210, y=230, width=90)
