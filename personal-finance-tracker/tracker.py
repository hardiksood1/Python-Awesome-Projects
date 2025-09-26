from database import get_connection

def add_income(amount, category):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO transactions (type, category, amount) VALUES (?, ?, ?)",
        ("Income", category, amount)
    )
    conn.commit()
    conn.close()

def add_expense(amount, category):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO transactions (type, category, amount) VALUES (?, ?, ?)",
        ("Expense", category, amount)
    )
    conn.commit()
    conn.close()

def view_summary():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM transactions WHERE type = 'Income'")
    total_income = cursor.fetchone()[0] or 0.0

    cursor.execute("SELECT SUM(amount) FROM transactions WHERE type = 'Expense'")
    total_expenses = cursor.fetchone()[0] or 0.0

    balance = total_income - total_expenses
    conn.close()

    return {
        "Total Income": total_income,
        "Total Expenses": total_expenses,
        "Balance": balance
    }