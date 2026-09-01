# === Stage 45: Добавь восстановление из резервной копии ===
# Project: GoalLadder
def load_backup(backup_path):
    """Восстанавливает цели из JSON-резервной копии. """
    import json
    if not os.path.exists(backup_path):
        print(f"Файл резервной копии не найден: {backup_path}")
        return
    try:
        with open(backup_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        goals = data.get('goals', [])
        print(f"Восстановлено {len(goals)} целей из резервной копии.")
        for g in goals:
            add_goal(g)
    except Exception as e:
        print(f"Ошибка при загрузке резервной копии: {e}")
