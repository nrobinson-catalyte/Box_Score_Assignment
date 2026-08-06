import sqlite3


DATABASE_NAME = "nba_tracker.db"


def get_connection():
    return sqlite3.connect(DATABASE_NAME)


def create_tables():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Players (
        Player_ID INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        Height TEXT,
        Weight TEXT,
        College TEXT
    )
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Teams (
        Team_ID INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        City TEXT,
        State TEXT,
        Arena TEXT,
        Record TEXT
    )
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Games (
        Game_ID INTEGER PRIMARY KEY,
        Home_Team TEXT,
        Away_Team TEXT,
        Date TEXT,
        Arena TEXT
    )
    """)


    connection.commit()
    connection.close()