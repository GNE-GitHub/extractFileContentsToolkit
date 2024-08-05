import os
import tkinter as tk
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText

def extract_file_contents(project_dir):
    """
    Extracts the contents of all files in the specified project directory
    and its subdirectories and returns them as a single string.
    """
    file_contents = ""
    for root, dirs, files in os.walk(project_dir):
        for filename in files:
            file_path = os.path.join(root, filename)
            if os.path.isfile(file_path):
                try:
                    with open(file_path, "r", encoding="utf-8") as input_file:
                        content = input_file.read()
                except UnicodeDecodeError:
                    try:
                        with open(file_path, "r", encoding="latin-1") as input_file:
                            content = input_file.read()
                    except UnicodeDecodeError:
                        content = "Error reading file due to encoding issues."
                file_contents += f"########################################{file_path}\n########################################\n{content}########################################\n"
    return file_contents

def select_folder():
    global selected_folder
    selected_folder = filedialog.askdirectory()
    if selected_folder:
        display_file_contents()

def display_file_contents():
    global selected_folder
    file_contents = extract_file_contents(selected_folder)
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, file_contents)

def copy_content():
    file_contents = text_area.get("1.0", tk.END)
    root.clipboard_clear()
    root.clipboard_append(file_contents.strip())
    print("Content copied to clipboard!")

# Create the main window
root = tk.Tk()
root.title("Automatic Folder Selection and File Content Display")

# Create the select folder button
select_folder_button = tk.Button(root, text="Select Folder", command=select_folder)
select_folder_button.pack(pady=10)

# Create the text area to display file contents
text_area = ScrolledText(root, width=80, height=20, wrap=tk.WORD)
text_area.pack(pady=10)

# Create the copy content button
copy_content_button = tk.Button(root, text="Copy Content", command=copy_content)
copy_content_button.pack(pady=10)

root.mainloop()
