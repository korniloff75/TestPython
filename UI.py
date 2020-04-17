from tkinter import *
from tkinter import messagebox
# import tkinter

root = Tk()
# root = tkinter.Tk()
root.title("Графическая программа на Python")
root.geometry("400x300+300+250")

clicks = 0


def click_button():
	global clicks
	clicks += 1
	root.title("Clicks {}".format(clicks))

btn = Button(text="Click Me", background="#555", foreground="#ccc", padx="20", pady="8", font="16", command=click_button)

def edit_click():
	messagebox.showinfo("GUI Python", "Нажата опция Edit")

main_menu = Menu()

file_menu = Menu()
file_menu.add_command(label="New")
file_menu.add_command(label="Save")
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit")

main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Edit", command=edit_click)
main_menu.add_cascade(label="View")

root.config(menu=main_menu)

btn.pack()

root.mainloop()