# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: GoalLadder
def parse_date(date_str):
    """
    Parses a date string in DD/MM/YYYY or YYYY-MM-DD format and returns a datetime.date object.
    Returns None if the date is invalid, with a clear error message for user feedback.
    """
    try:
        if '/' in date_str:
            parts = date_str.split('/')
            if len(parts) != 3:
                return None
            day, month, year = int(parts[0]), int(parts[1]), int(parts[2])
            if not (1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2100):
                return None
        else:
            parts = date_str.split('-')
            if len(parts) != 3:
                return None
            year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
            if not (1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2100):
                return None
        
        date_obj = datetime.date(year, month, day)
        
        # Validate the actual calendar day for the given month/year
        if date_obj.day != day or date_obj.month != month or date_obj.year != year:
            return None
            
        return date_obj
    except (ValueError, TypeError):
        return None
