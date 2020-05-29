import tkinter as tk
import subprocess

execute_simple_option = 'python -m pytest ./scripts/add_games/add_game_simple.py --show-capture=stdout -v -s'
execute_detailed_option = 'python -m pytest ./scripts/add_games/add_game_detailed.py --show-capture=stdout -v -s'
# execute_detailed_option = 'cd ../../ && la'

def execute_simple():
    subprocess.run(execute_simple_option, shell=True)

def execute_detailed():
    subprocess.run(execute_detailed_option, shell=True)


## Window build instructions ##
window = tk.Tk()

window.title('Backloggery Add Games')

lbl_header = tk.Label(
    text='Hi there',
    width=10,
    height=10)

btn_button1 = tk.Button(
    text='Click here for simple option',
    command=execute_simple_option,
    width=50,
    height=5)

btn_button2 = tk.Button(
    text='Click here for detailed option',
    command=execute_detailed_option,
    width=50,
    height=5)

lbl_header.pack()
btn_button1.pack()
btn_button2.pack()

window.mainloop()
