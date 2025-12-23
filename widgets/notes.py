import tkinter as tk
from core.widget_base import BaseWidget
from ui.theme import ThemeManager

PAPER_STYLES = {
    "Theme": None,
    "Yellow": "#fff4b8",
    "Blue": "#e8f1ff",
    "White": "#ffffff"
}

class NotesWidget(BaseWidget):
    TYPE = "notes"

    def __init__(self, **kwargs):
        super().__init__(title="Note", width=300, height=260, **kwargs)

        theme = ThemeManager.get()
        self.accent = theme["accent"]
        self.pinned = False
        self.paper_style = "Theme"

        # ---------- Header ----------
        header = tk.Frame(self.container, bg=self.bg_color)
        header.pack(fill="x", pady=(6, 2))

        self.pin_btn = tk.Button(
            header,
            text="📌",
            bg=self.bg_color,
            fg=self.fg_color,
            relief="flat",
            font=("Segoe UI", 12),
            command=self.toggle_pin
        )
        self.pin_btn.pack(side="right", padx=6)

        self.title_label = tk.Label(
            header,
            text="New Note",
            bg=self.bg_color,
            fg=self.fg_color,
            font=("Segoe UI", 12, "bold"),
            anchor="w"
        )
        self.title_label.pack(side="left", padx=8)

        # ---------- Paper Style Selector ----------
        style_frame = tk.Frame(self.container, bg=self.bg_color)
        style_frame.pack(fill="x", pady=2)

        for style in PAPER_STYLES:
            tk.Button(
                style_frame,
                text=style,
                bg=self.bg_color,
                fg=self.fg_color,
                relief="flat",
                font=("Segoe UI", 9),
                command=lambda s=style: self.set_paper_style(s)
            ).pack(side="left", padx=4)

        # ---------- Text Area ----------
        self.text = tk.Text(
            self.container,
            wrap="word",
            bg=self.bg_color,
            fg=self.fg_color,
            font=("Segoe UI", 11),
            relief="flat"
        )
        self.text.pack(fill="both", expand=True, padx=8, pady=6)

        self.text.bind("<KeyRelease>", self.update_title)

    # ---------------- BEHAVIOR ----------------
    def update_title(self, event=None):
        content = self.text.get("1.0", "end").strip()
        title = content.split("\n")[0][:25] if content else "New Note"
        self.title_label.config(text=title)

    def toggle_pin(self):
        self.pinned = not self.pinned
        self.root.attributes("-topmost", self.pinned)
        self.pin_btn.config(fg=self.accent if self.pinned else self.fg_color)

    def set_paper_style(self, style):
        self.paper_style = style
        color = PAPER_STYLES[style]

        if color:
            self.bg_color = color
            self.fg_color = "#000000"
        else:
            theme = ThemeManager.get()
            self.bg_color = theme["panel"]
            self.fg_color = theme["fg"]

        self.apply_colors()

    # ---------------- SAVE / RESTORE ----------------
    def get_data(self):
        return {
            "text": self.text.get("1.0", "end"),
            "pinned": self.pinned,
            "paper_style": self.paper_style
        }

    def load_data(self, data):
        self.text.insert("1.0", data.get("text", ""))
        self.pinned = data.get("pinned", False)
        self.paper_style = data.get("paper_style", "Theme")

        if self.pinned:
            self.root.attributes("-topmost", True)

        self.set_paper_style(self.paper_style)
        self.update_title()

    # ---------------- THEME ----------------
    def apply_colors(self):
        self.container.config(bg=self.bg_color)
        self.text.config(bg=self.bg_color, fg=self.fg_color)
        self.title_label.config(bg=self.bg_color, fg=self.fg_color)
        self.pin_btn.config(bg=self.bg_color)
