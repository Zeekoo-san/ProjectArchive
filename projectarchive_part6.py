# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: ProjectArchive
def delete_record(record_id, confirm=False):
    if record_id in records:
        rec = records[record_id]
        if confirm or input(f"Delete record {rec['title']}? (y/n) ") == 'y':
            del records[record_id]
            print(f"Record {record_id} deleted.")
            return True
    print("Deletion cancelled or not found.")
    return False

def delete_decision(decision_id, confirm=False):
    if decision_id in decisions:
        dec = decisions[decision_id]
        if confirm or input(f"Delete decision {dec['title']}? (y/n) ") == 'y':
            del decisions[decision_id]
            print(f"Decision {decision_id} deleted.")
            return True
    print("Deletion cancelled or not found.")
    return False

def delete_file(file_path, confirm=False):
    if file_path in files:
        f = files[file_path]
        if confirm or input(f"Delete file {f['name']}? (y/n) ") == 'y':
            del files[file_path]
            print(f"File {file_path} deleted.")
            return True
    print("Deletion cancelled or not found.")
    return False

def delete_tag(tag_name, confirm=False):
    if tag_name in tags:
        t = tags[tag_name]
        if confirm or input(f"Delete tag '{tag_name}'? (y/n) ") == 'y':
            del tags[tag_name]
            print(f"Tag {tag_name} deleted.")
            return True
    print("Deletion cancelled or not found.")
    return False

def delete_timeline_event(event_id, confirm=False):
    if event_id in timelines:
        ev = timelines[event_id]
        if confirm or input(f"Delete timeline event '{ev['title']}'? (y/n) ") == 'y':
            del timelines[event_id]
            print(f"Timeline event {event_id} deleted.")
            return True
    print("Deletion cancelled or not found.")
    return False

def delete_report(report_name, confirm=False):
    if report_name in reports:
        r = reports[report_name]
        if confirm or input(f"Delete report '{r['title']}'? (y/n) ") == 'y':
            del reports[report_name]
            print(f"Report {report_name} deleted.")
            return True
    print("Deletion cancelled or not found.")
    return False

# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: ProjectArchive
def delete_record(record_id, confirm=False):
    if record_id in records:
        rec = records[record_id]
        if confirm or input(f"Удалить запись {rec['title']}? (y/n) ") == 'y':
            del records[record_id]
            print(f"Запись {record_id} удалена.")
            return True
    print("Удаление отменено или запись не найдена.")
    return False

def delete_decision(decision_id, confirm=False):
    if decision_id in decisions:
        dec = decisions[decision_id]
        if confirm or input(f"Удалить решение {dec['title']}? (y/n) ") == 'y':
            del decisions[decision_id]
            print(f"Решение {decision_id} удалено.")
            return True
    print("Удаление отменено или решение не найдено.")
    return False

def delete_file(file_path, confirm=False):
    if file_path in files:
        f = files[file_path]
        if confirm or input(f"Удалить файл {f['name']}? (y/n) ") == 'y':
            del files[file_path]
            print(f"Файл {file_path} удален.")
            return True
    print("Удаление отменено или файл не найден.")
    return False

def delete_tag(tag_name, confirm=False):
    if tag_name in tags:
        t = tags[tag_name]
        if confirm or input(f"Удалить тег {t['name']}? (y/n) ") == 'y':
            del tags[tag_name]
            print(f"Тег {tag_name} удален.")
            return True
    print("Удаление отменено или тег не найден.")
    return False

def delete_timeline(timeline_id, confirm=False):
    if timeline_id in timelines:
        tl = timelines[timeline_id]
        if confirm or input(f"Удалить событие {tl['title']}? (y/n) ") == 'y':
            del timelines[timeline_id]
            print(f"Событие {timeline_id} удалено.")
            return True
    print("Удаление отменено или событие не найдено.")
    return False

def delete_report(report_id, confirm=False):
    if report_id in reports:
        r = reports[report_id]
        if confirm or input(f"Удалить отчет {r['title']}? (y/n) ") == 'y':
            del reports[report_id]
            print(f"Отчет {report_id} удален.")
            return True
    print("Удаление отменено или отчет не найден.")
    return False
