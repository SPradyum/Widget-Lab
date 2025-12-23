import json
import os

LAYOUT_FILE = r"E:\Documents\Projects\Python\widgetlab\data\widgets.json"

class LayoutManager:

    @staticmethod
    def save(widgets):
        data = []

        for w in widgets:
            info = w.serialize()
            if info:
                data.append(info)

        with open(LAYOUT_FILE, "w") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def load():
        if not os.path.exists(LAYOUT_FILE):
            return []

        with open(LAYOUT_FILE) as f:
            data = json.load(f)

    # Ensure correct format
        if isinstance(data, list):
            return data
        
        return []

