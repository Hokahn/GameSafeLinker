import os
import sys
import ctypes
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def run_as_admin():
    if ctypes.windll.shell32.IsUserAnAdmin():
        return True
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        return False

def create_hidden_junction():
    source = filedialog.askdirectory(title="chose the folder to move")
    if not source:
        return

    target_parent = filedialog.askdirectory(title="chose the target folder")
    if not target_parent:
        return

    folder_name = os.path.basename(source)
    destination = os.path.join(target_parent, folder_name)

    try:
        if not os.path.exists(destination):
            shutil.move(source, destination)
        
        cmd_link = f'mklink /J "{source}" "{destination}"'
        result = os.system(cmd_link)
        
        if result == 0:
            os.system(f'attrib +h +s /L "{source}"')
            messagebox.showinfo("Success", " ")
        else:
            messagebox.showerror("Error", " ")
            
    except Exception as e:
        messagebox.showerror("Error", f"{e}")

if __name__ == "__main__":
    if run_as_admin():
        root = tk.Tk()
        root.title("move folder")
        root.geometry("400x150")

        tk.Label(root, text="move folder and hide link", pady=10).pack()
        tk.Button(root, text="Start", command=create_hidden_junction, height=2, width=30).pack(pady=20)

        root.mainloop()