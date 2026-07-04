# === Stage 53: Add command help text and usage examples ===
# Project: ProjectArchive
def print_help():
    """Print usage and help text for ProjectArchive CLI."""
    print("ProjectArchive Knowledge Archive")
    print("=" * 40)
    print("\nUsage: python project_archive.py <command> [options]")
    print("\nCommands:")
    print("  init              Initialize a new archive repository.")
    print("  record            Add a new decision or record entry.")
    print("  file              Upload or link a document to an entry.")
    print("  tag               Assign tags to existing records.")
    print("  timeline          Generate a chronological view of events.")
    print("  report            Summarize archive statistics and status.")
    print("\nOptions:")
    print("  -h, --help        Show this help message and exit.")
    print("  -v, --verbose     Enable detailed output logging.")
    print("  -o <file>         Output results to a specific file path.")
    print("\nExamples:")
    print("  python project_archive.py init")
    print("  python project_archive.py record -t 'Architecture' -d 'Use Python for backend'")
    print("  python project_archive.py timeline --format markdown > history.md")
    print("  python project_archive.py report -o summary.txt")
