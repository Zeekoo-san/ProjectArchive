# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: ProjectArchive
import unittest
from project_archive import ProjectArchive, Record

class TestProjectArchiveEdgeCases(unittest.TestCase):
    def setUp(self):
        self.arch = ProjectArchive()

    def test_delete_nonexistent_record(self):
        with self.assertRaises(ValueError) as ctx:
            self.arch.delete_record("non-existent-id")
        self.assertIn("not found", str(ctx.exception).lower())

    def test_update_empty_content(self):
        rec = Record(id="123", content="old text")
        self.arch.add_record(rec)
        with self.assertRaises(ValueError) as ctx:
            self.arch.update_record("123", "")
        self.assertIn("content cannot be empty", str(ctx.exception).lower())

    def test_update_missing_id(self):
        rec = Record(id="456", content="test")
        self.arch.add_record(rec)
        with self.assertRaises(ValueError) as ctx:
            self.arch.update_record("missing-id", "new text")
        self.assertIn("not found", str(ctx.exception).lower())

    def test_delete_last_tag(self):
        rec = Record(id="1", content="test", tags=["tag-a"])
        self.arch.add_record(rec)
        self.arch.delete_record("1")
        with self.assertRaises(ValueError) as ctx:
            self.arch.delete_tag("tag-a")
        self.assertIn("no records using tag", str(ctx.exception).lower())

    def test_update_with_invalid_tags(self):
        rec = Record(id="789", content="test")
        self.arch.add_record(rec)
        with self.assertRaises(ValueError) as ctx:
            self.arch.update_record("789", "new text", tags=["tag-a"])
        self.assertIn("tags must be list of strings", str(ctx.exception).lower())

if __name__ == "__main__":
    unittest.main()
