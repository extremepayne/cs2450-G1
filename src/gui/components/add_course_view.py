import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox
from .custom_button import CustomButton


class AddCourseView(tk.Toplevel):
    def __init__(self, parent, save_callback=None):
        super().__init__(parent)
        self.title("Add Course")
        self.geometry("600x450")
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
            header_bar, text="Add New Course", bg="#B6EEFB", font=("Arial", 14, "bold")
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

        # Course name
        tk.Label(main_container, text="Course Name:").grid(
            row=1, column=0, padx=5, pady=5, sticky="e"
        )
        self.name_entry = tk.Entry(main_container, width=40)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        # Course code
        tk.Label(main_container, text="Course Code:").grid(
            row=2, column=0, padx=5, pady=5, sticky="e"
        )
        self.code_entry = tk.Entry(main_container, width=40)
        self.code_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        # Description
        tk.Label(main_container, text="Description:").grid(
            row=3, column=0, padx=5, pady=5, sticky="e"
        )
        self.description_text = tk.Text(main_container, width=30, height=5)
        self.description_text.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        # Start date
        tk.Label(main_container, text="Start Date (YYYY-MM-DD):").grid(
            row=4, column=0, padx=5, pady=5, sticky="e"
        )
        self.start_date_entry = tk.Entry(main_container, width=40)
        self.start_date_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        # End date
        tk.Label(main_container, text="End Date (YYYY-MM-DD):").grid(
            row=5, column=0, padx=5, pady=5, sticky="e"
        )
        self.end_date_entry = tk.Entry(main_container, width=40)
        self.end_date_entry.grid(row=5, column=1, padx=5, pady=5, sticky="w")

        # Buttons
        button_frame = tk.Frame(main_container)
        button_frame.grid(row=6, column=0, columnspan=2, pady=20)

        CustomButton(button_frame, text="Add", command=self.save_course).grid(
            row=0, column=0, padx=5
        )
        CustomButton(button_frame, text="Cancel", command=self.destroy).grid(
            row=0, column=1, padx=5
        )

    def save_course(self):
        if self.save_callback:

            # Check if required data is filled
            if not self.name_entry.get():
                messagebox.showinfo("Error", "Course name cannot be empty")
                raise ValueError("Course name cannot be empty")
            elif not self.code_entry.get():
                messagebox.showinfo("Error", "Course code cannot be empty")
                raise ValueError("Course code cannot be empty")

            course_data = {
                "name": self.name_entry.get(),
                "code": self.code_entry.get(),
                "description": self.description_text.get("1.0", "end-1c"),
                "start_date": self.start_date_entry.get(),
                "end_date": self.end_date_entry.get(),
            }
            self.save_callback(course_data)
        self.destroy()
