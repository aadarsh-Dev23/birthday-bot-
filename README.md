
---

# Birthday Wish with WhatsApp Integration

This project is a Python-based Birthday Reminder system that automatically sends WhatsApp messages to remind users of birthdays on the current day. It uses `pywhatkit` for WhatsApp message automation and `pandas` for data manipulation.

## Features

- **Automatic Birthday Detection:** Reads a CSV file containing user data and detects if any birthdays fall on the current day.
- **WhatsApp Message Automation:** Sends personalized birthday messages via WhatsApp to users whose birthdays are today.
- **Easy CSV Integration:** Load user data including names, birthdays, and phone numbers from a CSV file.

## Technologies Used

- **Python:** The core programming language used for the project.
- **pandas:** For handling and manipulating the CSV data.
- **pywhatkit:** To send WhatsApp messages automatically.
- **datetime:** For working with dates to compare the current date with the birthdays.

## How It Works

1. **Load User Data:** The script reads a CSV file (`data.csv`) containing user details. The CSV should have columns for `Name`, `Birthday`, and `Phone`.
2. **Date Comparison:** The script extracts the month and day from the `Birthday` column and compares it with the current date.
3. **Send WhatsApp Messages:** If there are users with birthdays today, it sends a personalized WhatsApp message to each of them using the phone numbers provided in the CSV.

## Prerequisites

- Python 3.x
- pandas
- pywhatkit

## Usage

1. **Prepare your CSV file:** Ensure your CSV file (`data.csv`) has columns named `Name`, `Birthday`, and `Phone`.
2. **Install dependencies:** Install the required Python packages using pip:
   ```bash
   pip install pandas pywhatkit
   ```
3. **Run the script:** Execute the Python script to send birthday reminders:
   ```bash
   python birthday_reminder.py
   ```

## Example CSV File

```csv
Name,Birthday,Phone
John Doe,1990-06-28,1234567890
Jane Smith,1985-04-15,0987654321
```

In this example, if today's date is June 28th, a WhatsApp message will be sent to John Doe.

## Notes

- Ensure that you have WhatsApp installed and logged in on your computer, as `pywhatkit` uses the web interface to send messages.
- Adjust the `sendwhatmsg` function parameters as needed for timing and other preferences.

---

