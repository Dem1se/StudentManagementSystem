import json
import os
from tkinter import BOTTOM, END, NW, SINGLE, TOP, Button, Entry, Frame, Label, Listbox, Toplevel, messagebox
from tkcalendar import Calendar


def EnrollPage():
    def enroll_ok():
        try:
            profile = {
                "ID": int(id_box.get()),
                "Name": name_box.get(),
                "Class": int(class_box.get()),
                "Section": section_list.curselection()[0],
                "DOB": dob_box.get_date(),
                "ParentContact": int(contact_box.get())
            }
            dir_path = f"./StudentManagementSystem/data/profiles"
            file_path = dir_path + f"/{profile['ID']}.json"
            
            if (not os.path.exists(dir_path)):
                os.makedirs(dir_path)
            with open(file_path, "w") as f:
                f.write(json.dumps(profile, indent=4))

        except (IndexError, ValueError):
            messagebox.showerror(
                title="Invalid Input",
                message="Information provided is incorrect. Please re-check the details.")

        else:
            messagebox.showinfo(
                title="Success",
                message="Successfully enrolled new student.")
            window.destroy()

    window = Toplevel(height=600, width=500)
    window.title("Add New Student")

    id_label = Label(window, text="ID :", fg="#cc3333")
    id_label.place(anchor=NW, x=120, y=20)
    id_box = Entry(window)
    id_box.place(x=150, y=20)

    name_label = Label(window, text="Name :")
    name_label.place(anchor=NW, x=100, y=50)
    name_box = Entry(window)
    name_box.place(x=150, y=50)

    class_label = Label(window, text="Class :")
    class_label.place(anchor=NW, x=105, y=80)
    class_box = Entry(window)
    class_box.place(x=150, y=80)

    section_label = Label(window, text="Section :")
    section_label.place(anchor=NW, x=90, y=110)
    section_list = Listbox(window, selectmode=SINGLE, height=6)
    section_list.insert(0, " A")
    section_list.insert(END, " B")
    section_list.insert(END, " C")
    section_list.insert(END, " D")
    section_list.insert(END, " E")
    section_list.insert(END, " F")
    section_list.place(x=150, y=110)

    dob_label = Label(window, text="DOB :")
    dob_label.place(anchor=NW, x=105, y=220)
    dob_box = Calendar(window, selectmode="day", year=2000, month=3, day=10)
    dob_box.place(x=150, y=220)

    contact_label = Label(window, text="Parent Contact :")
    contact_label.place(anchor=NW, x=50, y=420)
    contact_box = Entry(window)
    contact_box.place(x=150, y=420)

    ok_button = Button(window, text="OK", command=enroll_ok)
    ok_button.place(x=240, y=520, width=90)
    cancel_button = Button(window, text="Cancel", command=window.destroy)
    cancel_button.place(x=340, y=520, width=90)
