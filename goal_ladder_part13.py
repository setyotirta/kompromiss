# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: GoalLadder
class GoalSearcher:
    def __init__(self, goals):
        self.goals = goals  # список объектов Goal с полями title, description, deadline
    
    def search(self, query):
        if not query.strip():
            return []
        
        q_lower = query.lower()
        results = []
        
        for goal in self.goals:
            text_to_search = f"{goal.title} {goal.description}".lower()
            
            # Поиск по заголовку и описанию (без учёта регистра)
            if q_lower in text_to_search:
                results.append(goal)
                
                # Дополнительная логика для поиска по дедлайну, если он есть
                if hasattr(goal, 'deadline') and goal.deadline:
                    deadline_str = str(goal.deadline).lower()
                    if q_lower in deadline_str:
                        break  # Находим совпадение в дедлайне
        
        return results
