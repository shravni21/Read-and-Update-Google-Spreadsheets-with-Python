from googleapiclient.discovery import build
from google.oauth2 import service_account


SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']


creds = None
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)


# The ID of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1Xnig-X0YzFP0HGiwLYIvQ0koYNb_50dt85Bwcb5xLCk'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="placement!A1:E192").execute()
values = result.get('values', [])

array = [["12/12/2021", 5000], ["24/5/2017", 10000], ["10/1/2022", 3000]]
request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range="Sheet2!B2", valueInputOption="USER_ENTERED", body={"values": array}).execute()


print(request)
