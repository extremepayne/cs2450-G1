import os
import sys

# Add the src directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(current_dir))

from src.gui.gui import TaskManagerGUI
import tkinter as tk


def main():
    root = tk.Tk()
    root.title("Course Task Manager")
    root.geometry("1500x900")
    root.configure(background="#E6E6E6")

    app = TaskManagerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()