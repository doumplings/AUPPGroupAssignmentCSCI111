
from pathlib import Path
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Coding\Python\StuManSys\build\assets\frame4")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def addStudentPage():
    from fail import failPopup;
    from success import successPopUp;
    from backend.addStudent import addStudent;
    from backend.getNewStudentId import getNewStudentId;
    from StudentHomePage import StudentHomePage

    id = getNewStudentId()

    def submit_handler():
        first_name = entry_4.get()
        last_name = entry_5.get()
        email = entry_2.get()
        dob = entry_6.get()
        phonenum = entry_3.get()
        isStudentAdded = addStudent(id, first_name, last_name, email, phonenum, dob)
        if isStudentAdded == 'RECORD INSERTED':
            window.destroy()
            successPopUp('Successfully added new student', addStudentPage)
        else: 
            window.destroy()
            failPopup('Failed to add new student', addStudentPage)
            
        
    def back_clicked():
        window.destroy()
        StudentHomePage()
        


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

    backbtnimage = PhotoImage(
        file=relative_to_assets("button_1.png"))
    backbtn = Button(
        image=backbtnimage,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: back_clicked(),
        relief="flat"
    )
    backbtn.place(
        x=43.0,
        y=45.0,
        width=154.736328125,
        height=63.0
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(
        469.0,
        66.0,
        image=image_image_6
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        185.5,
        189.5,
        image=entry_image_1
    )

    canvas.create_text(
        77.0,
        170.0,
        anchor="nw",
        text= id,
        fill="#000000",
        font=("Inter", 28 * -1)
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        326.0,
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
        x=77.0,
        y=278.0,
        width=498.0,
        height=61.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        326.0,
        433.5,
        image=entry_image_3
    )
    entry_3 = Entry(
        bd=0,
        bg="#FFFBFB",
        fg="#000716",
        highlightthickness=0
    )
    entry_3.place(
        x=77.0,
        y=402.0,
        width=498.0,
        height=61.0
    )

    canvas.create_text(
        364.0,
        40.0,
        anchor="nw",
        text="Add Student",
        fill="#000000",
        font=("Inter", 28 * -1)
    )

    canvas.create_text(
        59.0,
        124.0,
        anchor="nw",
        text="ID: ",
        fill="#000000",
        font=("Inter", 28 * -1)
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        469.5,
        189.5,
        image=entry_image_4
    )
    entry_4 = Entry(
        bd=0,
        bg="#FFFBFB",
        fg="#000716",
        highlightthickness=0
    )
    entry_4.place(
        x=361.0,
        y=158.0,
        width=217.0,
        height=61.0
    )

    canvas.create_text(
        343.0,
        124.0,
        anchor="nw",
        text="First Name: ",
        fill="#000000",
        font=("Inter", 28 * -1)
    )

    canvas.create_text(
        59.0,
        243.0,
        anchor="nw",
        text="Email:",
        fill="#000000",
        font=("Inter", 28 * -1)
    )

    canvas.create_text(
        59.0,
        368.0,
        anchor="nw",
        text="Phone Number:",
        fill="#000000",
        font=("Inter", 28 * -1)
    )

    entry_image_5 = PhotoImage(
        file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(
        753.5,
        189.5,
        image=entry_image_5
    )
    entry_5 = Entry(
        bd=0,
        bg="#FFFBFB",
        fg="#000716",
        highlightthickness=0
    )
    entry_5.place(
        x=645.0,
        y=158.0,
        width=217.0,
        height=61.0
    )

    entry_image_6 = PhotoImage(
        file=relative_to_assets("entry_6.png"))
    entry_bg_6 = canvas.create_image(
        753.5,
        309.5,
        image=entry_image_6
    )
    entry_6 = Entry(
        bd=0,
        bg="#FFFBFB",
        fg="#000716",
        highlightthickness=0
    )
    entry_6.place(
        x=645.0,
        y=278.0,
        width=217.0,
        height=61.0
    )

    canvas.create_text(
        627.0,
        124.0,
        anchor="nw",
        text="Last Name: ",
        fill="#000000",
        font=("Inter", 28 * -1)
    )

    canvas.create_text(
        627.0,
        243.0,
        anchor="nw",
        text="Date of birth:",
        fill="#000000",
        font=("Inter", 28 * -1)
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: submit_handler(),
        relief="flat"
    )
    button_2.place(
        x=627.0,
        y=402.0,
        width=253.0,
        height=63.0
    )
    window.resizable(False, False)
    window.mainloop()
