# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

from My_Goog_Pack import goog_funcs as goog
lol=goog.get_goog_data()
topics=lol[0]
entries=lol[1:]
username="Smalley"
user_entry=goog.find_user(username,lol)
colors = {
    'background': '#111111',
    'text': '#111111'
}

if user_entry: #if user entry exists
    user_dict=goog.convert_to_dict(user_entry,topics)
else:
    user_dict={}


print("topics 1 " + topics[1] )
print("topics 2 " + topics[2] )
print("topics 3 " + topics[3] )
print("topics 4 " + topics[4] )
print("topics 5 " + topics[5] )
print("topics 6 " + topics[6] )
print("topics 7 " + topics[7] )
print("topics 8 " + topics[8] )
print("topics 9 " + topics[9] )
print("topics 10 " + topics[10] )
print("topics 11 " + topics[11] )
print("topics 12 " + topics[12] )

 


def generate_sliders():
    component_list=[]
    component_list.append(html.H1(
        children='EHL Quest Dashboard', 
        style={
            'textAlign': 'center',
            'color': colors['text']
        })) 
        
    for entry in entries:
        
        name=entry[1]
        quest=entry[2]
        start=entry[3]
        total_hrs=entry[4]
        mile_1=entry[5]
        mile_1_hr=entry[6]
        mile_2=entry[7]
        mile_2_hr=entry[9]
        mile_3=entry[10]
        mile_3_hr=entry[11]
        end=entry[8]

 

        component_list.append(html.Div(html.P("NAME: "+name)))
        component_list.append(html.Div(html.P("QUEST: "+quest)))
       
        comp = dcc.Slider(
            min=0,
            max=10,
            marks={0:start,3:mile_1,5:mile_2, 7:mile_3,10:end},
            value=4,
            )
        component_list.append(comp)
        
    return component_list

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children = generate_sliders())

if __name__ == '__main__':
    app.run_server(debug=True)