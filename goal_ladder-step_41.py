# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: GoalLadder
def dry_run(operation, entity, data, success):
    print(f"[DRY-RUN] {operation} {entity}: {'OK' if success else 'FAILED'} - {data}")
