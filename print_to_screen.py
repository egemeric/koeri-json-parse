#!/usr/bin/env python3
import requests
import json
import parse

liste_big=[]
def get_by_key_to_list(data,key):
    wanted_values=[]
    for i in data:
        wanted_values.append(i.get(key))
    return wanted_values


def sort_magnitude(data):
    sorted_list= sorted(data, key=lambda k: k['magnitude'])
    return sorted_list

def print_touser(data,setting):
    data.reverse()
    for i in data:
        if float(i.get("magnitude")) > 3.5 :
            print(i.get("magnitude"),i.get("location"),i.get("time"),sep="---")
            liste_big.append(i)
        elif setting=="all":
            print(i.get("magnitude"), i.get("location"), i.get("time"), sep="---")
        else:
            pass

def create_list(data_json):
    list_quakes=[]
    global gb_liste
    for i in range(0,len(data_json["result"])):
        list_quakes.append(data_json["result"][i])
    gb_liste=list_quakes
    return list_quakes
def get_json(data):
    dat_json=json.loads(data)
    return dat_json
def get_quakes():
    #URL="http://10.1.1.15/quake.html"
    #raw=requests.get(URL)
    #data=raw.content
   # return data
    res=parse.main()
    return res




ana_list=create_list(get_json(get_quakes()))
sorted_list=sort_magnitude(ana_list)
print("Earthquakes with magnetude bigger than 3.5:")
print_touser(sorted_list,"")

