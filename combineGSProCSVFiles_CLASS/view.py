import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import os

class View:
    def __init__(self, controller):
        self.controller = controller

        self.root = tk.Tk()
        self.root.title("Combine Excel Files")
        self.root.geometry("1000x750+400+100")
        self.font = ("Calibri", 12)
        self.font2 = ("Calibri", 16)


        # Create a button that will open the file selection dialog when clicked
        self.select_file_button = tk.Button(self.root, text="Select Input File")
        # self.select_file_button = tk.Button(self.root, text="Select Input File", command=self.select_file)
        self.select_file_button.grid(row=0, column=0, sticky='w', padx=5, pady=20)

        self.input_filepath_entrybox = tk.Entry(self.root, width=70, font=self.font)
        self.input_filepath_entrybox.grid(row=0, column=1,sticky='w', padx=5, pady=20)

        self.mfg_label = ttk.Label(self.root, text="Manufacture:", font=self.font2)
        self.mfg_label.grid(row=2, column=0, sticky='w', padx=10, pady=20)

        self.mfg_var = tk.StringVar()
        self.mfg = ttk.Combobox(self.root, font=self.font2, width=50, textvariable=self.mfg_var)
        # Adding combobox drop down list
        # self.mfg['values'] = self.controller.mfg_list
        self.mfg.grid(row=2, column=1, pady=20)
        # default value
        # mfg.current(2)
        #
        self.ball_label = ttk.Label(self.root, text="Ball:", font=self.font2)
        self.ball_label.grid(row=4, column=0, sticky='W', padx=10, pady=20)

        self.ball_var = tk.StringVar()
        self.ball = ttk.Combobox(self.root, width=50, font=self.font2, textvariable=self.ball_var)
        # Adding combobox drop down list
        # self.ball['values'] = self.controller.ball_list
        self.ball.grid(row=4, column=1, padx=5)

        self.output_file_button = tk.Button(self.root, text="Select Output CSV File")
        self.output_file_button.grid(row=6, column=0, sticky='w', padx=10, pady=20)

        self.output_file_var = tk.StringVar()
        self.output_entrybox = tk.Entry(self.root, width=70, font=self.font)
        self.output_entrybox.insert(0, self.controller.model.default_output_csv_file_path)
        self.output_entrybox.grid(row=6, column=1, padx=5, pady=20)

        # self.default_db_file_name
        # self.default_db_file_name
        # # output_text_box.insert(0,'/run/user/1000/gvfs/smb-share:server=unraiddog.local,share=family/Jerry/Golf Exports/GSProCombinedFile.csv')
        #self.default_db_file_name
        self.db_file_button = tk.Button(self.root, text="Select Database File")
        self.db_file_button.grid(row=8, column=0, sticky='w', padx=10, pady=20)

        self.db_entrybox = tk.Entry(self.root, width=70, font=self.font)
        self.db_entrybox.insert(0, self.controller.model.default_db_file_path )
        self.db_entrybox.grid(row=8, column=1, padx=5, pady=20)


        self.results_text_box = tk.Text(self.root, height="20")
        self.results_text_box.grid(row=9, column=0, padx=10, pady=20, columnspan=5)
        # results_text_box.insert(0,'/run/user/1000/gvfs/smb-share:server=unraiddog.local,share=family/Jerry/Golf Exports/GSProCombinedFile.csv')
        #
        self.process_button = tk.Button(self.root, text="Start")
        self.process_button.grid(row=10, column=0, sticky='w', padx=10, pady=5)

   ########################################################################

    #
    #     self.file_path = tk.StringVar()
    #
    #     self.browse_button = tk.Button(root, text='Browse', command=self.open_file)
    #     self.browse_button.pack()
    #
    #     self.file_entry = tk.Entry(root, textvariable=self.file_path)
    #     self.file_entry.pack()
    #
    #     self.textbox = tk.Text(root)
    #     self.textbox.pack()
    #
    #
    #     self.add_row_button = tk.Button(root, text='Add Row')
    #     self.add_row_button.pack()
    #

        # return file_path




    # def display_contents(self, contents):
    #     self.textbox.delete('1.0', tk.END)
    #     for row in contents:self.input_filepath_entrybox
    #         self.textbox.insert(tk.END, ', '.join(row) + '\n')
    #
    # def get_new_row(self):
    #     return self.textbox.get('1.0', tk.END).strip().split(',')

    def run(self):
        self.root.mainloop()