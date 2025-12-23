import time
import tkinter as tk
from core.widget_base import BaseWidget
from ui.theme import ThemeManager

class ClockWidget(BaseWidget):
    TYPE = "clock"

    def __init__(self, **kwargs):
        super().__init__(title="Clock", width=260, height=130, **kwargs)

        theme = ThemeManager.get()
        self.accent = theme["accent"]
        self.show_colon = True

        # Time
        self.time_label = tk.Label(
            self.container,
            bg=self.bg_color,
            fg=self.accent,
            font=("Segoe UI", 28, "bold")
        )
        self.time_label.pack(pady=(10, 0))

        # Greeting
        self.greeting_label = tk.Label(
            self.container,
            bg=self.bg_color,
            fg=self.fg_color,
            font=("Segoe UI", 12)
        )
        self.greeting_label.pack()

        # Date
        self.date_label = tk.Label(
            self.container,
            bg=self.bg_color,
            fg=self.fg_color,
            font=("Segoe UI", 10)
        )
        self.date_label.pack(pady=(0, 8))

        self.update_time()

    def get_greeting(self, hour):
        if hour < 12:
            return "Good Morning ☀"
        elif hour < 18:
            return "Good Afternoon 🌤"
        else:
            return "Good Evening 🌙"

    def update_time(self):
        now = time.localtime()
        hour = now.tm_hour
        minute = now.tm_min

        colon = ":" if self.show_colon else " "
        self.show_colon = not self.show_colon

        self.time_label.config(
            text=f"{hour:02d}{colon}{minute:02d}"
        )

        self.greeting_label.config(
            text=self.get_greeting(hour)
        )

        self.date_label.config(
            text=time.strftime("%A, %d %B")
        )

        self.root.after(500, self.update_time)

    def apply_colors(self):
        theme = ThemeManager.get()
        self.accent = theme["accent"]

        self.container.config(bg=self.bg_color)
        self.time_label.config(bg=self.bg_color, fg=self.accent)
        self.greeting_label.config(bg=self.bg_color, fg=self.fg_color)
        self.date_label.config(bg=self.bg_color, fg=self.fg_color)
