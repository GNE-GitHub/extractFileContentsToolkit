# import os
# import tkinter as tk
# from tkinter import filedialog
# from tkinter.scrolledtext import ScrolledText

# def extract_file_contents(project_dir):
#     """
#     Extracts the contents of all files in the specified project directory
#     and its subdirectories and returns them as a single string.
#     """
#     file_contents = ""
#     for root, dirs, files in os.walk(project_dir):
#         for filename in files:
#             file_path = os.path.join(root, filename)
#             if os.path.isfile(file_path):
#                 try:
#                     with open(file_path, "r", encoding="utf-8") as input_file:
#                         content = input_file.read()
#                 except UnicodeDecodeError:
#                     try:
#                         with open(file_path, "r", encoding="latin-1") as input_file:
#                             content = input_file.read()
#                     except UnicodeDecodeError:
#                         content = "Error reading file due to encoding issues."
#                 file_contents += f"########################################{file_path}\n########################################\n{content}########################################\n"
#     return file_contents

# def select_folder():
#     global selected_folder
#     selected_folder = filedialog.askdirectory()
#     if selected_folder:
#         display_file_contents()

# def display_file_contents():
#     global selected_folder
#     file_contents = extract_file_contents(selected_folder)
#     text_area.delete("1.0", tk.END)
#     text_area.insert(tk.END, file_contents)

# def copy_content():
#     file_contents = text_area.get("1.0", tk.END)
#     root.clipboard_clear()
#     root.clipboard_append(file_contents.strip())
#     print("Content copied to clipboard!")

# # Create the main window
# root = tk.Tk()
# root.title("Automatic Folder Selection and File Content Display")

# # Create the select folder button
# select_folder_button = tk.Button(root, text="Select Folder", command=select_folder)
# select_folder_button.pack(pady=10)

# # Create the text area to display file contents
# text_area = ScrolledText(root, width=80, height=20, wrap=tk.WORD)
# text_area.pack(pady=10)

# # Create the copy content button
# copy_content_button = tk.Button(root, text="Copy Content", command=copy_content)
# copy_content_button.pack(pady=10)

# root.mainloop()

# import os
# import tkinter as tk
# from tkinter import filedialog
# from tkinter.scrolledtext import ScrolledText

# def extract_file_contents(project_dir, file_types):
#     """
#     Extracts the contents of all files in the specified project directory
#     and its subdirectories that match the file types and returns them as a single string.
#     """
#     file_contents = ""
#     for root, dirs, files in os.walk(project_dir):
#         for filename in files:
#             if file_types:
#                 if not any(filename.endswith(ft.strip()) for ft in file_types.split(',')):
#                     continue  # Skip files that don't match the specified file types
            
#             file_path = os.path.join(root, filename)
#             if os.path.isfile(file_path):
#                 try:
#                     with open(file_path, "r", encoding="utf-8") as input_file:
#                         content = input_file.read()
#                 except UnicodeDecodeError:
#                     try:
#                         with open(file_path, "r", encoding="latin-1") as input_file:
#                             content = input_file.read()
#                     except UnicodeDecodeError:
#                         content = "Error reading file due to encoding issues."
#                 except PermissionError:
#                     content = "Error: Permission denied."
#                 except Exception as e:
#                     content = f"Unexpected error: {str(e)}"
#                 file_contents += f"########################################{file_path}\n########################################\n{content}\n########################################\n"
#     return file_contents

# def select_folder():
#     global selected_folder
#     selected_folder = filedialog.askdirectory()
#     if selected_folder:
#         display_file_contents()

# def display_file_contents():
#     global selected_folder
#     file_types = file_type_entry.get()
#     file_contents = extract_file_contents(selected_folder, file_types)
#     text_area.delete("1.0", tk.END)
#     text_area.insert(tk.END, file_contents)

# def copy_content():
#     file_contents = text_area.get("1.0", tk.END)
#     root.clipboard_clear()
#     root.clipboard_append(file_contents.strip())
#     print("Content copied to clipboard!")

# # Create the main window
# root = tk.Tk()
# root.title("Automatic Folder Selection and File Content Display")

# # Create the select folder button
# select_folder_button = tk.Button(root, text="Select Folder", command=select_folder)
# select_folder_button.pack(pady=10)

# # Create the file type entry field and label
# file_type_label = tk.Label(root, text="Enter file types (e.g., .txt, .py):")
# file_type_label.pack(pady=5)
# file_type_entry = tk.Entry(root, width=50)
# file_type_entry.pack(pady=5)

# # Create the text area to display file contents
# text_area = ScrolledText(root, width=80, height=20, wrap=tk.WORD)
# text_area.pack(pady=10)

# # Create the copy content button
# copy_content_button = tk.Button(root, text="Copy Content", command=copy_content)
# copy_content_button.pack(pady=10)

# root.mainloop()

import os
import tkinter as tk
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
from tkinter import Checkbutton, IntVar, Canvas, Frame, Scrollbar

def get_file_extensions(project_dir):
    """
    Scans the directory tree and returns a set of unique file extensions.
    """
    extensions = set()
    for root, dirs, files in os.walk(project_dir):
        for filename in files:
            _, ext = os.path.splitext(filename)
            if ext:
                extensions.add(ext)
    return sorted(extensions)

def extract_file_contents(project_dir, selected_extensions):
    """
    Extracts the contents of all files in the specified project directory
    and its subdirectories that match the selected extensions and returns them as a single string.
    """
    file_contents = ""
    for root, dirs, files in os.walk(project_dir):
        for filename in files:
            _, ext = os.path.splitext(filename)
            if selected_extensions and ext not in selected_extensions:
                continue  # Skip files that don't match the selected extensions
            
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
                except PermissionError:
                    content = "Error: Permission denied."
                except Exception as e:
                    content = f"Unexpected error: {str(e)}"
                file_contents += f"########################################{file_path}\n########################################\n{content}\n########################################\n"
    return file_contents

def select_folder():
    global selected_folder, check_vars, checkbuttons_frame
    selected_folder = filedialog.askdirectory()
    if selected_folder:
        # Discover file extensions in the selected directory
        extensions = get_file_extensions(selected_folder)
        
        # Clear previous checkboxes
        for widget in checkbuttons_frame.winfo_children():
            widget.destroy()

        # Create checkbuttons for each extension in two columns
        check_vars = {}
        col = 0
        row = 0
        for ext in extensions:
            var = IntVar()
            check_vars[ext] = var
            cb = Checkbutton(checkbuttons_frame, text=ext, variable=var)
            cb.grid(row=row, column=col, sticky='w')
            row += 1
            if row > len(extensions) // 2:
                row = 0
                col += 1

        # Update the canvas scroll region
        checkbuttons_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

def display_file_contents():
    global selected_folder, check_vars
    selected_extensions = [ext for ext, var in check_vars.items() if var.get() == 1]
    file_contents = extract_file_contents(selected_folder, selected_extensions)
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

# Create a canvas for the checklist with scrollbars
canvas = Canvas(root)
scrollbar_y = Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar_x = Scrollbar(root, orient="horizontal", command=canvas.xview)
canvas.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

scrollbar_y.pack(side="right", fill="y")
scrollbar_x.pack(side="bottom", fill="x")
canvas.pack(side="left", fill="both", expand=True)

# Create a frame inside the canvas to hold the checkbuttons
checkbuttons_frame = Frame(canvas)
canvas.create_window((0, 0), window=checkbuttons_frame, anchor="nw")

# Create the display contents button
display_button = tk.Button(root, text="Display File Contents", command=display_file_contents)
display_button.pack(pady=10)

# Create the text area to display file contents
text_area = ScrolledText(root, width=80, height=20, wrap=tk.WORD)
text_area.pack(pady=10)

# Create the copy content button
copy_content_button = tk.Button(root, text="Copy Content", command=copy_content)
copy_content_button.pack(pady=10)

root.mainloop()
