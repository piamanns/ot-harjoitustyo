from database_connection import get_database_connection


def drop_tables(connection):
    """Deletes all database tables.

    Args:
        connection: The Connection-object that represents the database.
    """

    cursor = connection.cursor()

    cursor.execute('''
        DROP TABLE IF EXISTS tf_presets;
    ''')
    cursor.execute('''
        DROP TABLE IF EXISTS metr_presets;
    ''')

    connection.commit()

def create_tables(connection):
    """Creates the database tables.

    Args:
        connection: The Connection-object that represents the database.
    """

    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE tf_presets (
            id INTEGER PRIMARY KEY,
            freq REAL,
            label TEXT
        );
    ''')

    cursor.execute('''
        CREATE TABLE metr_presets (
            id INTEGER PRIMARY KEY,
            bpm INTEGER,
            bpbar INTEGER,
            bunit INTEGER
        );
    ''')

    connection.commit()


def initialize_database():
    """Initializes the database.
    """

    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
