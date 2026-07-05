# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: ProjectArchive
class ColorFormatter:
    def __init__(self):
        self.colors = {
            'HEADER': '\033[95m',
            'OKBLUE': '\033[94m',
            'OKCYAN': '\033[96m',
            'WARNING': '\033[93m',
            'FAIL': '\033[91m',
            'ENDC': '\033[0m'
        }

    def info(self, msg):
        return f"{self.colors['OKCYAN']}{msg}{self.colors['ENDC']}"

    def success(self, msg):
        return f"{self.colors['HEADER']}{msg}{self.colors['ENDC']}"

    def warning(self, msg):
        return f"{self.colors['WARNING']}{msg}{self.colors['ENDC']}"

    def error(self, msg):
        return f"{self.colors['FAIL']}{msg}{self.colors['ENDC']}"

    def reset(self):
        return self.colors['ENDC']

if __name__ == "__main__":
    fmt = ColorFormatter()
    print(fmt.success("Archive initialized"))
    print(fmt.info("Loading records..."))
    print(fmt.warning("Some tags missing."))
    print(fmt.error("Connection timeout!"))
