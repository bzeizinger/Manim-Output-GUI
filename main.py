import tkinter as tk
from tkinter import ttk, filedialog as fd

root = tk.Tk()
root.title("Manim Output GUI")

directory = tk.StringVar(value="No directory selected")

selected_directory = ""

def open_directory():
    selected_directory = fd.askdirectory()
    
    if selected_directory:
        directory.set(selected_directory)
        
    return selected_directory

select_directory_button = ttk.Button(
    root,
    text="Select Directory",
    command=open_directory
)
select_directory_button.pack(padx=10, pady=10)

directory_label = ttk.Label(
    root,
    textvariable=directory
)
directory_label.pack(padx=10, pady=10)

root.mainloop()