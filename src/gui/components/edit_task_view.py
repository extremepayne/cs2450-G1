import tkinter as tk
from tkinter import ttk
from datetime import date
from .custom_button import CustomButton


class EditTaskView(tk.Toplevel):
    def __init__(self, parent, task_id, task_data=None, save_callback=None):
        super().__init__(parent)
        self.title("Edit Task")
        self.geometry("600x450")
        self.task_id = task_id
        self.task_data = task_data
        self.save_callback = save_callback

        # Create entry fields
        self.create_widgets()

    def create_widgets(self):
        # Main container using grid
        main_container = tk.Frame(self)
        main_container.grid(row=0, column=0, sticky="nsew")

        # Configure grid weights
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        main_container.grid_columnconfigure(1, weight=1)

        # Header bar
        header_bar = tk.Frame(main_container, bg="#B6EEFB", height=70)
        header_bar.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 10))

        # Add header label
        header_label = tk.Label(
            header_bar, text="Editing Task", bg="#B6EEFB", font=("Arial", 14, "bold")
        )
        header_label.pack(side=tk.LEFT, expand=True, pady=10)

        # Add close button
        close_button = tk.Button(
            header_bar,
            text="✕",
            bg="#B6EEFB",
            font=("Arial", 12),
            relief="flat",
            command=self.destroy,
        )
        close_button.pack(side=tk.RIGHT, padx=10, pady=10)

        # Task name
        tk.Label(main_container, text="Task Name:").grid(
            row=1, column=0, padx=5, pady=5, sticky="e"
        )
        self.name_entry = tk.Entry(main_container, width=40)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        # Due date
        tk.Label(main_container, text="Due Date (YYYY-MM-DD):").grid(
            row=2, column=0, padx=5, pady=5, sticky="e"
        )
        self.due_date_entry = tk.Entry(main_container, width=40)
        self.due_date_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        # Description
        tk.Label(main_container, text="Description:").grid(
            row=3, column=0, padx=5, pady=5, sticky="e"
        )
        self.description_text = tk.Text(main_container, width=30, height=5)
        self.description_text.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        # Course selection
        tk.Label(main_container, text="Course:").grid(
            row=4, column=0, padx=5, pady=5, sticky="e"
        )
        self.course_var = tk.StringVar(value=self.task_data.get("course", "CS 2450"))
        self.course_combo = ttk.Combobox(main_container, textvariable=self.course_var)
        self.course_combo["values"] = (
            "CS 2450",
            "CS 3060",
            "CS 2420",
        )  # TODO: Get from CourseList
        self.course_combo.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        # Status (move to row 5)
        tk.Label(main_container, text="Status:").grid(
            row=5, column=0, padx=5, pady=5, sticky="e"
        )
        self.status_var = tk.StringVar()
        self.status_combo = ttk.Combobox(main_container, textvariable=self.status_var)
        self.status_combo["values"] = ("Not Started", "In Progress", "Completed")
        self.status_combo.grid(row=5, column=1, padx=5, pady=5, sticky="w")

        # Populate fields if task_data exists
        if self.task_data:
            self.name_entry.insert(0, self.task_data["name"])
            self.due_date_entry.insert(0, self.task_data["due_date"])
            self.description_text.insert("1.0", self.task_data["description"])
            self.status_var.set(self.task_data["status"])
            if "course" in self.task_data:
                self.course_var.set(self.task_data["course"])

        # Buttons
        button_frame = tk.Frame(main_container)
        button_frame.grid(row=6, column=0, columnspan=2, pady=20)

        # Use grid for buttons too
        CustomButton(button_frame, text="Save", command=self.save_task).grid(
            row=0, column=0, padx=5
        )
        CustomButton(button_frame, text="Cancel", command=self.destroy).grid(
            row=0, column=1, padx=5
        )

    def save_task(self):
        if self.save_callback:
            task_data = {
                "name": self.name_entry.get(),
                "due_date": date.fromisoformat(self.due_date_entry.get()),
                "description": self.description_text.get("1.0", "end-1c"),
                "status": self.status_var.get(),
                "course": self.course_var.get(),  # Add course to task data
            }
            self.save_callback(task_data)
        self.destroy()
