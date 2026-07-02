# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: ProjectArchive
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent))
from project_archive import ProjectArchive

def run_demo():
    archive = ProjectArchive("demo_project")
    
    # Create initial record and decision
    archive.add_record("Initial Setup", "Project initialized with basic structure.")
    archive.make_decision("Architecture Choice", "Selected dependency-free Python stack for portability.")
    
    # Add a sample file content
    archive.upload_file("config.txt", "DEBUG=false\nLOG_LEVEL=INFO")
    
    # Tag the entry and add to timeline
    archive.tag_entry("Initial Setup", ["setup", "v1"])
    archive.add_timeline_event("Day 0", "Project structure created.")
    
    # Generate a simple report
    report = archive.generate_report()
    print(report)

if __name__ == "__main__":
    run_demo()
