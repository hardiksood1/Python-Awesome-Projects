from database import get_connection

def set_goal(goal_amount):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO savings_goal (id, goal_amount) VALUES (1, ?)", (goal_amount,))
    conn.commit()
    conn.close()

def get_goal():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT goal_amount FROM savings_goal WHERE id = 1")
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None

def suggest_plans(goal_amount, balance=0.0):
    remaining = max(goal_amount - balance, 0)
    if remaining == 0:
        return {"message": "🎉 Goal already achieved!", "plans": []}

    # Common saving plans
    monthly_options = [1000, 2000, 3000, 4000, 5000]
    plans = []
    for monthly in monthly_options:
        months_required = (remaining + monthly - 1) // monthly  # ceiling division
        plans.append({"monthly": monthly, "months": int(months_required)})

    return {"remaining": remaining, "plans": plans}

def calculate_monthly_for_months(goal_amount, months, balance=0.0):
    remaining = max(goal_amount - balance, 0)
    if months > 0:
        monthly_required = remaining / months
        return monthly_required
    return None

def track_savings_progress(balance):
    goal_amount = get_goal()
    if goal_amount:
        remaining = goal_amount - balance
        if remaining > 0:
            return f"You need to save {remaining:.2f} more to reach your goal."
        else:
            return "🎉 Congratulations! You've reached your savings goal."
    return "No savings goal set."