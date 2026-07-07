# === Stage 61: Add performance timing for core list and search operations ===
# Project: ProjectArchive
import time
from collections import OrderedDict

class PerformanceTimer:
    def __init__(self):
        self._timings = {}
    
    def measure(self, operation_name, func):
        start = time.perf_counter()
        result = func()
        end = time.perf_counter()
        duration = (end - start) * 1000
        
        if operation_name not in self._timings:
            self._timings[operation_name] = []
        
        self._timings[operation_name].append({
            'duration': duration,
            'timestamp': time.time()
        })
        
        return result
    
    def get_average(self, operation_name):
        if operation_name not in self._timings:
            return 0.0
        
        durations = [t['duration'] for t in self._timings[operation_name]]
        return sum(durations) / len(durations)
    
    def get_worst_case(self, operation_name):
        if operation_name not in self._timings:
            return 0.0
        
        durations = [t['duration'] for t in self._timings[operation_name]]
        return max(durations)
    
    def get_best_case(self, operation_name):
        if operation_name not in self._timings:
            return float('inf')
        
        durations = [t['duration'] for t in self._timings[operation_name]]
        return min(durations)
