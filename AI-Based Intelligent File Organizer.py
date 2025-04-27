import os
import shutil
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox

# Define categories and their respective folders
FILE_CATEGORIES = {
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Code": [".py", ".java", ".cpp", ".html", ".css", ".js"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Executables": [".exe", ".bat", ".sh", ".app"]
}

# Function to classify and move files
def organize_files(directory):
    directory = Path(directory)
    if not directory.exists():
        messagebox.showerror("Error", f"The directory {directory} does not exist.")
        return
    
    for file in directory.iterdir():
        if file.is_file():
            file_extension = file.suffix.lower()
            for category, extensions in FILE_CATEGORIES.items():
                if file_extension in extensions:
                    category_path = directory / category
                    category_path.mkdir(exist_ok=True)
                    shutil.move(str(file), str(category_path / file.name))
    
    messagebox.showinfo("Success", "✅ File organization completed!")

# GUI Application
def select_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        organize_files(folder_selected)

# Create GUI window
root = tk.Tk()
root.title("Intelligent File Organizer")
root.geometry("400x200")

label = tk.Label(root, text="Select a folder to organize:", font=("Arial", 12))
label.pack(pady=10)

select_button = tk.Button(root, text="Browse Folder", command=select_folder, font=("Arial", 12))
select_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=root.quit, font=("Arial", 12))
exit_button.pack(pady=10)

root.mainloop()