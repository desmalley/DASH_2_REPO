import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint


json_key='dnd-apr-2020-eaa3f3bf8046.json'
file_name='dnd (Responses)'
username_col= 1#username column index in sheet (python style starting at 0)

scope = [ 'https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_key,scope)
gc = gspread.authorize(credentials)


#****
def get_goog_data():
    wks= gc.open(file_name).sheet1 #gives first sheet of this file
    #pprint(wks.get_all_records())
    lol=[]
    for row in range(len(wks.get_all_records())):
        #print(wks.row_values(row+1))
        lol.append(wks.row_values(row+1))
    return lol
#wks.append_row(["into first col","into second col"])

def find_user(username,list_of_lists):
        user_list=[]
        for elem in list_of_lists:
            if username in elem[username_col]:     
#                if username == elem[username_col]: #strict
                user_list=elem
        return user_list
        
def make_same_len(topic_list,user_list):
    for entry in range(len(topic_list)-len(user_list)):
        user_list.append("not included")
    return user_list        

def convert_to_dict(my_list_short, keys):
        my_dict={}
        my_list=make_same_len(keys, my_list_short)
        for index in range(len(keys)):
                my_dict.update({keys[index]:my_list[index]})
        return my_dict