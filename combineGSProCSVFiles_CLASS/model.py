import csv
import time
import configparser
import os
import pandas as pd
import sqlite3


class Model:
    def __init__(self, input_file_path='', archive_dir_path='', working_dir_path='', output_file_header='',
                 output_csv_file_name='', output_csv_file_path='', db_file_name='', db_file_path='', db_archive_dir='',
                 csv_archive_dir='', base_dir='', default_input_csv_file_dir='', default_output_csv_file_path='',
                 default_db_file_path='', mfg='', ball='', output_csv_file_data='', input_file_archive_dir='', html_file_archive_dir=''):
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
        self.input_filename = os.path.basename(str(self.input_file_path))
        return self.input_filename

    def create_archive_dirs(self):
        self.archive_dir_paths = self.config.options('Archive_Directories')
        self.working_dir_path = os.getcwd()
        for self.archive_dir_path in self.archive_dir_paths:
            fullPath = f'{self.working_dir_path}/{self.config.get("Archive_Directories", self.archive_dir_path)}'
            if not os.path.exists(fullPath):
                # Create a new directory because it does not exist
                os.makedirs(fullPath)
                return 'Archive directories created\n\n'
        return 'Archive directories already exists\n\n'

    def archive_db_file(self):
        self.db_archive_dir = self.config.get('Archive_Directories', 'db_files')
        # workingDir = os.path.dirname(dbFilePath)
        filename, file_extension = os.path.splitext(str(self.db_file_path))
        fileBaseName = os.path.basename(filename)
        newFilename = f'{self.working_dir_path}/{self.db_archive_dir}/{fileBaseName}_{self.timestamp}.db'
        os.system(f"cp '{self.db_file_path}' '{newFilename}'")
        # os.system(f"cp '{self.db_file_path}")
        # results_text_box.insert("insert", f'Database archived: {newFilename}\n\n')
        return f'Database archived: {newFilename}\n\n'

    def archive_output_csv_file(self):
        self.csv_archive_dir = self.config.get('Archive_Directories', 'output_csv')
        # workingDir = os.path.dirname(outputFilePath)
        filename, file_extension = os.path.splitext(str(self.output_csv_file_path))
        fileBaseName = os.path.basename(filename)
        newFilename = f'{self.working_dir_path}/{self.csv_archive_dir}/{fileBaseName}_{self.timestamp}.csv'
        os.system(f"cp '{self.output_csv_file_path}' '{newFilename}'")
        return f'CSV file archived: {newFilename}\n\n'

    def archive_html_file(self):
        self.html_archive_dir = self.config.get('Archive_Directories', 'html_files')
        # workingDir = os.path.dirname(outputFilePath)
        # filename, file_extension = os.path.splitext(str(self.ht))
        fileBaseName = self.config.get('File_Details', 'default_html_file_name')
        newFilename = f'{self.working_dir_path}/{self.html_archive_dir}/{fileBaseName}_{self.timestamp}.html'
        os.system(f"cp '{fileBaseName}' '{newFilename}'")
        os.system(f"mv '{fileBaseName}' '{self.working_dir_path}/{self.html_archive_dir}")
        return f'HTML file archived: {newFilename}\n\n'

    def create_output_file(self):
        self.timestamp = time.strftime("%Y%m%d-%H%M%S")
        print('yo')

        with open(self.input_file_path, 'r') as f:
            activeFile = csv.reader(f)
            row_ctr = 1

            for row in activeFile:
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
        #
        # create_db()
        # archiveRawFile(inputFilepath)
        # results_text_box.insert("insert", f'{ctr} row added to the file\n\nScript successfully completed')
        # print('done')

    def write_header(self):
        # global output_file_path
        # output_file_path = output_text_box.get("1.0","end-1c").replace('{','').replace('}', '')
        # output_file_name = '/run/user/1000/gvfs/smb-share:server=unraiddog.local,share=family/Jerry/Golf Exports/GSProCombinedFile.csv'
        if not os.path.isfile(self.output_csv_file_path):
            data = list(self.output_file_header.split(","))
            activeOutputFile = open(self.output_csv_file_path, 'a')
            writer = csv.writer(activeOutputFile)
            writer.writerow(data)
            activeOutputFile.close()
        return

    def write_output_csv_file(self):
        data = self.output_csv_file_data

        activeOutputFile = open(self.output_csv_file_path, 'a')
        writer = csv.writer(activeOutputFile)
        writer.writerow(data)

        activeOutputFile.close()

    def archive_input_csv_file(self):
        self.input_csv_archive_dir = self.config.get('Archive_Directories', 'input_csv')
        # workingDir = os.path.dirname(filepath)
        cmd = f"mv '{self.input_file_path }' '{self.working_dir_path}/{self.input_csv_archive_dir}'"
        # "mv '/data/user/Family/Jerry/Golf Exports/combineGSProCSV/combineGSProCSVFiles_CLASS/gspro-export02-03-23-17-03-05-5i-One Iron-Hex Tour.csv' '/data/user/Family/Jerry/Golf Exports/combineGSProCSV/combineGSProCSVFiles_CLASS/archives/input_csv_files"
        os.system(cmd)
        return f'Input file archived: {self.input_file_path }\n\n'
        # results_text_box.insert("insert", f'Raw file archived: {filepath}\n\n')

    def create_db_file(self):
        working_file = pd.read_csv(self.output_csv_file_path)
        # dbPath = dbFilePath
        # dbPath = '/run/user/1000/gvfs/smb-share:server=unraiddog.local,share=family/Jerry/Golf Exports/GSProCombinedFile.db'
        conn = sqlite3.connect(self.db_file_path)
        working_file.to_sql('results', conn, if_exists='replace', index=False)
        conn.close()
        return f'Database file updated\n\n'

    def create_html_file(self):
        # csvPath = '/run/user/1000/gvfs/smb-share:server=unraiddog.local,share=family/Jerry/Golf Exports/GSProCombinedFile.csv'

        df = pd.read_csv(self.output_csv_file_path)

        html_table = df.to_html(index=False, classes=["table", "table-striped", "table-bordered"])
        # workingDir = os.path.dirname(outputFilePath)
        filename, file_extension = os.path.splitext(str(self.output_csv_file_path))
        fileBaseName = os.path.basename(filename)
        htmlFileName = f'{self.working_dir_path}/{fileBaseName}.html'

        with open(htmlFileName, "w") as f:
            f.write(html_table)

        return f'HTML file created\n\n'

        #################################################
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
