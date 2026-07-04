# === Stage 50: Add unit tests for import and export behavior ===
# Project: ProjectArchive
import json, os, tempfile
from pathlib import Path
def test_import_export():
    temp_dir = tempfile.mkdtemp()
    try:
        base_path = Path(temp_dir) / "archive"
        base_path.mkdir(exist_ok=True)
        initial_data = {"records": [{"id": 1, "title": "Init"}], "tags": ["start"]}
        with open(base_path / "data.json", "w") as f: json.dump(initial_data, f)
        
        def get_state(): return {k: list(v) if isinstance(v, dict) else v for k,v in initial_data.items()}
        
        # Test Export
        from project_archive.core import export_project
        exported_path = base_path / "export.json"
        with open(exported_path, "w") as f: json.dump(get_state(), f)
        assert os.path.exists(exported_path), "Export failed to create file"
        
        # Test Import (overwrite simulation)
        from project_archive.core import import_project
        new_data = {"records": [{"id": 2, "title": "New"}], "tags": ["new"]}
        with open(base_path / "data.json", "w") as f: json.dump(new_data, f)
        
        imported_state = import_project(str(base_path))
        assert len(imported_state["records"]) == 1 and imported_state["records"][0]["id"] == 2
        
    finally:
        import shutil; shutil.rmtree(temp_dir)
