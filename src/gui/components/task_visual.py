import tkinter as tk
from tkinter import ttk
import os


class TaskItem(tk.Frame):
    def __init__(
        self,
        parent,
        task_name,
        description,
        course,
        due_date,
        delete_callback,
        edit_callback,
    ):
        super().__init__(parent, bd=0, relief="flat", bg="#FFFFFF", padx=10, pady=5)

        # Configure column weights to push items to the right
        self.grid_columnconfigure(0, weight=1)  # Task name/description column expands
        self.grid_columnconfigure(1, weight=0)  # Course code stays fixed
        self.grid_columnconfigure(2, weight=0)  # Due date stays fixed
        self.grid_columnconfigure(3, weight=0)  # Edit button stays fixed
        self.grid_columnconfigure(4, weight=0)  # Delete button stays fixed

        # Task Name & Description (left-aligned)
        task_label = tk.Label(
            self, text=task_name, font=("Arial", 12, "bold"), bg="#FFFFFF"
        )
        task_label.grid(row=0, column=0, sticky="w", padx=(5, 10))

        desc_label = tk.Label(self, text=description, font=("Arial", 10), bg="#FFFFFF")
        desc_label.grid(row=1, column=0, sticky="w", padx=(5, 10))

        # Course & Due Date (right-aligned)
        course_label = tk.Label(self, text=course, font=("Arial", 10), bg="#FFFFFF")
        course_label.grid(row=0, column=1, padx=10, sticky="e")

        due_label = tk.Label(
            self, text=f"Due: {due_date}", font=("Arial", 10), bg="#FFFFFF"
        )
        due_label.grid(row=0, column=2, padx=10, sticky="e")

        # Get the absolute path to the assets directory
        assets_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")

        # Edit Button (right-aligned)
        edit_icon = tk.PhotoImage(file=os.path.join(assets_dir, "edit.png"))
        edit_button = tk.Button(
            self, image=edit_icon, command=lambda: edit_callback(task_name)
        )
        edit_button.image = edit_icon  # Keep reference
        edit_button.grid(row=0, column=3, padx=5, sticky="e")

        # Store task name and callbacks
        self.task_name = task_name
        self.delete_callback = delete_callback

        # Delete Button (right-aligned)
        delete_icon = tk.PhotoImage(file=os.path.join(assets_dir, "trash.png"))
        delete_button = tk.Button(self, image=delete_icon, command=self.delete_self)
        delete_button.image = delete_icon
        delete_button.grid(row=0, column=4, padx=5, sticky="e")

    def delete_self(self):
        """Handle task deletion"""
        if self.delete_callback(self.task_name):
            self.destroy()  # Remove the widget from view if deletion was confirmed


class TaskManagerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Task Manager")
        self.geometry("500x300")

        # Create a canvas with scrollbar
        self.canvas = tk.Canvas(self, bg="#FFFFFF")
        self.scrollbar = tk.Scrollbar(
            self, orient="vertical", command=self.canvas.yview
        )
        self.scrollable_frame = tk.Frame(self.canvas, bg="#FFFFFF")

        # Configure the canvas
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")),
        )

        # Create a window inside the canvas for the frame
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Pack the scrollbar and canvas
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        # Sample Data
        tasks = [
            ("Task three", "Task three descript...", "CS 2450", "1/1/2025"),
            ("Task one", "Task one descript...", "CS 3060", "1/13/2025"),
            ("Task two", "Task two descript...", "CS 2420", "10/7/2025"),
        ]

        # Create task items in the scrollable frame
        for task in tasks:
            task_item = TaskItem(
                self.scrollable_frame, *task, self.delete_task, self.edit_task
            )
            task_item.pack(fill="x", padx=5, pady=5)

        # Bind mousewheel to scroll
        self.bind_all("<MouseWheel>", self._on_mousewheel)

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def delete_task(self, task_name):
        print(f"Deleting: {task_name}")

    def edit_task(self, task_name):
        print(f"Editing: {task_name}")


if __name__ == "__main__":
    app = TaskManagerApp()
    app.mainloop()
