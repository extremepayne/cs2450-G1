import tkinter as tk


class CustomButton(tk.Button):
    def __init__(self, master, text="", command=None):
        super().__init__(
            master,
            text=text,
            bg="#E6E6E6",  # Default background color
            fg="#1A1A1A",  # Text color
            font=("Arial", 12),
            relief="flat",
            bd=0,  # No border
            highlightthickness=1,
            highlightbackground="#808080",
            padx=20,
            pady=10,
            command=command,
        )

        # Bind hover events
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self.configure(
            bg="#808080",  # Darker background on hover
            highlightbackground="#666666",  # Darker border on hover
        )

    def on_leave(self, e):
        self.configure(
            bg="#E6E6E6",  # Original background
            highlightbackground="#cccccc",  # Original border color
        )
