# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: GoalLadder
class _ANSI:
    _RESET = "\033[0m"
    _RED = "\033[31m"
    _GREEN = "\033[32m"
    _YELLOW = "\033[33m"
    _BLUE = "\033[34m"
    _CYAN = "\033[36m"
    _BOLD = "\033[1m"
    _DIM = "\033[2m"
    _OK = _GREEN + _BOLD
    _WARN = _YELLOW + _BOLD
    _FAIL = _RED + _BOLD
    _INFO = _BLUE

    @staticmethod
    def enabled():
        return "TERM" in os.environ and os.environ.get("GOAL_COLOR", "1") != "0"

    @staticmethod
    def colorize(text, code):
        if _ANSI.enabled():
            return f"{code}{text}{_ANSI._RESET}"
        return text

    @staticmethod
    def success(text):
        return _ANSI.colorize(text, _ANSI._OK)
    @staticmethod
    def warning(text):
        return _ANSI.colorize(text, _ANSI._WARN)
    @staticmethod
    def error(text):
        return _ANSI.colorize(text, _ANSI._FAIL)
    @staticmethod
    def info(text):
        return _ANSI.colorize(text, _ANSI._INFO)
