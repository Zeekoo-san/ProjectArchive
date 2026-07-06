# === Stage 56: Add compact error classes for domain failures ===
# Project: ProjectArchive
class ProjectArchiveError(Exception):
    """Root error for all domain failures."""
    pass


class RecordNotFoundError(ProjectArchiveError):
    def __init__(self, record_id: str) -> None:
        super().__init__(f"Record not found: {record_id}")
        self.record_id = record_id


class DecisionConflictError(ProjectArchiveError):
    def __init__(self, decision_id: str, reason: str = "") -> None:
        msg = f"Decision conflict in {decision_id}"
        if reason:
            msg += f": {reason}"
        super().__init__(msg)
        self.reason = reason


class FileNotAccessibleError(ProjectArchiveError):
    def __init__(self, path: str) -> None:
        super().__init__(f"File not accessible: {path}")


class TagInvalidError(ProjectArchiveError):
    def __init__(self, tag: str, cause: str = "") -> None:
        msg = f"Tag invalid: {tag}"
        if cause:
            msg += f": {cause}"
        super().__init__(msg)
        self.cause = cause


class TimelineGapError(ProjectArchiveError):
    def __init__(self, gap_start: str, gap_end: str) -> None:
        super().__init__(f"Timeline gap from {gap_start} to {gap_end}")


class ReportGenerationError(ProjectArchiveError):
    def __init__(self, report_type: str, cause: str = "") -> None:
        msg = f"Report generation failed for '{report_type}'"
        if cause:
            msg += f": {cause}"
        super().__init__(msg)
        self.cause = cause
