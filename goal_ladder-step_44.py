# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: GoalLadder
import shutil, os, json, datetime

def backup_data_file(db_path, backup_dir=None):
    if backup_dir is None:
        backup_dir = "backups"
    os.makedirs(backup_dir, exist_ok=True)
    if not os.path.exists(db_path):
        return None
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"{os.path.basename(db_path)}.{timestamp}.bak")
    shutil.copy2(db_path, backup_path)
    return backup_path
