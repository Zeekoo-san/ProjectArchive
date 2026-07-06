# === Stage 57: Add structured result objects for command handlers ===
# Project: ProjectArchive
class CommandResult:
    """Generic result for every command handler."""
    def __init__(self, status="ok", message="", data=None, errors=None):
        self.status = status
        self.message = message or ""
        self.data = data
        self.errors = errors or []

    @property
    def is_ok(self):
        return self.status == "ok" and not self.errors

    def to_dict(self):
        out = {"status": self.status, "message": self.message}
        if self.is_ok:
            out["data"] = self.data
        else:
            out["errors"] = self.errors
        return out

    __repr__ = lambda s: f"CommandResult(status={s.status!r}, is_ok={s.is_ok})"


class CommandError(CommandResult):
    """Marker for failed command results."""
    def __init__(self, message="", errors=None):
        super().__init__(status="error", message=message, errors=errors or [])
