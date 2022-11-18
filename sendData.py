import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json


from oauth2client.service_account import ServiceAccountCredentials
import gspread
import json
scopes = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]
credentials = ServiceAccountCredentials.from_json_keyfile_name("E:/telegramBot/valiteach/handlers/users/python-get-data-367016-6f7fbfe5253a.json", scopes) #access the json key you downloaded earlier
file = gspread.authorize(credentials) # authenticate the JSON key with gspread
file = file.open('pydata')
ws = file.worksheet('myWorksheet')
ws.update_acell('B1', 'Gspread !')
# sheet = file.open("pydata")  #open sheet
# all_cells = sheet.range('A1:C6')
# print(all_cells)
# sheet = sheet.sheet_name  #replace sheet_name with the name that corresponds to yours, e.g, it can be sheet1
# sheet.update_cell('B2','al')
# sheet.update_cell( 'Blue') #updates row 2 on column 3