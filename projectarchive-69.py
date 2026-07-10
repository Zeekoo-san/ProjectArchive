# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: ProjectArchive
def reset_demo_data():
    """Reset demo data for manual testing."""
    import os, shutil

    project_dir = os.path.dirname(os.path.abspath(__file__))
    archive_dir = os.path.join(project_dir, "archive")
    if os.path.exists(archive_dir):
        shutil.rmtree(archive_dir)

    timeline_file = os.path.join(project_dir, "timeline.csv")
    if os.path.exists(timeline_file):
        with open(timeline_file, 'w') as f:
            f.write("date,action,description\n")

    print("Demo data reset complete.")

if __name__ == "__main__":
    reset_demo_data()
