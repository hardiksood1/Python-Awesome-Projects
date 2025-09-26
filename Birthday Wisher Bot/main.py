import smtplib
from datetime import datetime as dt
import random
import pandas as pd
from email.mime.text import MIMEText
from email.header import Header

# =============================
# CONFIG
# =============================
MY_EMAIL = "Your email ID"
MY_PASSWORD = "gmail app password"   # <-- 16-digit Gmail App Password
CSV_FILE = "birthday.csv"
TEMPLATE_PATH = "./letter_{}.txt"   # Example: letter_1.txt, letter_2.txt, letter_3.txt


# =============================
# FUNCTIONS
# =============================

def load_birthdays(file_path):
    """Load birthday data from CSV into a DataFrame."""
    return pd.read_csv(file_path)


def get_today():
    """Return today's month-day string."""
    date = dt.now()
    return f"{date.month}-{date.day}"


def pick_random_template(name):
    """Pick a random template and replace [NAME] with actual name."""
    template_num = random.randint(1, 3)
    with open(TEMPLATE_PATH.format(template_num), "r") as wish_file:
        contents = wish_file.read()
    return contents.replace("[NAME]", name)


def send_email(to_email, subject, message):
    """Send an email using Gmail SMTP with UTF-8 encoding."""
    msg = MIMEText(message, "plain", "utf-8")
    msg["From"] = MY_EMAIL
    msg["To"] = to_email
    msg["Subject"] = Header(subject, "utf-8")

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(MY_EMAIL, to_email, msg.as_string())


def wish_birthdays():
    """Main function: checks birthdays and sends wishes."""
    data = load_birthdays(CSV_FILE)
    today = get_today()

    for _, row in data.iterrows():
        birth_day = f"{row['month']}-{row['day']}"
        if today == birth_day:
            message = pick_random_template(row["name"])
            send_email(row["email"], "Happy Birthday 🎉", message)
            print(f"✅ Sent birthday wish to {row['name']} at {row['email']}")


# =============================
# RUN
# =============================
if __name__ == "__main__":
    wish_birthdays()
