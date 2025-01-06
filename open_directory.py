def open_directory():
    selected_directory = fd.askdirectory()
    
    if selected_directory:
        directory.set(selected_directory)
        
    return selected_directory