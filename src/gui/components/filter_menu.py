import tkinter as tk
from tkinter import ttk
from .custom_button import CustomButton


class MenuWindow(tk.Frame):
    """A separate menu window for filtering options."""

    def __init__(self, parent, apply_callback):
        super().__init__(parent, bg="#52BEC4")
        self.config(bg="#52BEC4", padx=10, pady=10)

        # Filtering UI
        label = tk.Label(
            self, text="Filtering options", bg="#52BEC4", font=("Arial", 12, "bold")
        )
        label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        # Course Dropdown
        self.course_var = tk.StringVar()
        self.course_dropdown = ttk.Combobox(
            self, textvariable=self.course_var, values=["CS 2450", "CS 3060"]
        )
        self.course_dropdown.set("[select course]")
        self.course_dropdown.grid(row=0, column=1, padx=5)

        # Due Date Entry
        self.due_date_entry = tk.Entry(self)
        self.due_date_entry.insert(0, "Enter Date...")
        self.due_date_entry.grid(row=0, column=2, padx=5)

        # Apply Button
        apply_button = CustomButton(self, text="Apply", command=self.apply_filters)
        apply_button.grid(row=1, column=1, columnspan=2, pady=10)

        # Store callback function
        self.apply_callback = apply_callback

    def apply_filters(self):
        """Send filter data back to the main app."""
        course = self.course_var.get()
        due_date = self.due_date_entry.get()
        self.apply_callback(course, due_date)
        self.pack_forget()  # Close menu after applying
