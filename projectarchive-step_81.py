# === Stage 81: Add final README text as a module string with usage examples ===
# Project: ProjectArchive
def print_usage():
    """Print usage examples for ProjectArchive."""
    import project_archive as pa
    # Create a new record
    record = pa.Record(
        title="First Record",
        body="This is my first record in the archive.",
        tags=["example", "beginner"],
        created_by="Alice",
        timestamp=pa.Timestamp("2024-01-15 10:30"),
    )
    print(f"Created record: {record.title} by {record.created_by}")

    # Create a decision and link it to the record
    decision = pa.Decision(
        title="Go with Python",
        body="We chose Python for its simplicity.",
        options=["Python", "Rust", "JavaScript"],
        outcome="Python",
        linked_records=[record],
        timestamp=pa.Timestamp("2024-01-16 14:00"),
    )
    print(f"Made decision: {decision.title} -> Outcome: {decision.outcome}")

    # Create a file and attach it to the record
    file_entry = pa.File(
        name="notes.txt",
        content="Meeting notes here.",
        attached_to=record,
        timestamp=pa.Timestamp("2024-01-17 09:00"),
    )
    print(f"Attached file: {file_entry.name} to record '{record.title}'")

    # Create a timeline event for the project
    timeline_event = pa.TimelineEvent(
        title="Project Kickoff",
        description="Started ProjectArchive.",
        timestamp=pa.Timestamp("2024-01-15 09:00"),
        participants=["Alice", "Bob"],
    )
    print(f"Timeline event: {timeline_event.title}")

    # Create a report summarizing the archive state
    summary = pa.Report(
        title="Monthly Summary",
        records=pa.RecordSummary(count=len(pa.get_all_records())),
        decisions=pa.DecisionSummary(count=len(pa.get_all_decisions())),
        files=pa.FileSummary(count=len(pa.get_all_files())),
        timeline_events=pa.TimelineEventSummary(count=len(pa.get_all_timeline_events())),
    )
    print(f"Report: {summary.title} - {summary.records.count} records, {summary.decisions.count} decisions")

    # Add a tag and use it for filtering
    tag = pa.Tag(name="project-archive", description="Main project tag")
    record.tags.append(tag)
    print(f"Added tag '{tag.name}' to record. Filtered results: {pa.get_records_by_tag(tag)}")

    # Print all timeline events in chronological order
    events = pa.get_timeline_events_sorted()
    for event in events[:5]:  # Show first 5
        print(f"  - {event.title} at {event.timestamp}")

if __name__ == "__main__":
    print("=== ProjectArchive Usage Examples ===")
    print_usage()
