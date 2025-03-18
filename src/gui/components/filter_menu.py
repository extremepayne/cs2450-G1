import tkinter as tk
from tkinter import ttk
from .custom_button import CustomButton


class MenuWindow(tk.Frame):
    def __init__(self, parent, apply_callback):
        super().__init__(parent, bg="#52BEC4")
        self.config(bg="#52BEC4", padx=10, pady=10)

        # Filtering UI
        label = tk.Label(
            self, text="Filter by Course", bg="#52BEC4", font=("Arial", 12, "bold")
        )
        label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        # Course Dropdown
        self.course_var = tk.StringVar(value="All Courses")
        self.course_dropdown = ttk.Combobox(self, textvariable=self.course_var)
        self.course_dropdown["values"] = [
            "All Courses",
        ]
        self.course_dropdown.grid(row=0, column=1, padx=5)

        # Buttons
        button_frame = tk.Frame(self, bg="#52BEC4")
        button_frame.grid(row=1, column=0, columnspan=2, pady=10)

        CustomButton(button_frame, text="Apply", command=self.apply_filters).pack(
            side=tk.LEFT, padx=5
        )
        CustomButton(button_frame, text="Clear", command=self.clear_filter).pack(
            side=tk.LEFT, padx=5
        )

        self.apply_callback = apply_callback

    def apply_filters(self):
        course = self.course_var.get()
        self.apply_callback(course)

    def clear_filter(self):
        self.course_var.set("All Courses")
        self.apply_filters()

    def update_courses(self, course_list):
        """Update the course dropdown with new course list"""
        for course in course_list:
            self.course_dropdown["values"] += (course,)
        if "All Courses" not in self.course_var.get():
            self.course_var.set("All Courses")
