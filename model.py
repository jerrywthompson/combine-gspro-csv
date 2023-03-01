import configparser
import csv
import os
import sqlite3
import time
from datetime import datetime
from tkinter import messagebox
import pandas as pd
import prettytable
from dataclasses import dataclass
import os
import configparser
import time
from prettytable import from_db_cursor


@dataclass
class Model:
    input_file_path: str = ''
    input_folder_path: str = ''
    archive_dir_path: str = ''
    working_dir_path: str = ''
    db_file_path: str = ''
    output_csv_file_name: str = ''
    output_csv_file_path: str = ''
    db_file_name: str = ''
    db_archive_dir: str = ''
    csv_archive_dir: str = ''
    mfg: str = ''
    ball: str = ''
    output_csv_file_data: str = ''
    input_file_archive_dir: str = ''
    practice_session_dt_tm: str = ''
    html_file_archive_dir: str = ''
    html_header: str = ''
    html_footer: str = ''
    default_html_filename: str = ''

    def __post_init__(self):
        self.input_filename = os.path.basename(str(self.input_file_path))
        self.timestamp = time.strftime("%Y%m%d-%H%M%S")
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.practice_session_dt_tm = None
        self.output_file_header = self.config.get('File_Details', 'header')
        self.mfg_list = self.config.options('Manufacture')
        self.ball_list = self.config.options('Ball')
        self.default_input_csv_file_dir = self.config.get("File_Details", 'default_input_csv_file_dir')
        self.base_dir = os.getcwd()
        self.default_output_csv_file_path = os.path.join(self.base_dir, self.config.get("File_Details",
                                                                                        'default_output_csv_file_name'))
        self.default_db_file_path = os.path.join(self.base_dir, self.config.get("File_Details", 'default_db_file_name'))
        self.default_html_filename = self.config.get("File_Details", 'default_html_file_name')


    # def get_input_file_name(self):
    #     return self.input_filename

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

    def archive_duplicate_output_csv_file(self):
        self.csv_archive_dir = self.config.get('Archive_Directories', 'output_csv')
        filename, file_extension = os.path.splitext(str(self.output_csv_file_path))
        file_base_name = os.path.basename(filename)
        new_file_name = f'{self.working_dir_path}/{self.csv_archive_dir}/duplicates/{file_base_name}_{self.timestamp}.csv'
        os.system(f"cp '{self.output_csv_file_path}' '{new_file_name}'")
        return f'CSV file archived: {new_file_name}\n\n'

    def archive_html_file(self):
        self.html_archive_dir = self.config.get('Archive_Directories', 'html_files')
        file_base_name = self.config.get('File_Details', 'default_html_file_name')
        new_file_name = f"'{self.working_dir_path}/{self.html_archive_dir}/{file_base_name}_{self.timestamp}.html'"
        mvCmd = f"mv {file_base_name} {new_file_name}"
        os.system(mvCmd)
        return f'HTML file archived: {new_file_name}\n\n'

    def create_output_file(self):
        self.timestamp = time.strftime("%Y%m%d-%H%M%S")
        date_format = "%m-%d-%y-%H-%M-%S"
        print(self.input_file_path)
        self.practice_session_dt_tm = datetime.strptime(str(self.practice_session_dt_tm), date_format)

        with open(self.input_file_path, 'r') as f:
            active_file = csv.reader(f)
            row_ctr = 1

            try:
                for row in active_file:
                    # ignore header row
                    if row_ctr == 1:
                        self.write_header()
                    else:
                        # Round values to one decimal
                        formatted_row = []
                        for value in row:
                            # Round numbers to one decimal point
                            try:
                                workingValue = float(value)
                                rounded_value = round(workingValue, 1)
                                formatted_row.append(round(rounded_value, 1))
                            except:
                                formatted_row.append(value)

                        formatted_row.insert(0, self.practice_session_dt_tm)
                        formatted_row.insert(0, self.config.get('Ball', self.ball))
                        formatted_row.insert(0, self.config.get('Manufacture', self.mfg))
                        self.output_csv_file_data = formatted_row
                        self.write_output_csv_file()
                    row_ctr += 1
            except:
                errMsg = f'Issue with this file: {self.input_file_path}  skipping....'
                print(errMsg)
                messagebox.showwarning("Warning", errMsg)
                return False

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

    def create_html_fileORIG(self):
        df = pd.read_csv(self.output_csv_file_path)

        html_table = df.to_html(index=False, classes=["table", "table-striped", "table-bordered"])
        filename, file_extension = os.path.splitext(str(self.output_csv_file_path))
        file_base_name = os.path.basename(filename)
        html_file_name = f'{self.working_dir_path}/{file_base_name}.html'

        with open(html_file_name, "w") as f:
            f.write(html_table)

        return f'HTML file created\n\n'

    def create_html_file(self):
        filename = self.input_filename
        html_file_path = f'{self.working_dir_path}/{self.default_html_filename}'

        csv_file = open(self.output_csv_file_path, 'r')
        data = csv_file.readlines()
        column_names = data[0].split(',')
        table = prettytable.PrettyTable()
        table.field_names = column_names
        # table.add_row(column_names)
        for i in range(1, len(data)):
            row = data[i].split(',')
            table.add_row(row)
        html_table = table.get_html_string(attributes={"id": "datatypes", "class": "display"})

        html_header = self.get_header()
        html_footer = self.get_footer()

        with open(html_file_path, "w", encoding='utf-8') as f:
            f.write(html_header)
            f.write(html_table)
            f.write(html_footer)

        return f'HTML file created\n\n'

    def create_html_views(self):
        if not os.path.exists('views'):
            # Create a new directory because it does not exist
            os.makedirs('views')

        # connect to the SQLite database
        conn = sqlite3.connect(self.db_file_path)

        for file in os.listdir('sql/'):
            # Open the SQL file and read the query from it
            with open(f'sql/{file}', 'r') as f:
                query = f.read()

            # print(f'query: {query}')
            # print(f'file: {file}')

            # execute a SQL query
            cursor = conn.execute(query)
            # create a pretty table from the query results
            table = from_db_cursor(cursor)
            filename = file[:-4]
            # print(f'View filename: {filename}')
            html_view_file_path = f'views/{filename}.csv'
            with open(html_view_file_path, 'w') as f:
                f.write(table.get_string())

        return 'HTML views created'

    def get_filename_from_path(self):
        filename, file_extension = os.path.splitext(str(self.input_file_path))
        self.input_filename = filename
        return

    def get_details_from_filename(self):
        self.get_timestamp_from_filename()
        if self.check_for_duplicate_files():
            messagebox.showinfo("Warning", f"File is a duplicate.  Skipping: \n{self.input_filename}")
            return False

        self.get_filename_from_path()
        mfgStatus = self.get_mfg_from_filename()
        if not mfgStatus:
            messagebox.showinfo("Warning",
                                f"Manufacture missing from raw file or name does not match config file...\n{self.input_filename}")
            return False

        ballStatus = self.get_ball_from_filename()
        if not ballStatus:
            messagebox.showinfo("Warning",
                                f"Ball missing from raw file or name does not match config file...\n{self.input_filename}")
            return False
        return

    def get_timestamp_from_filename(self):
        self.get_filename_from_path()
        start = self.input_file_path.find('export') + 6
        end = start + 17
        self.practice_session_dt_tm = self.input_filename[start:end]
        return

    def get_mfg_from_filename(self):
        for activeMfg in self.config.options('Manufacture'):
            if activeMfg.lower() in self.input_file_path.lower():
                self.mfg = activeMfg
                return True

        self.mfg = False
        return False

    def get_ball_from_filename(self):
        for activeBall in self.config.options('Ball'):
            if activeBall.lower() in self.input_file_path.lower():
                self.ball = activeBall
                return True

        self.ball = False
        return False

    def check_for_duplicate_files(self):
        with open(self.output_csv_file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if self.practice_session_dt_tm in row:
                    print(f'File {self.input_filename} has already been added')
                    self.archive_duplicate_output_csv_file()
                    return True

    def get_header(self):
        self.html_header = f"""<html>
        <head>
            <link rel="stylesheet" type="text/css"
                  href="https://cdn.datatables.net/1.13.2/css/jquery.dataTables.min.css">
            <link rel="stylesheet" type="text/css"
                  href="https://cdn.datatables.net/buttons/2.3.4/css/buttons.dataTables.min.css">
        </head>
        <body>
            <p>
                {self.default_html_filename}
            </p>
            """
        return self.html_header

    def get_footer(self):
        self.html_footer = """
                <script type="text/javascript" charset="utf8" src="https://code.jquery.com/jquery-3.5.1.js"></script>
                <script type="text/javascript" charset="utf8"
                        src="https://cdn.datatables.net/1.13.2/js/jquery.dataTables.min.js"></script>
                <script type="text/javascript" charset="utf8"
                        src="https://code.jquery.com/jquery-3.5.1.js"></script>
                <script type="text/javascript" charset="utf8"
                        src="https://cdn.datatables.net/1.13.2/js/jquery.dataTables.min.js"></script>
                <script type="text/javascript" charset="utf8"
                        src="https://cdn.datatables.net/buttons/2.3.4/js/dataTables.buttons.min.js"></script>
                <script type="text/javascript" charset="utf8"
                        src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.1.3/jszip.min.js"></script>
                <script type="text/javascript" charset="utf8"
                        src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.53/pdfmake.min.js"></script>
                <script type="text/javascript" charset="utf8"
                        src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.53/vfs_fonts.js"></script>
                <script type="text/javascript" charset="utf8"
                        src="https://cdn.datatables.net/buttons/2.3.4/js/buttons.html5.min.js"></script>
                <script type="text/javascript" charset="utf8"
                        src="https://cdn.datatables.net/buttons/2.3.4/js/buttons.print.min.js"></script>
                <script>
                    $('#datatypes').dataTable( {
                        "order": [],
                        dom: 'Bfrtip',
                        buttons: [
                            'copy', 'csv', 'excel', 'pdf', 'print'
                        ],
                        dom: 'Blfrtip',
                        "lengthMenu": [ [10, 25, 50, -1], [10, 25, 50, "All"] ]
                    });
                </script>
            </body>
        </html>"""

        return self.html_footer
