# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: GoalLadder
def run_cli():
    print("=== GoalLadder CLI ===")
    while True:
        cmd = input("\nКоманда (1-4, q=выход): ").strip()
        if cmd == "q": break
        elif cmd in ("1", "2"): print(f"Действие {cmd}: список целей/добавление цели.")
        elif cmd == "3": print("Действие 3: просмотр прогресса.")
        elif cmd == "4": print("Действие 4: обзор достижений.")
        else: print("Неизвестная команда.")
