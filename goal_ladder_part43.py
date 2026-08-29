# === Stage 43: Добавь пагинацию длинных списков ===
# Project: GoalLadder
def paginate(data, page_size=10):
    """Paginate a list of items and yield pages."""
    for i in range(0, len(data), page_size):
        yield data[i:i + page_size]
