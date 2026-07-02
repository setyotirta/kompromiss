# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: GoalLadder
class TagManager:
    def __init__(self, goals):
        self.goals = goals
        self.tags = {}  # {tag_name: set(goal_ids)}
    
    def add_tag(self, goal_id, tag_name):
        if not tag_name.strip(): return False
        if goal_id not in self.goals: return False
        if tag_name not in self.tags: self.tags[tag_name] = set()
        self.tags[tag_name].add(goal_id)
        self._update_goal_tags(goal_id, {tag_name})
        return True
    
    def remove_tag(self, goal_id, tag_name):
        if tag_name not in self.tags or goal_id not in self.tags[tag_name]: return False
        self.tags[tag_name].discard(goal_id)
        if not self.tags[tag_name]: del self.tags[tag_name]
        self._update_goal_tags(goal_id, set())
        return True
    
    def _update_goal_tags(self, goal_id, tag_set):
        goal = self.goals[goal_id]
        current_tags = {t for t in goal.get('tags', [])}
        to_add = tag_set - current_tags
        to_remove = current_tags - tag_set
        if not (to_add or to_remove): return
        
        new_tags_list = list(tag_set)
        goal['tags'] = new_tags_list
        # Сохранение в зависимости от вашего хранилища, например:
        # db.update_goal(goal_id, {'tags': new_tags_list})
