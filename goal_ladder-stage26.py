# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: GoalLadder
def demo_quick_test():
    print("=" * 50)
    print("DEMO: Quick Manual Test for GoalLadder")
    print("=" * 50)

    # Create a goal
    goal = create_goal("Learn Python", "2024-12-31", steps=["Install PyCharm", "Write first script", "Debug errors"])

    # Add progress
    add_progress(goal, {"step": "Write first script", "done": True})
    add_progress(goal, {"step": "Debug errors", "done": False})

    print(f"\nGoal: {goal['name']}")
    print(f"Deadline: {goal['deadline']}")
    print(f"Progress: {sum(1 for p in goal['progress'] if p.get('done'))}/{len(goal['progress'])} steps done")

    # Simulate user input
    cmd = "show_goal 1"
    while cmd != "exit":
        result = handle_command(cmd)
        print(result)
        cmd = input("Enter command (or 'exit'): ").strip()

    print("\nDemo complete. Goodbye!")
