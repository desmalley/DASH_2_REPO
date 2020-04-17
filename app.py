# -*- coding: utf-8 -*-
#LIBRARIES
import dash
import dash_core_components as dcc
import dash_html_components as html
import datetime
from My_Goog_Pack import goog_funcs as goog


#GLOBALS
lol=goog.get_goog_data()
topics=lol[0]
entries=lol[1:]
max_label_length=30 #max length of slider labels
colors = {
    'background': '#111111',
    'text': '#111111'
}
group={"caitlin":["Caitlin Bingham","Caitlin"],
       "daniel":["Daniel Smalley","Daniel", "Dr. Smalley","Smalley"],
       "dylan":["Dylan","Dylan Barton"],
       "mitch":["Mitchell","Mitchell Adams", "Mitch"],
       "steve":["Stephen","Stephen Griffith","Steve"],
       "manusha":["Manusha","Manusha Korimi"],
       "kyle":["Kyle","Kyle Schvaneveldt"],
       "keaton":["Keaton Shurilla","Keaton"],
       "elias":["Elias", "Elias Guanuna"],
       "ximena":["Ximena", "Ximena Briceno"],
       "josh":["Josh","Josh Laney"],
       "wes":["Wes","Wesley", "Wes Rodgers", "Wesley Rogers"],
       "luke":[ "Luke", "Luke Johnson"]
       }
today=datetime.datetime.now()

#LOCAL FUNCTIONS
#1 pointer group**********************************

def pointer_calc(start, end):
#Usage:
    if  start and end:
        start_list=start.split("/")
        start_list_rearranged=[start_list[2],start_list[0],start_list[1]]
        start_reformatted=datetime.datetime(int(start_list_rearranged[0]),int(start_list_rearranged[1]),int(start_list_rearranged[2]))
      
        end_list=end.split("/")
        end_list_rearranged=[end_list[2],end_list[0],end_list[1]]
        end_reformatted=datetime.datetime(int(end_list_rearranged[0]),int(end_list_rearranged[1]),int(end_list_rearranged[2]))
        td_duration=end_reformatted-start_reformatted
        
        td_runway=end_reformatted-today
        
        duration=td_duration.days
        
        runway=td_runway.days
        
        pointer=int(10-(runway/duration)*10)
        return pointer
    else:
        return 10 #make it look like they're done


#***********************************

#2 dash group**********************************  
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
        component_list.append(find_images(name))
        component_list.append(html.Div(html.P("NAME: "+name)))
        component_list.append(html.Div(html.P("QUEST: "+quest)))
        if len(mile_1)+len(mile_2)+len(mile_3) > 3*max_label_length:
            component_list.append(html.Div(html.P("milestone 1: {}".format(mile_1))))         
            component_list.append(html.Div(html.P("milestone 2: {}".format(mile_2))))         
            component_list.append(html.Div(html.P("milestone 3: {}".format(mile_3))))         
            mile_1="milestone 1"
            mile_2="milestone 2"
            mile_3="milestone 3"      
        comp = dcc.Slider(
            min=0,
            max=10,
            marks={0:start,3:mile_1,5:mile_2, 7:mile_3,10:end},
            value=pointer_calc(start,end),
            )
        component_list.append(comp)
        
    return component_list
# dash group**********************************   
    
    
        

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children = generate_sliders())

if __name__ == '__main__':
    app.run_server(debug=True)