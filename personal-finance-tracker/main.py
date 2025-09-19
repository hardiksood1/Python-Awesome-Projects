import streamlit as st
import tracker
import savings
import visualization
import database

def main():
    st.set_page_config(page_title="Personal Finance Tracker", layout="centered")
    st.title("💰 Personal Finance Tracker")

    menu = [
        "Add Income",
        "Add Expense",
        "View Summary",
        "Set Savings Goal",
        "Visualize Spending",
        "Exit"
    ]
    choice = st.sidebar.radio("📌 Menu", menu)

    # ==============================
    # Add Income
    # ==============================
    if choice == "Add Income":
        st.subheader("➕ Add Income")
        amount = st.number_input("Enter income amount (₹)", min_value=0.0, format="%.2f")
        source = st.text_input("Source (e.g., Salary, Freelancing)")
        if st.button("Save Income"):
            if amount > 0 and source:
                tracker.add_income(amount, source)
                st.success(f"Income of ₹{amount:.2f} added from {source}")
            else:
                st.warning("Please enter valid income and source.")

    # ==============================
    # Add Expense
    # ==============================
    elif choice == "Add Expense":
        st.subheader("➖ Add Expense")
        amount = st.number_input("Enter expense amount (₹)", min_value=0.0, format="%.2f")
        category = st.text_input("Category (e.g., Food, Rent, Travel)")
        if st.button("Save Expense"):
            if amount > 0 and category:
                tracker.add_expense(amount, category)
                st.success(f"Expense of ₹{amount:.2f} added under {category}")
            else:
                st.warning("Please enter valid expense and category.")

    # ==============================
    # View Summary
    # ==============================
    elif choice == "View Summary":
        st.subheader("📊 Financial Summary")
        summary = tracker.view_summary()
        st.write(summary)

    # ==============================
    # Smart Savings Planner
    # ==============================
    elif choice == "Set Savings Goal":
        st.subheader("🎯 Smart Savings Planner")

        goal = st.number_input("Enter your savings goal (₹)", min_value=0.0, format="%.2f")
        if st.button("Set Goal"):
            if goal > 0:
                savings.set_goal(goal)
                st.success(f"Savings goal of ₹{goal:.2f} set!")
            else:
                st.warning("Please enter a valid goal.")

        # Current financials
        current_summary = tracker.view_summary()
        balance = current_summary["Balance"]
        goal_amount = savings.get_goal()

        if goal_amount:
            st.info(f"Your current goal: ₹{goal_amount:.2f}")
            st.write(savings.track_savings_progress(balance))

            # Suggested fixed plans
            st.subheader("📊 Suggested Monthly Saving Plans")
            plans = savings.suggest_plans(goal_amount, balance)
            if "plans" in plans and plans["plans"]:
                for p in plans["plans"]:
                    st.write(f"💰 Save ₹{p['monthly']} / month → Reach in {p['months']} months")

            # Custom plan (like EMI system)
            st.subheader("📝 Calculate Custom Plan")
            months = st.number_input("Enter number of months you want to achieve this goal in", min_value=1, step=1)
            if st.button("Calculate Monthly Saving"):
                monthly_required = savings.calculate_monthly_for_months(goal_amount, months, balance)
                if monthly_required:
                    st.success(
                        f"To reach your goal of ₹{goal_amount:.2f} in {months} months, "
                        f"you need to save ₹{monthly_required:.2f} per month."
                    )

    # ==============================
    # Visualization
    # ==============================
    elif choice == "Visualize Spending":
        st.subheader("📈 Visualization Options")

        section = st.radio("Choose visualization type", ["Salary & Expense", "Investment & Goal"])

        if section == "Salary & Expense":
            chart_type = st.selectbox(
                "Select a chart",
                ["Bar Chart", "Pie Chart", "Line Chart", "Stacked Bar Chart", "Histogram"]
            )
        else:
            chart_type = st.selectbox(
                "Select a chart",
                ["Goal Progress Bar", "Goal Completion Pie"]
            )

        fig = visualization.visualize_data(section, chart_type)
        if fig:
            st.pyplot(fig)
        else:
            st.warning("No data available for visualization.")

    # ==============================
    # Exit
    # ==============================
    elif choice == "Exit":
        st.info("Exiting... (Just close the browser tab 🙂)")


if __name__ == "__main__":
    database.initialize_database()
    main()