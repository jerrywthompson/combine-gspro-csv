from flask import Flask, request
import tkinter as tk
import csv
import configparser
import os

app = Flask(__name__)
config = configparser.ConfigParser()
config.read('config.ini')

output_file_header = config.get('Output_File','header')
mfg_list = config.options('Manufacture')
ball_list = config.options('Ball')

archiveDir = 'archives'
if not os.path.exists(archiveDir):
   os.makedirs(archiveDir)

def writeHeader():
    global output_file_path
    output_file_path = request.form['output_text_box']
    if not os.path.isfile(output_file_path):
        data = list(output_file_header.split(","))
        activeOutputFile = open(output_file_path, 'a')
        writer = csv.writer(activeOutputFile)
        writer.writerow(data)
        activeOutputFile.close()
    return

def writeOutput():
    global activeOutputFile
    data = output_file_data
    activeOutputFile = open(output_file_path, 'a')
    writer = csv.writer(activeOutputFile)
    writer.writerow(data)
    activeOutputFile.close()

def archiveFile(filepath):
    os.system(f"mv '{filepath}' {archiveDir}")

def process_files():
    for filepath in filepaths:
        global output_file_data
        ctr = 1
        mfgKey = request.form['mfg']
        mfgName = config.get('Manufacture', mfgKey)
        ballKey = request.form['ball']
        ballName = config.get('Ball', ballKey)
        with open(filepath, 'r') as f:
            activeFile = csv.reader(f)
            for row in activeFile:
                if ctr == 1:
                    writeHeader()
                else:
                    row.insert(0, ballName)
                    row.insert(0, mfgName)
                    output_file_data = row
                    writeOutput()
                ctr += 1
        archiveFile(filepath)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        global filepaths
        filepaths = request.form.getlist('filepaths')
        process_files()
        return 'File updated'
    return '''
        <form method="post">
            Manufacture: <select name="mfg">
                {0}
            </select><br>
            Ball: <select name="ball">
                {1}
            </select><br>
            <textarea name="filepaths" placeholder="Select files"></textarea><br>
            <textarea name="output_text_box" placeholder="Select
