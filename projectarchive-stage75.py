# === Stage 75: Add a validation report that lists warnings and errors ===
# Project: ProjectArchive
def validate_archive():
    warnings = []
    errors = []
    for record in records:
        if not record.get("title"):
            errors.append(f"Record {record['id']} missing title")
        if record.get("date") and (not isinstance(record["date"], str) or len(record["date"]) < 10):
            warnings.append(f"Record {record['id']} date may be invalid: {record['date']}")
    for decision in decisions:
        if not decision.get("title"):
            errors.append(f"Decision {decision['id']} missing title")
        if not decision.get("rationale"):
            errors.append(f"Decision {decision['id']} missing rationale")
    for f in files:
        if not f.get("filename"):
            warnings.append(f"File entry missing filename")
    tags = set()
    for item in records + decisions:
        for t in item.get("tags", []):
            if not isinstance(t, str) or len(t.strip()) == 0:
                errors.append(f"Empty tag found on {item['id']}")
            else:
                tags.add(t.strip().lower())
    if len(tags) < 1 and warnings:
        warnings.append("No valid tags were collected across records and decisions")
    report = {"warnings": warnings, "errors": errors}
    return report
