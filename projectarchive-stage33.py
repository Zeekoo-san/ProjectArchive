# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: ProjectArchive
SETTINGS = {
    "max_history_days": 365,
    "auto_tag_new_files": True,
    "report_format": "markdown",
    "log_level": "INFO"
}

def update_settings(key: str, value):
    if key in SETTINGS and isinstance(SETTINGS[key], (int, float, bool, str)):
        SETTINGS[key] = value
        return f"Updated {key} to {value}"
    raise ValueError(f"Invalid setting key or type mismatch for {key}")

def get_settings():
    import copy
    return copy.deepcopy(SETTINGS)
