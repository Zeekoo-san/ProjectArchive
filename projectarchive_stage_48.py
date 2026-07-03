# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: ProjectArchive
import unittest
from datetime import date, timedelta

class TestProjectArchiveHelpers(unittest.TestCase):
    def test_validate_record_date(self):
        self.assertTrue(ProjectArchive._validate_date(date.today()))
        with self.assertRaises(ValueError):
            ProjectArchive._validate_date("not a date")

    def test_create_decision_summary(self):
        decision = {"title": "Refactor", "status": "done"}
        summary = ProjectArchive._create_decision_summary(decision)
        self.assertIn("Refactor", summary)
        self.assertIn("done", summary.lower())

    def test_generate_timeline_entry(self):
        entry = ProjectArchive._generate_timeline_entry(
            date.today(), "Update docs"
        )
        self.assertEqual(entry["date"], date.today().isoformat())
        self.assertEqual(entry["action"], "Update docs")

    def test_calculate_project_age_days(self):
        start_date = date.today() - timedelta(days=30)
        age_days = ProjectArchive._calculate_project_age(start_date, date.today())
        self.assertEqual(age_days, 30)
