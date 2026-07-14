# === Stage 76: Add graceful keyboard interrupt handling in the CLI entry point ===
# Project: ProjectArchive
import sys


def on_sigint(signum, frame):
    """Handle Ctrl+C gracefully: abort any active task and exit cleanly."""
    print("\n\nInterrupted by user.", file=sys.stderr)
    sys.exit(130)
