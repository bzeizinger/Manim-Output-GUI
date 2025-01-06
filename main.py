import tkinter as tk
from tkinter import ttk, filedialog as fd
from open_directory import open_directory

root = tk.Tk()
root.title("Manim Output GUI")
root.resizable(False, False)

directory = tk.StringVar(value="No directory selected")

selected_directory = ""

title1 = ttk.Label(
    root,
    text="Directory",
    font=(None, 20, "bold")
)
title1.pack(padx=10, pady=10)

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

title2 = ttk.Label(
    root,
    text="Show preview",
    font=(None, 20, "bold")
)
title2.pack(padx=10, pady=10)

show_preview_checkbox = ttk.Checkbutton(
    root,
    text="Show preview"
)
show_preview_checkbox.pack(padx=10, pady=10)

title3 = ttk.Label(
    root,
    text="Show preview",
    font=(None, 20, "bold")
)
title3.pack(padx=10, pady=10)

root.mainloop()
