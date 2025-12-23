import tkinter as tk
from tkinter import ttk
import psutil
from core.widget_base import BaseWidget
from ui.theme import ThemeManager

class SystemWidget(BaseWidget):
    TYPE = "system"

    def __init__(self, **kwargs):
        super().__init__(title="System Monitor", width=300, height=180, **kwargs)

        theme = ThemeManager.get()
        self.accent = theme["accent"]

        self._style_progress()

        self._build_ui()
        self.update_stats()

    def _style_progress(self):
        style = ttk.Style()
        style.theme_use("default")
        style.configure(
            "Accent.Horizontal.TProgressbar",
            troughcolor=self.bg_color,
            background=self.accent,
            thickness=10
        )

    def _build_ui(self):
        self.title = tk.Label(
            self.container,
            text="SYSTEM STATUS",
            bg=self.bg_color,
            fg=self.fg_color,
            font=("Segoe UI", 12, "bold")
        )
        self.title.pack(pady=(8, 4))

        self.cpu_label = tk.Label(self.container, bg=self.bg_color, fg=self.fg_color)
        self.cpu_label.pack(anchor="w", padx=10)
        self.cpu_bar = ttk.Progressbar(
            self.container, style="Accent.Horizontal.TProgressbar", length=260
        )
        self.cpu_bar.pack(pady=(0, 8))

        self.ram_label = tk.Label(self.container, bg=self.bg_color, fg=self.fg_color)
        self.ram_label.pack(anchor="w", padx=10)
        self.ram_bar = ttk.Progressbar(
            self.container, style="Accent.Horizontal.TProgressbar", length=260
        )
        self.ram_bar.pack(pady=(0, 8))

        self.battery_label = tk.Label(self.container, bg=self.bg_color, fg=self.fg_color)
        self.battery_label.pack(anchor="w", padx=10)
        self.battery_bar = ttk.Progressbar(
            self.container, style="Accent.Horizontal.TProgressbar", length=260
        )
        self.battery_bar.pack(pady=(0, 8))

    def update_stats(self):
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent
        battery = psutil.sensors_battery()
        batt = battery.percent if battery else 0

        self.cpu_label.config(text=f"CPU Usage: {cpu}%")
        self.cpu_bar["value"] = cpu

        self.ram_label.config(text=f"RAM Usage: {ram}%")
        self.ram_bar["value"] = ram

        self.battery_label.config(
            text=f"Battery: {batt}%" if battery else "Battery: N/A"
        )
        self.battery_bar["value"] = batt

        self.root.after(1000, self.update_stats)

    def apply_colors(self):
        theme = ThemeManager.get()
        self.accent = theme["accent"]
        self._style_progress()

        self.container.config(bg=self.bg_color)
        self.title.config(bg=self.bg_color, fg=self.fg_color)
        self.cpu_label.config(bg=self.bg_color, fg=self.fg_color)
        self.ram_label.config(bg=self.bg_color, fg=self.fg_color)
        self.battery_label.config(bg=self.bg_color, fg=self.fg_color)
