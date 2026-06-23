# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: ProjectArchive
class CommandDispatcher:
    def __init__(self, handlers):
        self.handlers = {cmd.lower(): handler for cmd, handler in handlers.items()}

    def dispatch(self, raw_input):
        if not raw_input.strip(): return None
        parts = raw_input.split(maxsplit=1)
        cmd = parts[0]
        args = parts[1].strip() if len(parts) > 1 else ""
        handler = self.handlers.get(cmd)
        if handler: return handler(args)
        print(f"Unknown command: {cmd}")
        return None

    def register(self, name, func):
        self.handlers[name.lower()] = func
