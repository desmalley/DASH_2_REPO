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

group={"caitlin":["Caitlin Bingham","Caitlin"],
       "daniel":["Daniel Smalley","Daniel", "Dr. Smalley"],
       "dylan":["Dylan","Dylan Barton"],
       "mitch":["Mitchell","Mitchell Adams", "Mitch"],
       "steve":["Stephen","Stephen Griffith","Steve"],
       "manusha":["Manusha","Manusha Korimi"],
       "kyle":["Kyle","Kyle Schvaneveldt"],
       "keaton":["Keaton Shurilla","Keaton"],
       "elias":["Elias", "Elias Guanuna"],
       "ximena":["Ximena", "Ximena Briceno"],
       "josh":["Josh","Josh Laney"],
       "wes":["Wes","Wesley", "Wes Rodgers", "Wesley Rogers"]
       }


    

def find_images(username_entry):
    heroes=[]
    for handle,nicknames in group.items():
        for elem in username_entry.split():
            if elem in nicknames:
                heroes.append(handle)
    if not heroes:
        heroes.append("missing")
    image_objects=[]
    for hero in heroes:
        image_objects.append(html.Img(src=app.get_asset_url(hero + '.png')))
   
    return image_objects[0]





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
        print(name)
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

        #image
      
        component_list.append(find_images(name))
        print(component_list)
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