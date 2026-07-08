# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: ProjectArchive
def recommend_priority(records: list[dict]) -> dict[str, float]:
    scores = {}
    for r in records:
        name = r.get("name", "")
        score = 0.0
        if "critical" in str(r).lower():
            score += 3.0
        elif "important" in str(r).lower():
            score += 2.0
        elif "low" in str(r).lower():
            score -= 1.0
        score += len(str(r)) / 100.0
        scores[name] = round(score, 3)
    return {k: v for k, v in sorted(scores.items(), key=lambda x: -x[1])}
