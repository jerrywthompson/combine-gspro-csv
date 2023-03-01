import tkinter as tk
import pandas as pd
import sqlite3
from tkinter import filedialog, OptionMenu, messagebox
from tkinter import ttk
import csv
import configparser
import os
import time

# if os.environ.get('DISPLAY','') == '':
#     print('no display found. Using :0.0')
#     os.environ.__setitem__('DISPLAY', ':0.0')

timestamp = time.strftime("%Y%m%d-%H%M%S")

config = configparser.ConfigParser()
config.read('config.ini')

output_file_header = config.get('Output_File', 'header')
# output_file_data = ""
mfg_list = config.options('Manufacture')
ball_list = config.options('Ball')


def createArchiveDir():
    archiveDir = config.options('Archive_Directories')
    workingDir = os.path.dirname(inputFilepath)
    for dirPath in archiveDir:
        fullPath = f'{workingDir}/{config.get("Archive_Directories", dirPath)}'
        if not os.path.exists(fullPath):
            # Create a new directory because it does not exist
            os.makedirs(fullPath)


def writeHeader():
    # global output_file_path
    # output_file_path = output_text_box.get("1.0","end-1c").replace('{','').replace('}', '')
    # output_file_name = '/run/user/1000/gvfs/smb-share:server=unraiddog.local,share=family/Jerry/Golf Exports/GSProCombinedFile.csv'
    if not os.path.isfile(outputFilePath):
        data = list(output_file_header.split(","))
        activeOutputFile = open(outputFilePath, 'a')
        writer = csv.writer(activeOutputFile)
        writer.writerow(data)
        activeOutputFile.close()
    return


def writeOutput():
    global activeOutputFile

    data = output_file_data

    activeOutputFile = open(outputFilePath, 'a')
    # activeOutputFile = open('/run/user/1000/gvfs/smb-share:server=unraiddog.local,share=family/Jerry/Golf Exports/GSProCombinedFile.csv', 'a')
    writer = csv.writer(activeOutputFile)
    writer.writerow(data)
    # for data_list in outputFileData:
    # writer.writerow(outputFileData)
    activeOutputFile.close()


def archiveRawFile(filepath):
    archiveDir = config.get('Archive_Directories', 'raw_files')
    workingDir = os.path.dirname(filepath)
    os.system(f"mv '{filepath}' '{workingDir}/{archiveDir}'")
    results_text_box.insert("insert", f'Raw file archived: {filepath}\n\n')


def archiveCSVFile():
    archiveDir = config.get('Archive_Directories', 'csv_files')
    workingDir = os.path.dirname(outputFilePath)
    filename, file_extension = os.path.splitext(str(outputFilePath))
    fileBaseName = os.path.basename(filename)
    newFilename = f'{workingDir}/{archiveDir}/{fileBaseName}_{timestamp}.csv'
    os.system(f"cp '{outputFilePath}' '{newFilename}'")
    results_text_box.insert("insert", f'CSV file archived: {newFilename}\n\n')


def archiveDBFile():
    archiveDir = config.get('Archive_Directories', 'db_files')
    workingDir = os.path.dirname(dbFilePath)
    filename, file_extension = os.path.splitext(str(dbFilePath))
    fileBaseName = os.path.basename(filename)
    newFilename = f'{workingDir}/{archiveDir}/{fileBaseName}_{timestamp}.db'
    os.system(f"cp '{dbFilePath}' '{newFilename}'")
    results_text_box.insert("insert", f'Database archived: {newFilename}\n\n')


def select_files():
    global inputFilepath

    results_text_box.delete("insert", tk.END)

    inputFilepath = str(filedialog.askopenfilenames(
        initialdir="/run/user/1000/gvfs/smb-share:server=unraiddog.local,share=family/Jerry/Golf Exports/"))[2:-3]
    # filename, file_extension = os.path.splitext(str(inputFilepath)[:-3])
    inputFilename = os.path.basename(str(inputFilepath))
    filepath_entrybox.delete(0, tk.END)
    filepath_entrybox.insert(tk.END, str(inputFilename))


def select_output_file():
    global outputFilePath
    # Create a file selection dialog
    outputFilePath = str(filedialog.askopenfilenames(
        initialdir='/run/user/1000/gvfs/smb-share:server=unraiddog.local,share=family/Jerry/Golf Exports/'))[2:-3]
    output_entrybox.delete(0, tk.END)
    filename, file_extension = os.path.splitext(str(outputFilePath))
    if file_extension != '.csv':
        messagebox.showwarning("Warning", "You did not select a CSV file")
        return
    outputFilename = os.path.basename(str(outputFilePath))
    output_entrybox.insert(tk.END, outputFilename)


def select_database_file():
    global dbFilePath
    # Create a file selection dialog
    dbFilePath = str(filedialog.askopenfilenames(
        initialdir='/run/user/1000/gvfs/smb-share:server=unraiddog.local,share=family/Jerry/Golf Exports/'))[2:-3]
    db_entrybox.delete(0, tk.END)
    filename, file_extension = os.path.splitext(str(dbFilePath))
    if file_extension != '.db':
        messagebox.showwarning("Warning", "You did not select a DATABASE file")
        return
    dbFilename = os.path.basename(str(dbFilePath))
    db_entrybox.insert(tk.END, dbFilename)


def create_db():
    df = pd.read_csv(outputFilePath)
    # dbPath = dbFilePath
    # dbPath = '/run/user/1000/gvfs/smb-share:server=unraiddog.local,share=family/Jerry/Golf Exports/GSProCombinedFile.db'
    conn = sqlite3.connect(dbFilePath)
    df.to_sql('results', conn, if_exists='replace', index=False)
    results_text_box.insert("insert", "Database created")
    conn.close()


def createTable():
    csvPath = '/run/user/1000/gvfs/smb-share:server=unraiddog.local,share=family/Jerry/Golf Exports/GSProCombinedFile.csv'

    df = pd.read_csv(inputFilepath)

    html_table = df.to_html(index=False, classes=["table", "table-striped", "table-bordered"])
    workingDir = os.path.dirname(outputFilePath)
    filename, file_extension = os.path.splitext(str(outputFilePath))
    fileBaseName = os.path.basename(filename)
    htmlFileName = f'{workingDir}/{fileBaseName}_{timestamp}.html'

    with open(htmlFileName, "w") as f:
        f.write(html_table)


def process_files():
    global timestamp

    timestamp = time.strftime("%Y%m%d-%H%M%S")
    results_text_box.delete("insert", tk.END)
    createArchiveDir()
    archiveDBFile()
    archiveCSVFile()

    # for filepath in inputFilepath:
    global output_file_data
    ctr = 1

    mfgKey = mfg.get()
    mfgName = config.get('Manufacture', mfgKey)
    ballKey = ball.get()
    ballName = config.get('Ball', ballKey)

    with open(inputFilepath, 'r') as f:
        activeFile = csv.reader(f)

        for row in activeFile:
            # ignore header row
            if ctr == 1:
                writeHeader()
            else:
                row.insert(0, ballName)
                row.insert(0, mfgName)
                output_file_data = row

                writeOutput()
            ctr += 1

    archiveRawFile(inputFilepath)
    results_text_box.insert("insert", f'{ctr} row added to the file\n\nScript successfully completed')
    print('done')


root = tk.Tk()
root.title("Combine Excel Files")
root.geometry("1400x1000+400+400")

# Create a button that will open the file selection dialog when clicked
select_file_button = tk.Button(root, text="Select Input File", command=select_files)
select_file_button.grid(row=0, column=0, sticky='w', padx=5, pady=20)

filepath_entrybox = tk.Entry(root, width=50)
filepath_entrybox.grid(row=0, column=1, padx=5, pady=20)

mfg_label = ttk.Label(root, text="Manufacture:", font=("Times New Roman", 10))
mfg_label.grid(row=2, column=0, sticky='w', padx=10, pady=20)

mfg_var = tk.StringVar()
mfg = ttk.Combobox(root, width=50, textvariable=mfg_var)
# Adding combobox drop down list
mfg['values'] = mfg_list
mfg.grid(row=2, column=1, pady=20)
# default value
# mfg.current(2)

ball_label = ttk.Label(root, text="Ball:", font=("Times New Roman", 10))
ball_label.grid(row=4, column=0, sticky='W', padx=10, pady=20)

ball_var = tk.StringVar()
ball = ttk.Combobox(root, width=50, textvariable=ball_var)
# Adding combobox drop down list
ball['values'] = ball_list
ball.grid(row=4, column=1, padx=5)

output_file_button = tk.Button(root, text="Select Output CSV File", command=select_output_file)
output_file_button.grid(row=6, column=0, sticky='w', padx=10, pady=20)
output_file_var = tk.StringVar()
output_entrybox = tk.Entry(root, width=50)
output_entrybox.grid(row=6, column=1, padx=5, pady=20)
# output_text_box.insert(0,'/run/user/1000/gvfs/smb-share:server=unraiddog.local,share=family/Jerry/Golf Exports/GSProCombinedFile.csv')

db_file_button = tk.Button(root, text="Select Database File", command=select_database_file)
db_file_button.grid(row=8, column=0, sticky='w', padx=10, pady=20)

db_entrybox = tk.Entry(root, width=50)
db_entrybox.grid(row=8, column=1, padx=5, pady=20)

results_text_box = tk.Text(root, height="15")
results_text_box.grid(row=10, column=0, padx=10, pady=20, columnspan=2)
# results_text_box.insert(0,'/run/user/1000/gvfs/smb-share:server=unraiddog.local,share=family/Jerry/Golf Exports/GSProCombinedFile.csv')


process_button = tk.Button(root, text="Start", command=process_files)
process_button.grid(row=12, column=0, sticky='w', padx=10, pady=5)

root.mainloop()
