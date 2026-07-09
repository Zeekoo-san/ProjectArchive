# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: ProjectArchive
def _merge_imports(target, source):
    """Merge source imports into target, skipping obvious duplicates."""
    seen = {i.strip() for i in target.imports}
    new_added = []
    for imp in source.imports:
        if imp not in seen and imp != "":
            seen.add(imp)
            target.imports.append(imp)
            new_added.append(imp)
