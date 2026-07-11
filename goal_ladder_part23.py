# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: GoalLadder
def print_table(rows, headers):
    """Compact table renderer."""
    widths = [len(str(h)) for h in headers]
    for r in rows:
        for i, v in enumerate(r or []):
            if i < len(widths) and len(str(v)) > widths[i]:
                widths[i] = len(str(v))

    fmt = " | ".join(f"{{:<{w}}}" for w in widths) + " |"
    print(fmt.format(*headers))
    sep = "-+-".join("-" * w for w in widths) + "-"
    print(sep)
    for r in rows:
        print(fmt.format(*r))

if __name__ == "__main__":
    goals = [
        {"title": "Finish Python crash course", "steps_done": 12, "total_steps": 15},
        {"title": "Read a book about AI", "steps_done": 3, "total_steps": 8},
        {"title": "Learn Git basics", "steps_done": 6, "total_steps": 6},
    ]
    print_table(
        [[g["title"], f"{round(g['steps_done'] / g['total_steps'], 0)}%", g['total_steps']] for g in goals],
        ["Goal", "Progress", "Steps"]
    )
