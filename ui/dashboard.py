import tkinter as tk
from ui.theme import ThemeManager

class Dashboard(tk.Frame):
    def __init__(self, master, manager):
        super().__init__(master)
        self.manager = manager
        self.pack(fill="both", expand=True)
        self.build()

    def build(self):
        theme = ThemeManager.get()
        self.configure(bg=theme["bg"])

        # Title
        tk.Label(
            self,
            text="WIDGETLAB",
            bg=theme["bg"],
            fg=theme["accent"],
            font=("Segoe UI", 28, "bold")
        ).pack(pady=(25, 10))

        tk.Label(
            self,
            text="Build your desktop. Your way.",
            bg=theme["bg"],
            fg=theme["fg"],
            font=("Segoe UI", 13)
        ).pack(pady=(0, 25))

        # Cards container
        card_area = tk.Frame(self, bg=theme["bg"])
        card_area.pack()

        self.card(card_area, "🕒 Clock", self.manager.add_clock)
        self.card(card_area, "📝 Notes", self.manager.add_notes)
        self.card(card_area, "☑ To-Do", self.manager.add_todo)
        self.card(card_area, "📊 System", self.manager.add_system)

        # Theme switcher
        tk.Label(
            self,
            text="Theme",
            bg=theme["bg"],
            fg=theme["fg"],
            font=("Segoe UI", 12)
        ).pack(pady=(25, 5))

        theme_frame = tk.Frame(self, bg=theme["bg"])
        theme_frame.pack()

        for name in ["Cyberpunk", "Glass", "Midnight", "NightLife"]:
            tk.Button(
                theme_frame,
                text=name,
                bg=theme["panel"],
                fg=theme["fg"],
                activebackground=theme["accent"],
                width=12,
                command=lambda n=name: self.change_theme(n)
            ).pack(side="left", padx=5)

    def card(self, parent, text, command):
        theme = ThemeManager.get()

        btn = tk.Button(
            parent,
            text=text,
            bg=theme["panel"],
            fg=theme["fg"],
            font=("Segoe UI", 13),
            width=20,
            height=2,
            relief="flat",
            activebackground=theme["accent"],
            command=command
        )
        btn.pack(pady=6)

    def change_theme(self, name):
        ThemeManager.set(name)
        self.destroy()
        self.manager.refresh_dashboard()
