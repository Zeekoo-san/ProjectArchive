# === Stage 44: Add backup creation for the data file ===
# Project: ProjectArchive
import shutil, os, datetime
def backup_data(data_file="archive.db", dest_dir=".backups"):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    src_path = data_file
    dst_path = os.path.join(dest_dir, f"{os.path.basename(src_path)}_{timestamp}")
    try:
        shutil.copy2(src_path, dst_path)
        print(f"Backup created at {dst_path}")
    except Exception as e:
        print(f"Backup failed: {e}")

if __name__ == "__main__":
    backup_data()
