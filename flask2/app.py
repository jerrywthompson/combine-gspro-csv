from flask import Flask, render_template
import tkinter as tk
from tkinter import filedialog, OptionMenu
from tkinter import ttk
import csv
import configparser
import os
import fileinput
from os.path import exists

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('config.ini')

filepaths = []

def select_files():
    global filepaths

    filepaths = filedialog.askopenfilenames(initialdir = "/run/user/1000/gvfs/smb-share:server=unraiddog.local,share=family/Jerry/Golf Exports/")

@app.route('/')
def index():
    select_files()
    return render_template('index.html', filepaths=filepaths)

if __name__ == '__main__':
    app.run(debug=True)
