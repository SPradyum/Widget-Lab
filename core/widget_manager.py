import tkinter as tk
from ui.dashboard import Dashboard
from core.layout_engine import LayoutManager
from widgets.clock import ClockWidget
from widgets.notes import NotesWidget
from widgets.todo import TodoWidget
from widgets.system import SystemWidget

class WidgetManager:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("WidgetLab")
        self.root.geometry("520x640")
        self.root.resizable(False, False)

        self.widgets = []
        self.dashboard = None

        self.refresh_dashboard()
        self.load_widgets()

    def refresh_dashboard(self):
        if self.dashboard:
            self.dashboard.destroy()
        self.dashboard = Dashboard(self.root, self)

    def add_clock(self): self.widgets.append(ClockWidget())
    def add_notes(self): self.widgets.append(NotesWidget())
    def add_todo(self): self.widgets.append(TodoWidget())
    def add_system(self): self.widgets.append(SystemWidget())

    def load_widgets(self):
        data = LayoutManager.load()
        if not isinstance(data, list):
            return
        for w in data:
            cls = {
                "clock": ClockWidget,
                "notes": NotesWidget,
                "todo": TodoWidget,
                "system": SystemWidget
            }.get(w["type"])
            if not cls: continue

            widget = cls(
                width=w["width"], height=w["height"],
                x=w["x"], y=w["y"]
            )
            widget.bg_color = w["bg_color"]
            widget.fg_color = w["fg_color"]
            widget.opacity = w["opacity"]
            widget.root.attributes("-alpha", widget.opacity)
            widget.apply_colors()
            widget.load_data(w.get("data", {}))
            self.widgets.append(widget)

    def run(self):
        self.root.mainloop()
