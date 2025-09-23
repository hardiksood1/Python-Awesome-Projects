import matplotlib.pyplot as plt
from database import get_connection
import savings
import tracker

# ==========================
# Salary & Expense Charts
# ==========================
def bar_chart_expense():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT category, SUM(amount) FROM transactions WHERE type = 'Expense' GROUP BY category")
    rows = cursor.fetchall()
    conn.close()

    if rows:
        categories = [row[0] for row in rows]
        amounts = [row[1] for row in rows]
        fig, ax = plt.subplots()
        ax.bar(categories, amounts, color="orange")
        ax.set_xlabel('Category')
        ax.set_ylabel('Amount (₹)')
        ax.set_title('Spending by Category')
        plt.xticks(rotation=45)
        return fig
    return None


def pie_chart_expense():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT category, SUM(amount) FROM transactions WHERE type = 'Expense' GROUP BY category")
    rows = cursor.fetchall()
    conn.close()

    if rows:
        categories = [row[0] for row in rows]
        amounts = [row[1] for row in rows]
        fig, ax = plt.subplots()
        ax.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=90)
        ax.set_title('Spending by Category')
        return fig
    return None


def line_chart_expense_over_time():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT date, SUM(amount) FROM transactions WHERE type = 'Expense' GROUP BY date")
    rows = cursor.fetchall()
    conn.close()

    if rows:
        dates = [row[0] for row in rows]
        amounts = [row[1] for row in rows]
        fig, ax = plt.subplots()
        ax.plot(dates, amounts, marker='o', color="red")
        ax.set_xlabel('Date')
        ax.set_ylabel('Amount (₹)')
        ax.set_title('Expenses Over Time')
        plt.xticks(rotation=45)
        return fig
    return None


def stacked_bar_chart_income_expense():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT date, SUM(amount) FROM transactions WHERE type = 'Income' GROUP BY date")
    income_rows = cursor.fetchall()
    cursor.execute("SELECT date, SUM(amount) FROM transactions WHERE type = 'Expense' GROUP BY date")
    expense_rows = cursor.fetchall()
    conn.close()

    if income_rows or expense_rows:
        dates = sorted(list(set([row[0] for row in income_rows] + [row[0] for row in expense_rows])))
        income_dict = {row[0]: row[1] for row in income_rows}
        expense_dict = {row[0]: row[1] for row in expense_rows}
        income_amounts = [income_dict.get(d, 0) for d in dates]
        expense_amounts = [expense_dict.get(d, 0) for d in dates]

        fig, ax = plt.subplots()
        ax.bar(dates, income_amounts, label="Income", color="green")
        ax.bar(dates, expense_amounts, bottom=income_amounts, label="Expense", color="red")
        ax.set_xlabel('Date')
        ax.set_ylabel('Amount (₹)')
        ax.set_title('Income vs Expenses Over Time')
        plt.xticks(rotation=45)
        ax.legend()
        return fig
    return None


def histogram_expense_distribution():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT amount FROM transactions WHERE type = 'Expense'")
    rows = cursor.fetchall()
    conn.close()

    if rows:
        amounts = [row[0] for row in rows]
        fig, ax = plt.subplots()
        ax.hist(amounts, bins=10, color="purple")
        ax.set_xlabel('Expense Amount (₹)')
        ax.set_ylabel('Frequency')
        ax.set_title('Expense Distribution')
        return fig
    return None


# ==========================
# Investment & Goal Charts
# ==========================
def goal_progress_chart():
    summary = tracker.view_summary()
    balance = summary["Balance"]
    goal_amount = savings.get_goal()

    if goal_amount:
        remaining = max(goal_amount - balance, 0)
        achieved = min(balance, goal_amount)

        fig, ax = plt.subplots()
        ax.bar(["Saved"], [achieved], color="blue", label="Saved")
        ax.bar(["Remaining"], [remaining], color="gray", label="Remaining")
        ax.set_ylabel("Amount (₹)")
        ax.set_title("Goal Completion Progress")
        ax.legend()
        return fig
    return None


def investment_vs_goal_pie():
    summary = tracker.view_summary()
    balance = summary["Balance"]
    goal_amount = savings.get_goal()

    if goal_amount:
        achieved = min(balance, goal_amount)
        remaining = max(goal_amount - balance, 0)
        fig, ax = plt.subplots()
        ax.pie(
            [achieved, remaining],
            labels=["Saved", "Remaining"],
            autopct='%1.1f%%',
            colors=["blue", "lightgray"],
            startangle=90
        )
        ax.set_title("Investment vs Goal Completion")
        return fig
    return None


# ==========================
# Visualization Selector
# ==========================
def visualize_data(section, chart_type):
    if section == "Salary & Expense":
        if chart_type == "Bar Chart":
            return bar_chart_expense()
        elif chart_type == "Pie Chart":
            return pie_chart_expense()
        elif chart_type == "Line Chart":
            return line_chart_expense_over_time()
        elif chart_type == "Stacked Bar Chart":
            return stacked_bar_chart_income_expense()
        elif chart_type == "Histogram":
            return histogram_expense_distribution()

    elif section == "Investment & Goal":
        if chart_type == "Goal Progress Bar":
            return goal_progress_chart()
        elif chart_type == "Goal Completion Pie":
            return investment_vs_goal_pie()

    return None