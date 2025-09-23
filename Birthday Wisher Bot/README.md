#  Birthday Wisher Bot

A simple Python automation script that checks birthdays from a list and automatically sends personalized wishes via **Email** or **WhatsApp**.
---

## 🚀 Features
- Store names, birthdates, and contact details in a CSV/Excel file.
- Automatically check daily if it’s someone’s birthday.
- Send personalized greetings through:
  - 📧 Email (using `smtplib`)
  - 💬 WhatsApp (using `pywhatkit`)
- Schedule reminders for upcoming birthdays.
- Easy to customize and expand.

---

## 📂 Project Structure

```
Birthday-Wisher-Bot/
│── birthdays.csv          # Stores names, birthdates, and contacts
│── main.py                # Main script to run the bot
│── email_sender.py        # Handles sending emails
│── whatsapp_sender.py     # Handles sending WhatsApp messages
│── README.md              # Project documentation
```

---

## 🛠️ Technologies Used
- **Python**
- **pandas** → to manage birthdays list
- **smtplib** → to send emails
- **pywhatkit** → to send WhatsApp messages
- **datetime** → to check today’s date

---

## 📋 Requirements

Install dependencies with:
```bash
pip install pandas pywhatkit
```

For email sending, you also need an **App Password** if using Gmail (for accounts with 2FA enabled).

---

## ⚡ How to Use

1. Clone the project or copy the files.
2. Create a `birthdays.csv` file with the following format:

```csv
Name,Date,Email,Phone
John Doe,1995-09-23,john@example.com,+911234567890
Jane Smith,2000-01-15,jane@example.com,+919876543210
```

3. Update your **email credentials** inside `email_sender.py`. Example:

```python
EMAIL = "your_email@gmail.com"
PASSWORD = "your_app_password"
```

4. Run the script daily (manually or via Task Scheduler / cron):
```bash
python main.py
```

5. If today matches a birthday in the file → 🎉 wishes will be sent automatically!

---

## 🎯 Example Output

```
[2025-09-23 08:00] 🎉 It's John Doe's Birthday!
📧 Email sent successfully to john@example.com
💬 WhatsApp message scheduled for +911234567890
```

---

## 🔮 Future Improvements
- Add Telegram bot integration for headless servers.
- Schedule birthday reminders a day before.
- Integrate with Google Calendar for automatic sync.

---

## 👨‍💻 Author
Developed by **Hardik Sood** 🚀
