import tkinter as tk
from tkinter import ttk


class View:
    # noinspection SpellCheckingInspection
    def __init__(self, controller):
        self.controller = controller

        self.root = tk.Tk()
        self.root.title("Combine Excel Files")
        self.root.geometry("1000x800+400+10")
        self.root.configure(bg='lightsteelblue2', relief='raised')
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.font = ("Calibri", 12)
        self.font2 = ("Calibri", 16)
        self.rowCtr = 0

        # Create a button that will open the file selection dialog when clicked
        self.select_file_button = tk.Button(self.root, text="Select Input File")
        self.select_file_button.grid(row=self.rowCtr, column=0, sticky='w', padx=5, pady=20)

        self.select_folder_button = tk.Button(self.root, text="Select Input Folder")
        self.select_folder_button.grid(row=self.rowCtr, column=1, sticky='w', padx=5, pady=20)

        self.rowCtr = self.rowCtr + 1
        self.input_file_or_folder_path_entrybox = tk.Entry(self.root, width=70, font=self.font2)
        self.input_file_or_folder_path_entrybox.insert(0,self.controller.model.default_input_csv_folder)
        self.input_file_or_folder_path_entrybox.grid(row=self.rowCtr, column=0, sticky='ew', padx=5, pady=20, columnspan=2)

        self.rowCtr = self.rowCtr + 1
        self.mfg_label = ttk.Label(self.root, text="Manufacture:", font=self.font2)
        self.mfg_label.grid(row=self.rowCtr, column=0, sticky='w', padx=10, pady=10)

        self.mfg_var = tk.StringVar()
        self.mfg = ttk.Combobox(self.root, font=self.font2, width=50, textvariable=self.mfg_var)
        self.mfg.grid(row=self.rowCtr, column=1, pady=10)

        self.rowCtr = self.rowCtr + 2
        self.ball_label = ttk.Label(self.root, text="Ball:", font=self.font2)
        self.ball_label.grid(row=self.rowCtr, column=0, sticky='W', padx=10, pady=20)

        self.ball_var = tk.StringVar()
        self.ball = ttk.Combobox(self.root, width=50, font=self.font2, textvariable=self.ball_var)
        self.ball.grid(row=self.rowCtr, column=1, padx=5)

        self.rowCtr = self.rowCtr + 2
        self.output_file_button = tk.Button(self.root, text="Select Output CSV File")
        self.output_file_button.grid(row=self.rowCtr, column=0, sticky='w', padx=10, pady=20)

        self.output_file_var = tk.StringVar()
        self.output_entrybox = tk.Entry(self.root, width=70, font=self.font)
        self.output_entrybox.insert(0, self.controller.model.default_output_csv_file_path)
        self.output_entrybox.grid(row=self.rowCtr, column=1, padx=5, pady=20)

        self.rowCtr = self.rowCtr + 2
        self.db_file_button = tk.Button(self.root, text="Select Database File")
        self.db_file_button.grid(row=self.rowCtr, column=0, sticky='w', padx=10, pady=20)

        self.db_entrybox = tk.Entry(self.root, width=70, font=self.font)
        self.db_entrybox.insert(0, self.controller.model.default_db_file_path)
        self.db_entrybox.grid(row=self.rowCtr, column=1, padx=5, pady=20)

        self.rowCtr = self.rowCtr + 1
        self.results_text_box = tk.Text(self.root, height=20, width=125)
        self.results_text_box.grid(row=self.rowCtr, column=0, padx=10, pady=20, columnspan=2)

        self.rowCtr = self.rowCtr + 1
        self.process_button = tk.Button(self.root, text="Start")
        self.process_button.grid(row=self.rowCtr, column=0, sticky='w', padx=10, pady=5)

    def run(self):
        self.root.mainloop()
