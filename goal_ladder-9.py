# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: GoalLadder
import json, sys
from pathlib import Path

def load_initial_data(json_string: str) -> dict:
    """Загружает начальные данные из JSON-строки."""
    try:
        data = json.loads(json_string)
        
        # Валидация структуры данных
        required_keys = {'goals', 'achievements'}
        if not all(key in data for key in required_keys):
            raise ValueError(f"Необходимы ключи: {required_keys}")
            
        goals_data = data.get('goals', [])
        achievements_data = data.get('achievements', [])
        
        # Преобразование списков в словари для быстрого доступа по ID
        goals_map = {}
        for goal in goals_data:
            if 'id' not in goal:
                raise ValueError("Каждая цель должна иметь уникальный ключ 'id'")
            goals_map[goal['id']] = {
                'title': goal.get('title', ''),
                'steps': goal.get('steps', []),
                'deadline': goal.get('deadline'),
                'status': goal.get('status', 'in_progress')
            }
            
        achievements_map = {}
        for achievement in achievements_data:
            if 'id' not in achievement:
                raise ValueError("Каждое достижение должно иметь уникальный ключ 'id'")
            achievements_map[achievement['id']] = {
                'title': achievement.get('title', ''),
                'date_achieved': achievement.get('date_achieved'),
                'goal_id': achievement.get('goal_id')
            }
            
        return {'goals': goals_map, 'achievements': achievements_map}
        
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        sys.exit(1)

# Пример использования (раскомментируйте для тестирования):
if __name__ == "__main__":
    initial_json = '''{
        "goals": [
            {"id": 1, "title": "Изучить Python", "steps": ["Установить IDE", "Пройти курс"], "deadline": "2024-12-31", "status": "in_progress"},
            {"id": 2, "title": "Написать проект", "steps": ["Спроектировать архитектуру", "Реализовать MVP"], "deadline": null, "status": "pending"}
        ],
        "achievements": [
            {"id": 101, "title": "Первый код запущен", "date_achieved": "2024-06-01", "goal_id": 1}
        ]
    }'''
    
    loaded_data = load_initial_data(initial_json)
    print(f"Загружено {len(loaded_data['goals'])} целей и {len(loaded_data['achievements'])} достижений.")
