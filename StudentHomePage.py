
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Coding\Python\StuManSys\build\assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def StudentHomePage():
    from HomePage import HomePage
    from AddStudentPage import addStudentPage
    from AttendancePage import AttendancePage
    from SearchStudentPage import SearchStudentPage
    
    window = Tk()

    window.geometry("934x554")
    window.configure(bg = "#979FB2")

    def backbtn_clicked():
        window.destroy()
        HomePage()

    def search_clicked():
        window.destroy()
        SearchStudentPage()
    
    def add_clicked():
        window.destroy()
        addStudentPage()
    
    def delete_clicked():
        window.destroy()
        SearchStudentPage('DELETE')
    
    def update_clicked():
        window.destroy()
        SearchStudentPage('UPDATE')
    
    def attendance_clicked():
        window.destroy()
        SearchStudentPage('LATE')
    


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

    backbtnimage = PhotoImage(
        file=relative_to_assets("backbtn.png"))
    backbtn = Button(
        image=backbtnimage,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: backbtn_clicked(),
        relief="flat"
    )
    backbtn.place(
        x=43.0,
        y=45.0,
        width=154.736328125,
        height=63.0
    )

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

    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(
        466.0,
        66.0,
        image=image_image_6
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: search_clicked(),
        relief="flat"
    )
    button_1.place(
        x=95.0,
        y=159.0,
        width=198.0,
        height=96.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: add_clicked(),
        relief="flat"
    )
    button_2.place(
        x=368.0,
        y=159.0,
        width=198.0,
        height=96.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: delete_clicked(),
        relief="flat"
    )
    button_3.place(
        x=641.0,
        y=159.0,
        width=198.0,
        height=96.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: update_clicked(),
        relief="flat"
    )
    button_4.place(
        x=95.0,
        y=317.0,
        width=198.0,
        height=96.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: attendance_clicked(),
        relief="flat"
    )
    button_5.place(
        x=367.0,
        y=317.0,
        width=198.0,
        height=96.0
    )
    window.resizable(False, False)
    window.mainloop()
