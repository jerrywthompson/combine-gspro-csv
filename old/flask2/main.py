import tkinter as tk
from tkinter import filedialog, OptionMenu
from tkinter import ttk
import csv
import configparser
import os
import fileinput
from os.path import exists

config = configparser.ConfigParser()
config.read('config.ini')


def select_files():
    global filepaths

    filepaths = filedialog.askopenfilenames(initialdir = "/run/user/1000/gvfs/smb-share:server=unraiddog.local,share=family/Jerry/Golf Exports/")
    filepath_textbox.delete("1.0", tk.END)
    filepath_textbox.insert(tk.END, str(filepaths) + "\n")


root = tk.Tk()
root.title("Combine Excel Files")
root.geometry("600x400+200+200")


# Create a button that will open the file selection dialog when clicked
select_file_button = tk.Button(root, text="Select File(s)", command=select_files)
select_file_button.grid(row=5, column=0, sticky='W', padx=10,pady=5)


filepath_textbox = tk.Text(root, height=10, width=60, font=("Arial", 12))
filepath_textbox.grid(row=6, column=0, sticky='W', padx=10,pady=5)




root.mainloop()

