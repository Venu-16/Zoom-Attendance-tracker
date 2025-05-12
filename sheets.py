import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv
from os import environ as env

load_dotenv()
env['SHELL']

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)


def updateAttendence(email, present=True, ts='0', topic='', sheetName='AttPy'):
    sheet = client.open(sheetName).sheet1
    data = sheet.get_all_records()

    print(email)
    print(present, ts)

    for i, row in enumerate(data):
        if row['Email'] == email:
            if present:
                sheet.update_cell(i + 2, 3, 'P')
                sheet.update_cell(i + 2, 4, ts)
            else:
                sheet.update_cell(i + 2, 5, ts)
            sheet.update_cell(i + 2, 6, topic)

# updateAttendence('harsh')