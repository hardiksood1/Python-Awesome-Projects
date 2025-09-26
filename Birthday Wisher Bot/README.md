#  Birthday Wisher Bot

A simple Python automation script that checks birthdays from a list and automatically sends personalized wishes via **Email** or future work(**WhatsApp**).

---

##  Features
- Store names, birthdates, and contact details in a CSV/Excel file.
- Automatically check daily if it’s someone’s birthday.
- Send personalized greetings through:
  - 📧 Email (using `smtplib`)
- Schedule reminders for upcoming birthdays.
- Easy to customize and expand.

---

##  Project Structure

```
Birthday-Wisher-Bot/
│── birthdays.csv          # Stores names, birthdates, and contacts
│── main.py                # Main script to run the bot
│── email_sender.py        # Handles sending emails
│── README.md              # Project documentation
```

---

## 🛠️Technologies Used
- **Python**
- **pandas** → to manage birthdays list
- **smtplib** → to send emails
- **datetime** → to check today’s date

---

##  Future Improvements
- Add Telegram bot integration for headless servers.
- Schedule birthday reminders a day before.
- Integrate with Google Calendar for automatic sync.

---
