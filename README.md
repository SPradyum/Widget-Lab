# WidgetLab ✨  
A Creative, Customizable Desktop Widget Maker in Python

WidgetLab is a **modern, highly customizable desktop widget system** built using Python.  
It allows users to create, style, and manage **floating desktop widgets** for daily productivity — all from a visually rich dashboard.

Unlike basic widget tools, WidgetLab focuses on **personality, micro-interactions, and UX polish**, making widgets feel alive rather than static.

---

## 🚀 Key Highlights

- 🎨 Premium dashboard with multiple themes (Cyberpunk, Glass, Midnight, Sunset)
- 🧩 Modular widget system (plugin-style architecture)
- ✨ Creative widgets with animations and personality
- 💾 Persistent layouts (widgets restore on restart)
- 🖱️ Drag, resize, hover-glow, and fade-in animations
- 🎛️ Widget presets (Minimal / Focus / Fun)
- 🧠 Designed for real daily use, not just demo purposes

---

## 🧩 Available Widgets

### 🕒 Creative Clock Widget
- Live time with blinking animation
- Time-based greeting (Morning / Afternoon / Evening)
- Date display
- Theme-aware accent colors

### 📝 Creative Notes Widget
- Auto-generated title (from first line)
- 📌 Pin / unpin (always-on-top)
- Paper styles (Yellow, Blue, White, Theme)
- Clean hierarchy (title vs content)

### ☑️ Creative To-Do Widget
- Checkbox-based tasks
- Live progress bar
- Completed / total counter
- 🎉 Celebration when all tasks are done
- Persistent task state

### 📊 System Monitor Widget
- Animated CPU, RAM, and Battery bars
- Real-time updates
- Accent-colored visual indicators

---

## 🎨 UI & UX Features

- Floating card-style widgets with fake depth & shadows
- Hover glow using theme accent color
- Smooth fade-in animation when widgets appear
- Resizable widgets via drag handle
- Right-click context menu (Edit / Close)
- Widget editor with live customization
- Presets for instant personality switching

---

## 🧠 Architecture Overview

```text
widgetlab/
│
├── main.py
│
├── core/
│   ├── widget_base.py        # Base widget engine (drag, resize, effects)
│   ├── widget_manager.py    # App controller & dashboard logic
│   ├── layout_manager.py    # Save & restore layouts
│
├── ui/
│   ├── dashboard.py         # Premium dashboard UI
│   ├── widget_editor.py     # Widget customization & presets
│   └── theme_manager.py     # Theme definitions
│
├── widgets/
│   ├── clock_widget.py
│   ├── notes_widget.py
│   ├── todo_widget.py
│   └── system_widget.py
│
└── data/
    └── widgets.json         # Persistent layout storage
