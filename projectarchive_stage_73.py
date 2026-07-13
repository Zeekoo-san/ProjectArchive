# === Stage 73: Add a lightweight HTML report export ===
# Project: ProjectArchive
import json, os

def report_to_html(records_path="records.json"):
    with open(records_path) as f:
        records = json.load(f)
    html_parts = ["<html><head><title>ProjectArchive Report</title>",
                  "<style>body{font-family:sans-serif;max-width:800px;margin:auto;padding:2em}",
                  "h1,h2,li,p{margin:.5em 0}</style></head><body>"]
    html_parts.append(f"<h1>ProjectArchive Report</h1>")
    if not records:
        html_parts.append("<p>No records found.</p>")
    else:
        for rec in records:
            title = rec.get("title", "Untitled")
            body = rec.get("body", "")
            date = rec.get("date", "")
            tags_str = "<br>".join(f'<span style="background:#eee;padding:.15em .4em;border-radius:.2em;font-size:.85em">{t}</span>' for t in rec.get("tags", []))
            html_parts.append(f"<h2>{title}</h2>")
            if date:
                html_parts.append(f"<p><strong>Date:</strong> {date}</p>")
            html_parts.append(f"<p>{body.replace('<br>', '<br>').replace('&', '&amp;')}</p>")
            if tags_str:
                html_parts.append(tags_str)
            html_parts.append("<hr>")
    html_parts.append("</body></html>")
    return "\n".join(html_parts)

if __name__ == "__main__":
    print(report_to_html())
