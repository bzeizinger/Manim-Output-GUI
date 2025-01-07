import tkinter as tk
from tkinter import ttk, filedialog as fd

root = tk.Tk()
root.title("Manim Output GUI")
root.resizable(False, False)

directory = tk.StringVar(value="No directory selected")

selected_directory = ""

show_preview_var = tk.BooleanVar(value=False)
save_last_frame_var = tk.BooleanVar(value=False)
transparent_background_var = tk.BooleanVar(value=False)
quality_var = tk.StringVar(value=False)

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

l_quality_radiobutton = ttk.Radiobutton(
    quality_frame,
    text="854x480 15FPS",
    variable=quality_var,
    value="854x480 15FPS"
)
l_quality_radiobutton.pack(side="left", padx=5)

m_quality_radiobutton = ttk.Radiobutton(
    quality_frame,
    text="1920x1080 60FPS",
    variable=quality_var,
    value="1920x1080 60FPS"
)
m_quality_radiobutton.pack(side="left", padx=5)

p_quality_radiobutton = ttk.Radiobutton(
    quality_frame,
    text="2560x1440 60FPS",
    variable=quality_var,
    value="2560x1440 60FPS"
)
p_quality_radiobutton.pack(side="left", padx=5)

k_quality_radiobutton = ttk.Radiobutton(
    quality_frame,
    text="3840x2160 60FPS",
    variable=quality_var,
    value="3840x2160 60FPS"
)
k_quality_radiobutton.pack(side="left", padx=5)

title4 = ttk.Label(
    root,
    text="Save last Frame",
    font=(None, 20, "bold")
)
title4.pack(padx=10, pady=10)

save_last_frame_checkbox = ttk.Checkbutton(
    root,
    text="Save last frame",
    variable=save_last_frame_var
)
save_last_frame_checkbox.pack(padx=10, pady=10)

title5 = ttk.Label(
    root,
    text="Transparent Background",
    font=(None, 20, "bold")
)
title5.pack(padx=10, pady=10)

transparent_background_checkbox = ttk.Checkbutton(
    root,
    text="Save last frame",
    variable=transparent_background_var
)
transparent_background_checkbox.pack(padx=10, pady=10)

run_button = ttk.Button(
    root,
    text="Run",
    # command=
)
run_button.pack(padx=20, pady=20)

root.mainloop()