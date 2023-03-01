import tkinter as tk
from view import View
from model import Model

class Controller:
    def __init__(self):
        self.root = tk.Tk()
        self.view = View(self.root)
        self.model = Model()



        self.view.browse_button.config(command=self.load_file)
        # self.view.add_row_button.config(command=self.add_row)

    def run(self):
        self.root.mainloop()

    def load_file(self):
        file_path = self.view.open_file()
        if file_path:
            contents = self.model.load_file(file_path)
            self.view.display_contents(contents)

    def add_row(self):
        file_path = self.view.file_path.get()
        if file_path:
            new_row = self.view.get_new_row()
            self.model.add_row(file_path, new_row)
            self.load_file()