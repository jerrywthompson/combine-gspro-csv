import tkinter as tk
from tkinter import ttk, filedialog

class View:
    def __init__(self, root):
        self.root = root
        self.file_path = tk.StringVar()

        self.browse_button = tk.Button(root, text='Browse', command=self.open_file)
        self.browse_button.pack()

        self.file_entry = tk.Entry(root, textvariable=self.file_path)
        self.file_entry.pack()

        self.textbox = tk.Text(root)
        self.textbox.pack()


        self.add_row_button = tk.Button(root, text='Add Row')
        self.add_row_button.pack()

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[('CSV files', '*.csv')])
        self.file_path.set(file_path)
        return file_path

    def display_contents(self, contents):
        self.textbox.delete('1.0', tk.END)
        for row in contents:
            self.textbox.insert(tk.END, ', '.join(row) + '\n')

    def get_new_row(self):
        return self.textbox.get('1.0', tk.END).strip().split(',')

