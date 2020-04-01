from My_Goog_Pack import goog_funcs as goog
lol=goog.get_goog_data()
topics=lol[0]

username="Smalley"
user_entry=goog.find_user(username,lol)



if user_entry: #if user entry exists
    user_dict=goog.convert_to_dict(user_entry,topics)
else:
    user_dict={}

print(username + " Dictionary:")

print(user_dict)