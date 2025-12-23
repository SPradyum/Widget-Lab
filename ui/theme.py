THEMES = {
    "Cyberpunk": {
        "bg": "#0f1021",
        "panel": "#1b1d3a",
        "fg": "#00e5ff",
        "accent": "#ff2a6d",
        "font": ("Segoe UI", 11)
    },
    "Glass": {
        "bg": "#121212",
        "panel": "#1e1e1e",
        "fg": "#ffffff",
        "accent": "#00ffcc",
        "font": ("Segoe UI", 11)
    },
    "Midnight": {
        "bg": "#0b132b",
        "panel": "#1c2541",
        "fg": "#eaeaea",
        "accent": "#5bc0be",
        "font": ("Segoe UI", 11)
    },
    "NightLife": {
        "bg": "#2b1055",
        "panel": "#3c1a5b",
        "fg": "#f7b267",
        "accent": "#f25c54",
        "font": ("Segoe UI", 11)
    }
}

class ThemeManager:
    current = "Cyberpunk"

    @classmethod
    def get(cls):
        return THEMES[cls.current]

    @classmethod
    def set(cls, name):
        if name in THEMES:
            cls.current = name
