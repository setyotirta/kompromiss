# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: GoalLadder
import argparse

def main():
    parser = argparse.ArgumentParser(description="GoalLadder: Трекер целей")
    sub = parser.add_subparsers(dest="command")

    p_create = sub.add_parser("create", help="Создать цель")
    p_create.add_argument("name", help="Название цели")
    p_create.add_argument("--steps", type=int, help="Количество шагов")
    p_create.add_argument("--deadline", help="Дедлайн (YYYY-MM-DD)")
    p_create.add_argument("--priority", choices=["low", "medium", "high"], default="medium")

    p_list = sub.add_parser("list", help="Посмотреть цели")

    p_show = sub.add_parser("show", help="Показать цель")
    p_show.add_argument("id", help="ID цели")

    p_update = sub.add_parser("update", help="Обновить цель")
    p_update.add_argument("id", help="ID цели")
    p_update.add_argument("--done", action="store_true", help="Отметить как выполненную")
    p_update.add_argument("--step", type=int, help="Текущий шаг")
    p_update.add_argument("--deadline", help="Новый дедлайн")
    p_update.add_argument("--priority", choices=["low", "medium", "high"])

    p_delete = sub.add_parser("delete", help="Удалить цель")
    p_delete.add_argument("id", help="ID цели")

    args = parser.parse_args()
    if args.command == "create":
        GoalManager.create_goal(args.name, args.steps, args.deadline, args.priority)
    elif args.command == "list":
        GoalManager.list_goals()
    elif args.command == "show":
        GoalManager.show_goal(args.id)
    elif args.command == "update":
        GoalManager.update_goal(args.id, args.done, args.step, args.deadline, args.priority)
    elif args.command == "delete":
        GoalManager.delete_goal(args.id)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
