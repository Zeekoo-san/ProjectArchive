# === Stage 27: Add monthly summary calculations ===
# Project: ProjectArchive
from datetime import datetime, timedelta
import os

def calculate_monthly_summary(records):
    monthly_stats = {}
    for rec in records:
        date_str = rec.get('date', '')
        if not date_str: continue
        try:
            dt = datetime.strptime(date_str, '%Y-%m-%d')
            key = f"{dt.year}-{dt.month}"
            if key not in monthly_stats:
                monthly_stats[key] = {'count': 0, 'tags': set(), 'decisions': []}
            monthly_stats[key]['count'] += 1
            for tag in rec.get('tags', []):
                monthly_stats[key]['tags'].add(tag)
            if rec.get('type') == 'decision':
                monthly_stats[key]['decisions'].append(rec.get('title'))
        except ValueError: pass
    return {k: {'count': v['count'], 'unique_tags': len(v['tags']), 'decisions_count': len(v['decisions'])} for k, v in sorted(monthly_stats.items())}

def generate_monthly_report(records, output_file='monthly_summary.txt'):
    stats = calculate_monthly_summary(records)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("=== ProjectArchive Monthly Summary ===\n\n")
        for month in sorted(stats.keys()):
            data = stats[month]
            f.write(f"{month}: {data['count']} records | Tags: {data['unique_tags']} | Decisions: {data['decisions_count']}\n")
    print(f"Monthly summary written to {output_file}")
