import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv
import os

# Load environment variables from .env (even if empty)
load_dotenv()

# Remove this line - it crashes on Windows:
# env['SHELL']

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)

def updateAttendence(email, present=True, ts='0', topic='', sheetName='AttPy'):
    sheet = client.open(sheetName).sheet1
    data = sheet.get_all_records()

    print(f"Updating attendance for: {email}")
    print(f"Present: {present}, Timestamp: {ts}, Topic: {topic}")

    for i, row in enumerate(data):
        if row.get('Email', '').lower() == email.lower():
            if present:
                sheet.update_cell(i + 2, 3, 'P')       # Status column (C)
                sheet.update_cell(i + 2, 4, ts)        # Join Time (D)
            else:
                sheet.update_cell(i + 2, 5, ts)        # Leave Time (E)
            sheet.update_cell(i + 2, 6, topic)         # Topic (F)
            print(f"Row {i + 2} updated.")
            break
    else:
        print(f"No matching email found for {email}")
