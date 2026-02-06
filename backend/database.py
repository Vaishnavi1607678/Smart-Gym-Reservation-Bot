import sqlite3

conn = sqlite3.connect("gym.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS bookings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    hour INTEGER
)
""")

conn.commit()
