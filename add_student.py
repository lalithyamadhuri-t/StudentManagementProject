from tkinter import *
from db import get_connection

root = Tk()
root.title("Add Student")
root.geometry("1280x700+0+0")

def add():
    con = get_connection()
    cur = con.cursor()
    cur.execute(
        "INSERT INTO students(name, roll_no, course, phone) VALUES (%s,%s,%s,%s)",
        (name.get(), roll.get(), course.get(), phone.get())
    )
    con.commit()
    con.close()
    msg.config(text="Student Added Successfully")

Label(root, text="Name").grid(row=0, column=0)
Label(root, text="Roll No").grid(row=1, column=0)
Label(root, text="Course").grid(row=2, column=0)
Label(root, text="Phone").grid(row=3, column=0)

name = Entry(root)
roll = Entry(root)
course = Entry(root)
phone = Entry(root)

name.grid(row=0, column=1)
roll.grid(row=1, column=1)
course.grid(row=2, column=1)
phone.grid(row=3, column=1)

Button(root, text="Add", command=add).grid(row=4, column=1)
msg = Label(root, text="")
msg.grid(row=5, column=1)

root.mainloop()
