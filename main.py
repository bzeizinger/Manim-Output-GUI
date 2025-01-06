import tkinter as tk
from tkinter import ttk, filedialog as fd

root = tk.Tk()
root.title("Manim Output GUI")
root.resizable(False, False)

directory = tk.StringVar(value="No directory selected")

selected_directory = ""

show_preview_var = tk.BooleanVar(value=False)
quality_var = tk.StringVar(value="")  # Variable für Radiobuttons (Qualität)

def open_directory():
    selected_directory = fd.askdirectory()
    
    if selected_directory:
        directory.set(selected_directory)
        
    return selected_directory

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
    text="Show preview",
    variable=show_preview_var
)
show_preview_checkbox.pack(padx=10, pady=10)

title3 = ttk.Label(
    root,
    text="Quality",
    font=(None, 20, "bold")
)
title3.pack(padx=10, pady=10)

quality_frame = ttk.Frame(root)
quality_frame.pack(padx=10, pady=10)

low_quality_radiobutton = ttk.Radiobutton(
    quality_frame,
    text="480p",
    variable=quality_var,
    value="480p"
)
low_quality_radiobutton.pack(side="left", padx=5)

mid_quality_radiobutton = ttk.Radiobutton(
    quality_frame,
    text="1080p",
    variable=quality_var,
    value="1080p"
)
mid_quality_radiobutton.pack(side="left", padx=5)

high_quality_radiobutton = ttk.Radiobutton(
    quality_frame,
    text="2160p",
    variable=quality_var,
    value="2160p"
)
high_quality_radiobutton.pack(side="left", padx=5)

root.mainloop()