# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: ProjectArchive
class DryRunMixin:
    def __init__(self, dry_run=False):
        self._dry_run = dry_run

    @property
    def is_dry_run(self):
        return self._dry_run

    def _log_action(self, action_type, target, details=None):
        if not self.is_dry_run:
            raise RuntimeError(f"Action {action_type} on {target} would mutate state (dry-run mode)")
        print(f"[DRY-RUN] Would {action_type}: {target}")
        if details:
            for k, v in details.items():
                print(f"  -> {k}: {v}")

    def _execute_write(self, target, **kwargs):
        self._log_action("WRITE", target, kwargs)
        return None

    def _execute_delete(self, target):
        self._log_action("DELETE", target)
        return True
