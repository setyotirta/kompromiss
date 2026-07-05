# === Stage 20: Добавь восстановление записей из архива ===
# Project: GoalLadder
import json, os, datetime

def restore_from_archive():
    archive_path = 'goals_backup.json'
    if not os.path.exists(archive_path): return
    
    try:
        with open(archive_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        now = datetime.datetime.now()
        for item in data.get('goals', []):
            if item['status'] == 'archived':
                created_at = datetime.datetime.fromisoformat(item['created_at'])
                age_days = (now - created_at).days
                
                if age_days <= 30:
                    continue
                
                task_list = item.pop('tasks', [])
                
                for i, step in enumerate(task_list):
                    deadline_str = step.get('deadline')
                    if not deadline_str: continue
                    
                    try:
                        deadline = datetime.datetime.fromisoformat(deadline_str)
                        days_left = (deadline - now).days
                        
                        if days_left < 0 and item['status'] == 'completed':
                            item['tasks'][i]['done'] = True
                            
                    except ValueError:
                        pass
                
                item.pop('archived_at', None)
                
        with open(archive_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
    except Exception:
        pass
