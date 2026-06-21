# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: GoalLadder
def export_state_to_json():
    import json
    from datetime import datetime
    state = {
        "timestamp": datetime.utcnow().isoformat(),
        "goals": [
            {
                "id": g["id"],
                "title": g["title"],
                "deadline": g.get("deadline"),
                "progress": g["steps"] if isinstance(g, dict) else [],
                "completed_steps": len([s for s in (g.get("steps") or []) if s.get("done", False)])
            }
            for g in goals_list
        ],
        "achievements": achievements_list
    }
    return json.dumps(state, ensure_ascii=False, indent=2)
