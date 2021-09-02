
from googleapiclient.discovery import build
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

SAMPLE_SPREADSHEET_ID = '1KrPYhcIIbYVahqybpoiE4j6nl1vQQ-py5KgeXbmufYQ'
service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="ok!A1:B4").execute()

values = result.get('values', [])
request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='ok!A1', valueInputOption='USER_ENTERED', body={'values':result_data}).execute()
print(values)