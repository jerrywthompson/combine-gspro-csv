import configparser
import csv
import os
import sqlite3
import time

import pandas as pd


class Model:
    def __init__(self, input_file_path='', archive_dir_path='', working_dir_path='', db_file_path='',
                 output_csv_file_name='', output_csv_file_path='', db_file_name='', db_archive_dir='',
                 csv_archive_dir='', mfg='', ball='', output_csv_file_data='', input_file_archive_dir='',
                 html_file_archive_dir=''):

        self.input_file_path = None
        self.html_archive_dir = None
        self.input_csv_archive_dir = None
        self.archive_dir_paths = None
        self.input_filename = os.path.basename(str(self.input_file_path))
        self.timestamp = time.strftime("%Y%m%d-%H%M%S")

        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

        self.input_file_path = input_file_path
        self.output_file_header = self.config.get('File_Details', 'header')
        self.mfg_list = self.config.options('Manufacture')
        self.mfg = mfg
        self.ball_list = self.config.options('Ball')
        self.ball = ball
        self.output_csv_file_name = output_csv_file_name
        self.output_csv_file_path = output_csv_file_path
        self.output_csv_file_data = output_csv_file_data
        self.db_file_name = db_file_name
        self.db_file_path = db_file_path
        self.working_dir_path = working_dir_path
        self.base_dir = os.getcwd()
        self.default_input_csv_file_dir = self.config.get("File_Details", 'default_input_csv_file_dir')
        self.default_output_csv_file_path = os.path.join(self.base_dir, self.config.get("File_Details",
                                                                                        'default_output_csv_file_name'))
        self.default_db_file_path = os.path.join(self.base_dir, self.config.get("File_Details", 'default_db_file_name'))
        self.archive_dir_path = archive_dir_path
        self.csv_archive_dir = csv_archive_dir
        self.db_archive_dir = db_archive_dir
        self.input_file_archive_dir = input_file_archive_dir
        self.html_file_archive_dir = html_file_archive_dir

    def get_input_file_name(self):
        return self.input_filename

    def create_archive_dirs(self):
        self.archive_dir_paths = self.config.options('Archive_Directories')
        self.working_dir_path = os.getcwd()
        for self.archive_dir_path in self.archive_dir_paths:
            full_path = f'{self.working_dir_path}/{self.config.get("Archive_Directories", self.archive_dir_path)}'
            if not os.path.exists(full_path):
                # Create a new directory because it does not exist
                os.makedirs(full_path)
                return 'Archive directories created\n\n'
        return 'Archive directories already exists\n\n'

    def archive_db_file(self):
        self.db_archive_dir = self.config.get('Archive_Directories', 'db_files')
        filename, file_extension = os.path.splitext(str(self.db_file_path))
        file_base_name = os.path.basename(filename)
        new_file_name = f'{self.working_dir_path}/{self.db_archive_dir}/{file_base_name}_{self.timestamp}.db'
        os.system(f"cp '{self.db_file_path}' '{new_file_name}'")
        return f'Database archived: {new_file_name}\n\n'

    def archive_output_csv_file(self):
        self.csv_archive_dir = self.config.get('Archive_Directories', 'output_csv')
        filename, file_extension = os.path.splitext(str(self.output_csv_file_path))
        file_base_name = os.path.basename(filename)
        new_file_name = f'{self.working_dir_path}/{self.csv_archive_dir}/{file_base_name}_{self.timestamp}.csv'
        os.system(f"cp '{self.output_csv_file_path}' '{new_file_name}'")
        return f'CSV file archived: {new_file_name}\n\n'

    def archive_html_file(self):
        self.html_archive_dir = self.config.get('Archive_Directories', 'html_files')
        file_base_name = self.config.get('File_Details', 'default_html_file_name')
        new_file_name = f'{self.working_dir_path}/{self.html_archive_dir}/{file_base_name}_{self.timestamp}.html'
        os.system(f"mv '{file_base_name}' '{self.working_dir_path}/{self.html_archive_dir}")
        return f'HTML file archived: {new_file_name}\n\n'

    def create_output_file(self):
        self.timestamp = time.strftime("%Y%m%d-%H%M%S")
        print('yo')

        with open(self.input_file_path, 'r') as f:
            active_file = csv.reader(f)
            row_ctr = 1

            for row in active_file:
                # ignore header row
                if row_ctr == 1:
                    self.write_header()
                else:
                    row.insert(0, self.ball)
                    row.insert(0, self.mfg)
                    self.output_csv_file_data = row
                    self.write_output_csv_file()
                row_ctr += 1
        return f'Output file created\n\n'

    def write_header(self):
        if not os.path.isfile(self.output_csv_file_path):
            data = list(self.output_file_header.split(","))
            active_output_file = open(self.output_csv_file_path, 'a')
            writer = csv.writer(active_output_file)
            writer.writerow(data)
            active_output_file.close()
        return

    def write_output_csv_file(self):
        data = self.output_csv_file_data

        active_output_file = open(self.output_csv_file_path, 'a')
        writer = csv.writer(active_output_file)
        writer.writerow(data)

        active_output_file.close()

    def archive_input_csv_file(self):
        self.input_csv_archive_dir = self.config.get('Archive_Directories', 'input_csv')
        cmd = f"mv '{self.input_file_path}' '{self.working_dir_path}/{self.input_csv_archive_dir}'"
        os.system(cmd)
        return f'Input file archived: {self.input_file_path}\n\n'

    def create_db_file(self):
        working_file = pd.read_csv(self.output_csv_file_path)
        conn = sqlite3.connect(self.db_file_path)
        working_file.to_sql('results', conn, if_exists='replace', index=False)
        conn.close()
        return f'Database file updated\n\n'

    def create_html_file(self):
        df = pd.read_csv(self.output_csv_file_path)

        html_table = df.to_html(index=False, classes=["table", "table-striped", "table-bordered"])
        filename, file_extension = os.path.splitext(str(self.output_csv_file_path))
        file_base_name = os.path.basename(filename)
        html_file_name = f'{self.working_dir_path}/{file_base_name}.html'

        with open(html_file_name, "w") as f:
            f.write(html_table)

        return f'HTML file created\n\n'
