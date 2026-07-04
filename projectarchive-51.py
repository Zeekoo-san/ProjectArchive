# === Stage 51: Add unit tests for search and filter behavior ===
# Project: ProjectArchive
import unittest
from project_archive import Archive, Record, Decision, File, Tag, TimelineEvent, Report

class TestSearchFilter(unittest.TestCase):
    def setUp(self):
        self.archive = Archive()
        
    def test_search_by_keyword_in_content(self):
        rec1 = Record("Intro", "Welcome to the archive.", tags=["intro"])
        rec2 = Record("Guide", "Use this guide for setup.", tags=["guide"])
        dec1 = Decision("Opt v1", "Chosen version 1.", tags=["v1"])
        self.archive.add_record(rec1)
        self.archive.add_record(rec2)
        self.archive.add_decision(dec1)
        
        results = self.archive.search(keyword="setup")
        self.assertEqual(len(results), 1)
        self.assertIn("Guide", str(results[0]))

    def test_filter_by_tag(self):
        rec1 = Record("A", "Content A.", tags=["dev"])
        rec2 = Record("B", "Content B.", tags=["prod"])
        dec1 = Decision("C", "Decision C.", tags=["dev"])
        self.archive.add_record(rec1)
        self.archive.add_record(rec2)
        self.archive.add_decision(dec1)
        
        results = self.archive.filter(tags=["dev"])
        self.assertEqual(len(results), 2)

    def test_search_with_multiple_keywords(self):
        rec = Record("X", "This is a very important document.", tags=["key"])
        self.archive.add_record(rec)
        
        results = self.archive.search(keyword="important")
        self.assertTrue(any("very" in str(r.content) for r in results))

    def test_filter_by_date_range(self):
        from datetime import datetime, timedelta
        today = datetime.now()
        rec1 = Record("Old", "Content.", tags=["old"])
        rec2 = Record("New", "Fresh content.", tags=["new"])
        
        self.archive.add_record(rec1)
        self.archive.add_record(rec2)
        
        results = self.archive.filter(date_from=today - timedelta(days=30))
        self.assertEqual(len(results), 2)

    def test_search_returns_only_records(self):
        rec = Record("R", "Text.", tags=["r"])
        dec = Decision("D", "Dec.", tags=["d"])
        rep = Report("Rep", "Report text.", tags=["rep"])
        
        self.archive.add_record(rec)
        self.archive.add_decision(dec)
        self.archive.add_report(rep)
        
        results = self.archive.search(keyword="Text")
        self.assertTrue(isinstance(results[0], Record))
