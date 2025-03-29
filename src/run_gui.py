import os
import sys
import tkinter as tk

# Add parent directory to path
sys.path.append(os.path.dirname(__file__))

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
