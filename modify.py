from tkinter import *
import os

root = Tk()
root.title("Modify Students")
root.geometry("1280x700+0+0")

Label(
    root,
    text="Modify Student Records",
    font=("Arial", 20)
).pack(pady=30)

def add_student():
    os.system("python add_student.py")

def update_student():
    os.system("python update_student.py")

def delete_student():
    os.system("python delete_student.py")

Button(
    root,
    text="Add Student",
    width=20,
    height=2,
    command=add_student
).pack(pady=10)

Button(
    root,
    text="Update Student",
    width=20,
    height=2,
    command=update_student
).pack(pady=10)

Button(
    root,
    text="Delete Student",
    width=20,
    height=2,
    command=delete_student
).pack(pady=10)

root.mainloop()
