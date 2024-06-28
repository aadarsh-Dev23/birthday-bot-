import pywhatkit
import pandas as pd
from datetime import datetime

# Load the CSV file into a DataFrame
df = pd.read_csv('data.csv')

today = datetime.today().strftime("%m-%d")

# Extract month and day from the 'Birthday' column for comparison
df['Birthday_MD'] = pd.to_datetime(df['Birthday']).dt.strftime("%m-%d")

today_birthday = df[df['Birthday_MD'] == today]

# Print the name(s) of the user(s) with today's birthday
if not today_birthday.empty:
    for name in today_birthday['Name']:
        pywhatkit.sendwhatmsg(f"+91 {today_birthday['Phone']}",f"Today is {name}'s birthday!",20,31)
else:
    print("No one has a birthday today.")
