
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Coding\Python\StuManSys\build\assets\frame3")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def AttendancePage(st_id):
    from backend.setIsLate import isLate
    from backend.getStudent import getStudent
    from SearchStudentPage import SearchStudentPage
    from success import successPopUp
    from fail import failPopup


    studentInfo = getStudent(st_id) 


    def back_clicked():
        window.destroy()
        SearchStudentPage('LATE')

    def late_clicked():
        late = isLate(st_id)
        if late == 'RECORD UPDATED':
            window.destroy()
            successPopUp('Student is late', SearchStudentPage, 'LATE')
        else:
            window.destroy
            failPopup('Invalid Id', AttendancePage, st_id)




    window = Tk()

    window.geometry("934x554")
    window.configure(bg = "#979FB2")


    canvas = Canvas(
        window,
        bg = "#979FB2",
        height = 554,
        width = 934,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        467.0,
        277.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        466.0,
        277.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        466.0,
        66.0,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        467.0,
        277.0,
        image=image_image_4
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        466.0,
        277.0,
        image=image_image_5
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: back_clicked(),
        relief="flat"
    )
    button_1.place(
        x=43.0,
        y=45.0,
        width=154.736328125,
        height=63.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: late_clicked(),
        relief="flat"
    )
    button_2.place(
        x=72.0,
        y=386.0,
        width=253.0,
        height=63.0
    )

    canvas.create_text(
        73.0,
        244.0,
        anchor="nw",
        text="First Name: ",
        fill="#000000",
        font=("Inter", 28 * -1)
    )

    canvas.create_text(
        357.0,
        244.0,
        anchor="nw",
        text="Last Name: ",
        fill="#000000",
        font=("Inter", 28 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        199.5,
        309.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#FFFBFB",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=91.0,
        y=278.0,
        width=217.0,
        height=61.0
    )
    entry_1.insert(0, studentInfo['first_name'])

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        483.5,
        309.5,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#FFFBFB",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=375.0,
        y=278.0,
        width=217.0,
        height=61.0
    )
    entry_2.insert(0, studentInfo['last_name'])

    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(
        466.0,
        66.0,
        image=image_image_6
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        231.5,
        201.5,
        image=entry_image_3
    )
    entry_3 = Entry(
        bd=0,
        bg="#FFFBFB",
        fg="#000716",
        highlightthickness=0
    )
    entry_3.place(
        x=91.0,
        y=170.0,
        width=281.0,
        height=61.0
    )
    entry_3.insert(0, studentInfo['id'])

    canvas.create_text(
        73.0,
        119.0,
        anchor="nw",
        text="ID:",
        fill="#000000",
        font=("Inter", 28 * -1)
    )
    window.resizable(False, False)
    window.mainloop()

