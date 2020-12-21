from tkinter import filedialog
from tkinter import *
root = Tk()
root.withdraw()
folder_selected = filedialog.askdirectory()
my_file = open("settings.ini","w")
my_file.write(folder_selected)