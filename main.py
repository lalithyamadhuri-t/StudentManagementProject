from tkinter import *
import os

window = Tk()
window.title("Student Management System")
window.geometry("1280x700+0+0")

Label(
    window,
    text="STUDENT MANAGEMENT SYSTEM",
    font=("Arial", 24)
).pack(pady=40)

def open_modify():
    os.system("python modify.py")

def open_view():
    os.system("python view_student.py")

Button(
    window,
    text="Modify Students",
    width=25,
    height=2,
    command=open_modify
).pack(pady=20)

Button(
    window,
    text="View Students",
    width=25,
    height=2,
    command=open_view
).pack(pady=20)

window.mainloop()
