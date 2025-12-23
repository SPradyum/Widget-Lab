import tkinter as tk
from tkinter import colorchooser

class WidgetEditor:
    def __init__(self, widget):
        self.widget = widget

        self.window = tk.Toplevel()
        self.window.title("Widget Editor")
        self.window.geometry("300x300")
        self.window.configure(bg="#1e1e1e")

        self._build_ui()

    def _build_ui(self):
        tk.Label(
            self.window,
            text="Customize Widget",
            fg="white",
            bg="#1e1e1e",
            font=("Segoe UI", 14, "bold")
        ).pack(pady=10)

        tk.Button(
            self.window,
            text="Change Background Color",
            command=self.change_bg
        ).pack(pady=5)

        tk.Button(
            self.window,
            text="Change Text Color",
            command=self.change_fg
        ).pack(pady=5)

        tk.Label(
            self.window,
            text="Opacity",
            fg="white",
            bg="#1e1e1e"
        ).pack(pady=10)

        self.opacity = tk.Scale(
            self.window,
            from_=30,
            to=100,
            orient="horizontal",
            command=self.set_opacity
        )
        self.opacity.set(100)
        self.opacity.pack(pady=5)

        tk.Button(
            self.window,
            text="Close",
            command=self.window.destroy
        ).pack(pady=15)

    def change_bg(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.widget.bg_color = color
            self.widget.container.config(bg=color)
            self.widget.apply_colors()

    def change_fg(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.widget.fg_color = color
            self.widget.apply_colors()

    def set_opacity(self, value):
        self.widget.root.attributes("-alpha", int(value) / 100)
