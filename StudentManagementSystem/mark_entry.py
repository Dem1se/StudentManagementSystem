import os
import json
from tkinter import NW, Toplevel, Entry, Button, Label, messagebox


def MarkEntry():
    def mark_ok():
        try:
            marks = {
                "ID": int(id_box.get()),
                "Physics": int(phy_box.get()),
                "Chemistry": int(chem_box.get()),
                "Maths": int(math_box.get()),
                "English": int(eng_box.get()),
                "ComputerScience": int(comp_box.get())
            }
            dir_path = f"./StudentManagementSystem/data/marks"
            marks_file_path = dir_path + f"/{marks['ID']}.json"
            profile_file_path = f"./StudentManagementSystem/data/profiles/{marks['ID']}.json"
            
            # Make sure a student with the given ID exists first
            if (not os.path.exists(profile_file_path)):
                raise StudentNotFoundError

            # Make sure all the marks are under 100
            for key in marks:
                if (key != "ID"):
                    if (marks[key] > 100):
                        raise ValueError

            if (not os.path.exists(dir_path)):
                os.makedirs(dir_path)
            with open(marks_file_path, "w") as f:
                f.write(json.dumps(marks, indent=4))

        except (IndexError, ValueError):
            messagebox.showerror(
                title="Invalid Input",
                message="Information provided is incorrect. Please re-check the details.")
        except StudentNotFoundError:
            messagebox.showerror(
                title="Invalid Input",
                message="Student with given ID does not exist. Please re-check the ID or enroll the student first.")
        else:
            messagebox.showinfo(
                title="Success",
                message="Successfully recorded marks.")
            window.destroy()

    window = Toplevel(height=300, width=500)
    window.title("Input marks of students")

    id_label = Label(window, text="ID :", fg="#cc3333")
    id_label.place(anchor=NW, x=120, y=20)
    id_box = Entry(window)
    id_box.place(x=200, y=20)

    phy_label = Label(window, text="Phyics :")
    phy_label.place(anchor=NW, x=120, y=50)
    phy_box = Entry(window)
    phy_box.place(x=200, y=50)
    Label(window, text="/100").place(x=300, y=50)

    chem_label = Label(window, text="Chemistry :")
    chem_label.place(anchor=NW, x=120, y=80)
    chem_box = Entry(window)
    chem_box.place(x=200, y=80)
    Label(window, text="/100").place(x=300, y=80)

    math_label = Label(window, text="Maths :")
    math_label.place(anchor=NW, x=120, y=110)
    math_box = Entry(window)
    math_box.place(x=200, y=110)
    Label(window, text="/100").place(x=300, y=110)

    eng_label = Label(window, text="English :")
    eng_label.place(anchor=NW, x=120, y=140)
    eng_box = Entry(window)
    eng_box.place(x=200, y=140)
    Label(window, text="/100").place(x=300, y=140)

    comp_label = Label(window, text="Comp Sci :")
    comp_label.place(anchor=NW, x=120, y=170)
    comp_box = Entry(window)
    comp_box.place(x=200, y=170)
    Label(window, text="/100").place(x=300, y=170)

    ok_button = Button(window, text="OK", command=mark_ok)
    ok_button.place(x=100, y=230, width=90)
    cancel_button = Button(window, text="Cancel", command=window.destroy)
    cancel_button.place(x=210, y=230, width=90)

class StudentNotFoundError(Exception):
    def __str__(self):
        return "Student profile of given ID does not exist."
