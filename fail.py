
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Coding\Python\StuManSys\build\assets\fail")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def failPopup(errMessage, newWindow, param= None):

    window = Tk()

    window.geometry("349x175")
    window.configure(bg = "#FFFFFF")
    def back_handler():
        window.destroy()
        if param != None:
            newWindow(param)
        else:
            newWindow()

    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 175,
        width = 349,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        174.0,
        87.0,
        image=image_image_1
    )


    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: back_handler(),
        relief="flat"
    )
    button_1.place(
        x=250.0,
        y=112.0,
        width=80,
        height=40
    )


    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        110.0,
        87.0,
        image=image_image_2
    )

    canvas.create_text(
        164.0,
        29.0,
        anchor="nw",
        text="FAILED",
        fill="#000000",
        font=("Inter", 28 * -1)
    )

    canvas.create_text(
        180.0,
        96.0,
        anchor="nw",
        text=errMessage,
        fill="#000000",
        font=("Inter", 16 * -1)
    )
    window.resizable(False, False)
    window.mainloop()
