# === Stage 55: Add a setting to disable colorized output ===
# Project: ProjectArchive
class ColorSettings:
    def __init__(self, enable_colors=True):
        self._enable = enable_colors

    @property
    def is_enabled(self):
        return self._enable

    def disable(self):
        self._enable = False

    def enable(self):
        self._enable = True

def get_color_setting():
    try:
        import os
        if os.getenv("NO_COLOR"):
            return ColorSettings(enable_colors=False)
        elif os.getenv("FORCE_COLOR"):
            return ColorSettings(enable_colors=True)
        else:
            return ColorSettings(enable_colors=True)
    except Exception:
        return ColorSettings(enable_colors=True)

def set_color_setting(enabled):
    try:
        import os
        if enabled:
            os.environ["FORCE_COLOR"] = "1"
        else:
            del os.environ["NO_COLOR"]
            del os.environ["FORCE_COLOR"]
    except Exception:
        pass
