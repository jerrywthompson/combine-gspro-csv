from tkinter import filedialog, OptionMenu
import tkinter as tk
from tkinter import ttk
import csv
import configparser
import fileinput



config = configparser.ConfigParser()
config.read('config.ini')
mfg_list = config.options('Manufacture')
ball_list = config.options('Ball')





def select_files():
    filepath_textbox.delete("1.0", tk.END)
    # Create a file selection dialog
    filepaths = filedialog.askopenfilenames()
    
    #for filepath in filepaths:
     #   with open(filepath, "r") as file:
      #      contents = file.read()
       #     print(f"filePath: {filepath}")
            # perform the desired operation on the file contents
        # Insert filepaths into the textbox
    for filepath in filepaths:
        filepath_textbox.insert(tk.END, filepath + "\n")


                # Read the contents of the first CSV file
        with open(filepath, "r") as file1:
            reader1 = csv.reader(file1)
            output = [row for row in reader1]

        # Combine the data from both files
        #rows = rows1 + rows2

        # Write the resulting data to a new CSV file
        with open("result.csv", "w") as result:
            writer = csv.writer(result)
            writer.writerows(output)

        print('done')
        
    

root = tk.Tk()
root.title("Combine Excel Files")
root.geometry("600x400+200+200")
#root.grid_rowconfigure(0, weight=1)
#root.grid_columnconfigure(0, weight=1)



# Create a button that will open the file selection dialog when clicked
select_file_button = tk.Button(root, text="Select File(s)", command=select_files)
select_file_button.grid(row=0, column=0, sticky='W', padx=10,pady=5)

filepath_textbox = tk.Text(root, height=10, width=60, font=("Arial", 12))
filepath_textbox.grid(row=1, column=0, sticky='W', padx=10,pady=5)

mfg_label = ttk.Label(root, text = "Manufacture:", font = ("Times New Roman", 10))
mfg_label.grid(row=5,column=0, sticky='W', padx=5, pady=5)

mfg_var = tk.StringVar()
mfg = ttk.Combobox(root, width = 27, textvariable = mfg_var)  
# Adding combobox drop down list
mfg['values'] = mfg_list
mfg.grid(row=5,column=0, padx=5)  
# Shows february as a default value
mfg.current(2)

ball_label = ttk.Label(root, text = "Ball:", font = ("Times New Roman", 10))
ball_label.grid(row=6,column=0, sticky='W', padx=5, pady=5)

ball_var = tk.StringVar()
ball = ttk.Combobox(root, width = 27, textvariable = ball_var)  
# Adding combobox drop down list
ball['values'] = ball_list
ball.grid(row=6,column=0, padx=5)  
# Shows february as a default value
#ball.current(2)



root.mainloop()
