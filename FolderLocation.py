
from tkinter import filedialog
import tkinter as tk


def getFolderList():

    root = tk.Tk()
    root.withdraw()
    root.call('wm', 'attributes', '.', '-topmost', True)
    files = filedialog.askopenfilename(multiple=True)

    var = root.tk.splitlist(files)
    filePaths = []
    for f in var:
        filePaths.append(f)
    filePaths

    return filePaths
