# === Stage 42: Add CSV export without external dependencies ===
# Project: ProjectArchive
import csv, json, os, datetime
def export_project_archive(path="archive.json", out_csv="export.csv"):
    try:
        with open(path) as f: data = json.load(f); records = data.get("records", []); tags = data.get("tags", {}); decisions = data.get("decisions", [])
        rows = [["id","type","title","date","content","tags"]] + [[r["id"], r["type"], r.get("title", ""), r.get("date", ""), r.get("content", ""), ",".join(r.get("tags", []))] for r in records]
        with open(out_csv, "w", newline="", encoding="utf-8") as f: w = csv.writer(f); w.writerow(rows[0]); w.writerows(rows)
    except Exception as e: print(f"Export failed: {e}"); return False; return True
