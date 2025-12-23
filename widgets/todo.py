import tkinter as tk
from tkinter import ttk
from core.widget_base import BaseWidget
from ui.theme import ThemeManager

class TodoWidget(BaseWidget):
    TYPE = "todo"

    def __init__(self, **kwargs):
        super().__init__(title="To-Do List", width=320, height=320, **kwargs)

        theme = ThemeManager.get()
        self.accent = theme["accent"]
        self.tasks = []

        # ---- Header ----
        self.header = tk.Label(
            self.container,
            text="Your Tasks",
            bg=self.bg_color,
            fg=self.fg_color,
            font=("Segoe UI", 13, "bold")
        )
        self.header.pack(pady=(8, 2))

        # ---- Progress text ----
        self.progress_text = tk.Label(
            self.container,
            text="0 / 0 completed",
            bg=self.bg_color,
            fg=self.fg_color,
            font=("Segoe UI", 10)
        )
        self.progress_text.pack()

        # ---- Progress bar ----
        self.progress = ttk.Progressbar(
            self.container,
            orient="horizontal",
            length=260,
            mode="determinate"
        )
        self.progress.pack(pady=(4, 10))

        # ---- Entry ----
        self.entry = tk.Entry(
            self.container,
            bg=self.bg_color,
            fg=self.fg_color,
            insertbackground=self.fg_color,
            font=("Segoe UI", 11),
            relief="flat"
        )
        self.entry.pack(fill="x", padx=10, pady=6)
        self.entry.bind("<Return>", self.add_task)

        # ---- Task list ----
        self.list_frame = tk.Frame(self.container, bg=self.bg_color)
        self.list_frame.pack(fill="both", expand=True, padx=10)

        # ---- Celebration ----
        self.celebration = tk.Label(
            self.container,
            text="🎉 All tasks completed!",
            bg=self.bg_color,
            fg=self.accent,
            font=("Segoe UI", 12, "bold")
        )

    # ---------------- TASK LOGIC ----------------
    def add_task(self, event=None, text=None, checked=False):
        if text is None:
            text = self.entry.get().strip()
            if not text:
                return
            self.entry.delete(0, "end")

        var = tk.BooleanVar(value=checked)

        row = tk.Frame(self.list_frame, bg=self.bg_color)
        row.pack(fill="x", pady=3)

        cb = tk.Checkbutton(
            row,
            variable=var,
            bg=self.bg_color,
            activebackground=self.bg_color,
            selectcolor=self.accent,
            highlightthickness=0
        )
        cb.pack(side="left")

        label = tk.Label(
            row,
            text=text,
            bg=self.bg_color,
            fg=self.fg_color,
            font=("Segoe UI", 11),
            anchor="w"
        )
        label.pack(side="left", fill="x", expand=True, padx=6)

        def update_style(*_):
            if var.get():
                label.config(
                    fg="#888888",
                    font=("Segoe UI", 11, "overstrike")
                )
            else:
                label.config(
                    fg=self.fg_color,
                    font=("Segoe UI", 11)
                )
            self.update_progress()

        var.trace_add("write", update_style)
        update_style()

        self.tasks.append((text, var, label))
        self.update_progress()

    # ---------------- PROGRESS ----------------
    def update_progress(self):
        total = len(self.tasks)
        done = sum(var.get() for _, var, _ in self.tasks)

        self.progress["maximum"] = max(total, 1)
        self.progress["value"] = done

        self.progress_text.config(text=f"{done} / {total} completed")

        # Celebration logic
        if total > 0 and done == total:
            if not self.celebration.winfo_ismapped():
                self.celebration.pack(pady=6)
        else:
            self.celebration.pack_forget()

    # ---------------- SAVE / RESTORE ----------------
    def get_data(self):
        return {
            "tasks": [
                {"text": text, "checked": var.get()}
                for text, var, _ in self.tasks
            ]
        }

    def load_data(self, data):
        for task in data.get("tasks", []):
            self.add_task(text=task["text"], checked=task["checked"])

    # ---------------- THEME ----------------
    def apply_colors(self):
        theme = ThemeManager.get()
        self.accent = theme["accent"]

        self.container.config(bg=self.bg_color)
        self.header.config(bg=self.bg_color, fg=self.fg_color)
        self.progress_text.config(bg=self.bg_color, fg=self.fg_color)
        self.celebration.config(bg=self.bg_color, fg=self.accent)

        self.entry.config(
            bg=self.bg_color,
            fg=self.fg_color,
            insertbackground=self.fg_color
        )

        self.list_frame.config(bg=self.bg_color)

        for _, _, label in self.tasks:
            label.config(bg=self.bg_color)
