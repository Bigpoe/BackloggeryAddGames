from scripts.extract_data_module.extract_data import ExtractDataObj
from tkinter.filedialog import askopenfilename, asksaveasfilename
from config.config import config_data

import pandas as pd
import tkinter as tk
import subprocess

extract = ExtractDataObj()
games_list = extract.extract_simple_data_from_csv()

execute_simple_option = config_data['simple_choice']
execute_detailed_option = config_data['detailed_choice']

## Functions description ##
def execute_simple():
    subprocess.run(execute_simple_option, shell=True)

def execute_detailed():
    subprocess.run(execute_detailed_option, shell=True)


def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.csv"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")

def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="csv",
        filetypes=[("Text Files", "*.csv"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {filepath}")


## Window build instructions ##
window = tk.Tk()
window.title('Backloggery Add Games')

## Window items ##
lbl_header = tk.Label(
    text='Hi there',
    width=10,
    height=2)

lbl_step_1 = tk.Label(
    text='Step 1 - Review the games in your CSV file',
    width=50,
    height=5)

txt_edit = tk.Text(window)

lbl_step_2 = tk.Label(
    text='Step 2 - Select between Simple or Detailed mode',
    width=50,
    height=5)

btn_button1 = tk.Button(
    text='Click here for simple option',
    command=execute_simple,
    width=30,
    height=2)

btn_button2 = tk.Button(
    text='Click here for detailed option',
    command=execute_detailed,
    width=30,
    height=2)

btn_open = tk.Button(
    text="Open CSV file", 
    command=open_file)

btn_save = tk.Button(
    text="Save CSV fiel changes", 
    command=save_file)

# games_list_textfield = tk.Text()

# for index, row in games_list.iterrows():
#     game_data_row = ",".join((row['game_name'], row['console_name'], row['progress_status'], row['progress_notes'], str(row['now_playing']), str(row['whishlist'])))
#     games_list_textfield.insert(tk.END, game_data_row + '\n')


## Pack window items ##
lbl_header.pack()
lbl_step_1.pack()
btn_open.pack()
btn_save.pack()
txt_edit.pack()
lbl_step_2.pack()
btn_button1.pack()
btn_button2.pack()
# games_list_textfield.pack()

window.mainloop()
