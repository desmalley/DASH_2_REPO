import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = [ 'https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('sdnd-apr-2020-eaa3f3bf8046.json',scope)

gc = gspread.authorize(credentials)

#****

def get_goog_data():
    wks= gc.open('test').sheet1
    #pprint(wks.get_all_records())
    lol=[]
    for row in range(len(wks.get_all_records())):
        #print(wks.row_values(row+1))
        lol.append(wks.row_values(row+1))
    return lol
#wks.append_row(["into first col","into second col"])

