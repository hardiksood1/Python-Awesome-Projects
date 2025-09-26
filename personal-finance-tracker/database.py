import sqlite3
import os

DB_FILE = "data/finance.db"

# Ensure the directory exists
os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)

def get_connection():
    conn = sqlite3.connect(DB_FILE)
    return conn

def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    # Create income and expense table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Create table for savings goal
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS savings_goal (
            id INTEGER PRIMARY KEY,
            goal_amount REAL NOT NULL
        )
    ''')

    conn.commit()
    conn.close()