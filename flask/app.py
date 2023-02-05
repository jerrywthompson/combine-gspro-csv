from flask import Flask, request, render_template
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

@app.route("/")
def index():
    return render_template("index.html", mfg_list=mfg_list, ball_list=ball_list)

@app.route("/process", methods=["POST"])
def process():
    mfg_choice = request.form.get("mfg")
    ball_choice = request.form.get("ball")
    output_file = request.form.get("output_file")
    file_input = request.files.getlist("file_input")

    mfgName = config.get('Manufacture', mfg_choice)
    ballName = config.get('Ball', ball_choice)

    with open(output_file, 'a') as out_file:
        writer = csv.writer(out_file)
        if os.stat(output_file).st_size == 0:
            writer.writerow(output_file_header.split(","))
        for file in file_input:
            with open(file, 'r') as f:
                reader = csv.reader(f)
                ctr = 1
                for row in reader:
                    if ctr == 1:
                        ctr += 1
                        continue
                    else:
                        row.insert(0, ballName)
                        row.insert(0, mfgName)
                        writer.writerow(row)
            archiveFile(file.filename)
    return "Files processed"

def archiveFile(filepath):
    os.system(f"mv '{filepath}' {archiveDir}")

if __name__ == "__main__":
    app.run(debug=True)
