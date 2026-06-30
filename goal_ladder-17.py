# === Stage 17: Добавь группировку записей по категориям ===
# Project: GoalLadder
def group_by_category(records):
    from collections import defaultdict
    grouped = defaultdict(list)
    for record in records:
        cat = record.get('category', 'General')
        grouped[cat].append(record)
    return dict(sorted(grouped.items()))
