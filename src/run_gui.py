import os
import sys
import tkinter as tk

# Add project root and src to Python path
project_root = os.path.dirname(os.path.dirname(__file__))
src_path = os.path.join(project_root, "src")
sys.path.append(project_root)
sys.path.append(src_path)

from gui.gui import TaskManagerGUI


def main():
    root = tk.Tk()
    root.title("Course Task Manager")
    root.geometry("1500x900")
    root.configure(background="#E6E6E6")

    app = TaskManagerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
