import os
from tkinter import filedialog, messagebox

from model import Model
from view import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)

        self.mfg_list = self.model.mfg_list
        self.ball_list = self.model.ball_list

        # link the view
        self.view.select_file_button.config(command=self.select_input_file)
        self.view.mfg['values'] = self.mfg_list
        self.view.ball['values'] = self.ball_list
        self.view.output_file_button.config(command=self.select_output_file)
        self.view.db_file_button.config(command=self.select_database_file)
        self.view.process_button.config(command=self.main)

    def main(self):
        # Get values from gui
        self.view.results_text_box.delete("1.0", 'end')
        self.model.db_file_path = self.view.db_entrybox.get()
        self.model.output_csv_file_path = self.view.output_entrybox.get()
        self.model.mfg = self.model.config.get('Manufacture', self.view.mfg.get())
        self.model.ball = self.model.config.get('Ball', self.view.ball.get())

        # Create archive dir if they don't exists
        res = self.model.create_archive_dirs()
        self.view.results_text_box.insert('end', res)

        # Archive existing output, html and db fies
        res = self.model.archive_db_file()
        self.view.results_text_box.insert('end', res)
        res = self.model.archive_output_csv_file()
        self.view.results_text_box.insert('end', res)
        res = self.model.archive_html_file()
        self.view.results_text_box.insert('end', res)

        # Build and create output, html & db files
        res = self.model.create_output_file()
        self.view.results_text_box.insert('end', res)
        res = self.model.create_html_file()
        self.view.results_text_box.insert('end', res)
        res = self.model.create_db_file()
        self.view.results_text_box.insert('end', res)

        # Archive the input file
        res = self.model.archive_input_csv_file()
        self.view.results_text_box.insert('end', res)

        # Display script complete message
        self.view.results_text_box.insert('end', 'Script Complete')
        self.view.results_text_box.see('end')
        messagebox.showinfo("Info", "Script complete")

        return

    def run(self):
        self.view.run()

    def clear_results_textbox(self):
        self.view.results_text_box.delete("1.0", 'end')

    def write_to_results_text_box(self, data):
        self.view.results_text_box.insert('end', data)

    def select_input_file(self):
        self.model.input_file_path = filedialog.askopenfilename(filetypes=[('CSV files', '*.csv')])
        self.view.input_filepath_entrybox.delete(0, 'end')
        self.view.input_filepath_entrybox.insert(0, self.model.input_file_path)

    # noinspection SpellCheckingInspection
    def select_output_file(self):
        # Create a file selection dialog
        self.model.output_csv_file_path = str(filedialog.askopenfilenames(filetypes=[('CSV files', '*.csv')],
                                                                          initialdir='/run/user/1000/gvfs/smb-share:server=unraiddog.local,share=family/Jerry/Golf Exports/'))[
                                          2:-3]
        self.view.output_entrybox.delete(0, 'end')
        filename, file_extension = os.path.splitext(str(self.model.output_csv_file_path))
        if file_extension != '.csv':
            messagebox.showwarning("Warning", "You did not select a CSV file")
            return
        self.model.output_csv_file_name = os.path.basename(str(self.model.output_csv_file_path))
        self.view.output_entrybox.insert('end', self.model.output_csv_file_path)

    # noinspection SpellCheckingInspection
    def select_database_file(self):
        # Create a file selection dialog
        self.model.db_file_path = str(filedialog.askopenfilenames(filetypes=[('Database files', '*.db')],
                                                                  initialdir='/run/user/1000/gvfs/smb-share:server=unraiddog.local,share=family/Jerry/Golf Exports/'))[
                                  2:-3]
        self.view.db_entrybox.delete(0, 'end')
        filename, file_extension = os.path.splitext(str(self.model.db_file_path))
        if file_extension != '.db':
            messagebox.showwarning("Warning", "You did not select a DATABASE file")
            return
        self.model.db_file_name = os.path.basename(str(self.model.db_file_path))
        self.view.db_entrybox.insert('end', self.model.db_file_path)
