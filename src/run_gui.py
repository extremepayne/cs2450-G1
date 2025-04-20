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

def save_task(self):
    """Collect updated task data and call the save callback."""
    if self.save_callback:
        task_data = {
            "name": self.name_entry.get(),
            "due_date": self.due_date_cal.get_date(),
            "description": self.description_text.get("1.0", "end-1c"),
            "status": self.status_var.get(),
            "course": self.course_var.get(),
        }
        self.save_callback(task_data, self.task_id)  # Pass updated data and task ID
    self.destroy()
