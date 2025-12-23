import tkinter as tk
from ui.theme import ThemeManager

class BaseWidget:
    TYPE = "base"

    def __init__(self, title="Widget", width=200, height=100, x=300, y=300):
        theme = ThemeManager.get()

        self.root = tk.Toplevel()
        self.root.title(title)
        self.root.overrideredirect(True)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        self.root.attributes("-topmost", True)
        self.root.attributes("-alpha", 0.97)

        self.bg_color = theme["panel"]
        self.fg_color = theme["fg"]
        self.accent = theme["accent"]
    
        # ---------- SHADOW LAYER ----------
        self.shadow = tk.Frame(
            self.root,
            bg="#000000"
        )
        self.shadow.pack(fill="both", expand=True, padx=4, pady=4)

        # ---------- CARD LAYER ----------
        self.container = tk.Frame(
            self.shadow,
            bg=self.bg_color
        )
        self.container.pack(fill="both", expand=True)

        self._make_draggable()
        self._add_context_menu()
        self._add_hover_effect()

    # ---------------- DRAG ----------------
    def _make_draggable(self):
        self.container.bind("<Button-1>", self._start_move)
        self.container.bind("<B1-Motion>", self._on_move)

    def _start_move(self, event):
        self._x = event.x
        self._y = event.y

    def _on_move(self, event):
        x = self.root.winfo_x() + event.x - self._x
        y = self.root.winfo_y() + event.y - self._y
        self.root.geometry(f"+{x}+{y}")

    def _fade_in(self):
        self._alpha = 0.0
        self.root.attributes("-alpha", self._alpha)

        def step():
            self._alpha += 0.08
            if self._alpha <= 1.0:
                self.root.attributes("-alpha", self._alpha)
                self.root.after(15, step)
        step()


    # ---------------- CONTEXT MENU ----------------
    def _add_context_menu(self):
        self.menu = tk.Menu(self.root, tearoff=0)
        self.menu.add_command(label="Edit Widget", command=self.open_editor)
        self.menu.add_command(label="Close Widget", command=self.close)

        self.container.bind(
            "<Button-3>",
            lambda e: self.menu.tk_popup(e.x_root, e.y_root)
        )

    def open_editor(self):
        from ui.editor import WidgetEditor
        WidgetEditor(self)

    # ---------------- HOVER EFFECT ----------------
    def _add_hover_effect(self):
        self.container.bind("<Enter>", self._hover_on)
        self.container.bind("<Leave>", self._hover_off)

    def _hover_on(self, event=None):
        # Slight glow + depth
        self.shadow.config(bg=self.accent)
        self.root.attributes("-alpha", 1.0)

    def _hover_off(self, event=None):
        self.shadow.config(bg="#000000")
        self.root.attributes("-alpha", 0.97)

    # ---------------- THEME ----------------
    def apply_colors(self):
        self.container.config(bg=self.bg_color)
        for child in self.container.winfo_children():
            try:
                child.config(bg=self.bg_color, fg=self.fg_color)
            except:
                pass

    # ---------------- SAVE / RESTORE ----------------
    def serialize(self):
        return {
            "type": self.TYPE,
            "x": self.root.winfo_x(),
            "y": self.root.winfo_y(),
            "width": self.root.winfo_width(),
            "height": self.root.winfo_height(),
            "bg_color": self.bg_color,
            "fg_color": self.fg_color,
            "opacity": self.root.attributes("-alpha"),
            "data": self.get_data()
        }

    def get_data(self):
        self._fade_in()
        return {}

    def load_data(self, data):
        pass

    def close(self):
        self.root.destroy()
        
