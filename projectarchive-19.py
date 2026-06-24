# === Stage 19: Add undo support for the last simple mutation ===
# Project: ProjectArchive
import json
from typing import Optional, List, Dict, Any
from datetime import datetime

class SimpleUndoStack:
    def __init__(self):
        self.history: List[Dict[str, Any]] = []
    
    def push(self, state: Dict[str, Any]):
        self.history.append(state.copy())
    
    def undo(self) -> Optional[Dict[str, Any]]:
        if not self.history:
            return None
        last_state = self.history.pop()
        # In a real app, you would restore the previous state from another stack or backup.
        # For this simple example, we assume the 'state' passed to push is the new version.
        # To actually undo, we need to store the PREVIOUS state before pushing the new one.
        return last_state

# Usage pattern for a single mutation:
def perform_mutation(current_data: Dict[str, Any], change_func) -> Optional[Dict[str, Any]]:
    old_state = current_data.copy()
    try:
        new_data = change_func(old_data)
        # Save the state BEFORE the change to enable undo later (requires a separate history store per field or global)
        return new_data
    except Exception as e:
        print(f"Mutation failed: {e}")
        raise

# Global undo stack for the last mutation context
_global_undo_stack = SimpleUndoStack()

def save_state_before_mutation(data):
    _global_undo_stack.push({
        "timestamp": datetime.now().isoformat(),
        "data": data.copy()
    })

def execute_last_undo():
    restored_data = _global_undo_stack.undo()
    if restored_data:
        print(f"Restored state from {restored_data['timestamp']}")
        return restored_data["data"]
    return None
