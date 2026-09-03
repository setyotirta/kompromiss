# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: GoalLadder
def migrate_goal_structure():
    """
    Migration: Add new fields to Goal structure.
    This migration updates the schema to include progress tracking,
    deadlines, and achievements.
    """
    migration_version = 2
    
    # Define the new schema
    new_goal_schema = {
        'id': str,
        'title': str,
        'description': str,
        'steps': list,
        'progress': int,
        'deadline': str,
        'completed': bool,
        'achievements': list,
        'created_at': str,
        'updated_at': str
    }
    
    # Check if migration is needed
    current_version = get_migration_version()
    
    if current_version < migration_version:
        print(f"Migrating from version {current_version} to {migration_version}...")
        migrate_goals_to_new_schema(new_goal_schema)
        set_migration_version(migration_version)
        print("Migration complete!")
    else:
        print("Already on latest migration version.")
