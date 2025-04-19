import tkinter as tk
from tkinter import ttk
from datetime import date
from tkinter import messagebox
from .custom_button import CustomButton
from tkcalendar import Calendar


class AddTaskView(tk.Toplevel):
    def __init__(self, parent, save_callback=None):
        super().__init__(parent)
        self.title("Add Task")
        self.geometry("600x500")
        self.save_callback = save_callback

        # Course Dropdown
        self.course_var = tk.StringVar(value="Choose a Course")
        self.course_dropdown = ttk.Combobox(self, textvariable=self.course_var)
        self.course_dropdown["values"] = [
            "Choose a Course",
        ]

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
            header_bar, text="Add New Task", bg="#B6EEFB", font=("Arial", 14, "bold")
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

        # Course selection (moved up after task name)
        tk.Label(main_container, text="Course:").grid(
            row=2, column=0, padx=5, pady=5, sticky="e"
        )
        self.course_dropdown = ttk.Combobox(
            main_container, textvariable=self.course_var
        )
        self.course_dropdown["values"] = ["Choose a Course"]
        self.course_dropdown.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        # Due date
        tk.Label(main_container, text="Due Date:").grid(
            row=3, column=0, padx=5, pady=5, sticky="e"
        )
        self.due_date_cal = Calendar(
            main_container,
            selectmode="day",
            date_pattern="yyyy-mm-dd",
            foreground="black",
            background="white",
            headersbackground="white",
            normalbackground="white",
        )
        self.due_date_cal.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        # Description
        tk.Label(main_container, text="Description:").grid(
            row=4, column=0, padx=5, pady=5, sticky="e"
        )
        self.description_text = tk.Text(main_container, width=30, height=5)
        self.description_text.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        # Status (move to row 5)
        tk.Label(main_container, text="Status:").grid(
            row=5, column=0, padx=5, pady=5, sticky="e"
        )
        self.status_var = tk.StringVar(value="Not Started")
        self.status_combo = ttk.Combobox(main_container, textvariable=self.status_var)
        self.status_combo["values"] = ("Not Started", "In Progress", "Completed")
        self.status_combo.grid(row=5, column=1, padx=5, pady=5, sticky="w")

        # Buttons
        button_frame = tk.Frame(main_container)
        button_frame.grid(row=6, column=0, columnspan=2, pady=20)

        CustomButton(button_frame, text="Add", command=self.save_task).grid(
            row=0, column=0, padx=5
        )
        CustomButton(button_frame, text="Cancel", command=self.destroy).grid(
            row=0, column=1, padx=5
        )

    def update_courses(self, course_list):
        """Update the course dropdown with new course list"""
        for course in course_list:
            self.course_dropdown["values"] += (course,)
        if "Choose a Course" not in self.course_var.get():
            self.course_var.set("Choose a Course")

    def save_task(self):
        if self.save_callback:

            # Check if required data is filled
            if not self.name_entry.get():
                messagebox.showinfo("Error", "Task name cannot be empty")
                raise ValueError("Task name cannot be empty")
            elif self.course_var.get() == "Choose a Course":
                messagebox.showinfo("Error", "Task must have a course")
                raise ValueError("Task must have a course")

            task_data = {
                "name": self.name_entry.get(),
                "due_date": date.fromisoformat(self.due_date_cal.get_date()),
                "description": self.description_text.get("1.0", "end-1c"),
                "status": self.status_var.get(),
                "course": self.course_var.get(),
            }
            self.save_callback(task_data)
        self.destroy()
