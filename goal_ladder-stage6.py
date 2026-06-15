# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: GoalLadder
class GoalFilter:
    def __init__(self, goals):
        self.goals = goals
    
    def filter_by_status(self, status):
        return [g for g in self.goals if g.get('status') == status]
    
    def filter_by_category(self, category):
        return [g for g in self.goals if g.get('category', '').lower() == category.lower()]
    
    def filter_by_tag(self, tag):
        tags = set(g.get('tags', []))
        return [g for g in self.goals if any(tag in t for t in tags)]
    
    def combine_filters(self, status=None, category=None, tag=None):
        filtered = self.goals
        if status: filtered = self.filter_by_status(status)
        if category: filtered = self.filter_by_category(category)
        if tag: filtered = self.filter_by_tag(tag)
        return filtered
