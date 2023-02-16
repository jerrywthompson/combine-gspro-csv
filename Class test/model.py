import csv
import tkinter as tk
from tkinter import filedialog

class Model:

    # def __init__(self):
    #     self.input_file_path = ""
    #
    # def open_file(self):
    #     input_file_path = filedialog.askopenfilename(filetypes=[('CSV files', '*.csv')])
    #     self.input_file_path = input_file_path
    #     # return file_path


    def load_file(self, file_path):
        contents = []
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                contents.append(row)
        return contents

    def add_row(self, file_path, new_row):
        with open(file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(new_row)