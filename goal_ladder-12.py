# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: GoalLadder
def load_goals_from_file(filepath: str) -> list[dict]:
    try:
        import json
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, list):
            raise ValueError("Файл должен содержать массив целей")
        return [item for item in data if isinstance(item, dict)]
    except FileNotFoundError:
        print(f"Ошибка: файл {filepath} не найден.")
        return []
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON в файле {filepath}: {e}")
        return []
    except Exception as e:
        print(f"Неожиданная ошибка при загрузке файла: {type(e).__name__}: {e}")
        return []
