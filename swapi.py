import json
import pandas as pd
import requests
import numpy as np

#PEOPLE

uri = 'https://swapi.dev/api/people/'

def fetch_num_people ():
    r = requests.get(uri)
    if r.status_code == 200:
        data = r.json()
        count = data["count"]
        return count
    else:
        return "NO DATA"
      
      people
def people_dframe():
    columns = ["name","height","birth_year","gender","homeworld","films", "vehicles","starships"]
    swapi_df= pd.DataFrame(columns=columns)
    for index, row in enumerate(fetch_all_people()):
        swapi_df.loc[index,'name']=row['name']
        swapi_df.loc[index,'height']=row['height']
        swapi_df.loc[index,'birth_year']=row['birth_year']
        swapi_df.loc[index,'gender']=row['gender']
        swapi_df.loc[index,'homeworld']=row['homeworld']
        swapi_df.loc[index,'films']=row['films']
        swapi_df.loc[index,'vehicles']=row['vehicles']
        swapi_df.loc[index,'starships']=row['starships']
    return swapi_df

#print(people_dframe())

#STARSHIP 

def fetch_starship(n_page):
    uri = 'https://swapi.dev/api/starships'
    url = uri
    if n_page > 1:
        url = f'{uri}/?page={str(n_page)}'
    
    url
    
    url = f'https://swapi.dev/api/starships'
    if n_page > 0:
        url = f'{uri}/?page={str(n_page)}'
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        results_list = data['results']
        return results_list
    else:
        return None

def create_starship_dataframe():
    columns = ['name','model','manufacturer','crew','passengers','starship_class']
    starship_df = pd.DataFrame(columns=columns)
    starship_list = fetch_starship(4)
    starship_list
    for index, row in enumerate(starship_list):
        starship_df.loc[index,'name'] = row['name']
        starship_df.loc[index,'model'] = row['model']
        starship_df.loc[index,'manufacturer'] = row['manufacturer']
        starship_df.loc[index,'crew'] = row['crew']
        starship_df.loc[index,'passengers'] = row['passengers']
        starship_df.loc[index,'starship_class'] = row['starship_class']
    return starship_df

def fetch_all_people():
    datalist=[]
    for i in range (1, fetch_num_people()+2):
        url = f'{uri}{str(i)}'
        r_people = requests.get(url)
        if r_people.status_code == 200:
            data_people = r_people.json()
            datalist.append(data_people)
    return datalist

#PLANETS

def fetch_planets(n_planets):
    url = 'https://swapi.dev/api/planets/'
    if n_planets > 0:
        url = f'{url}/{str(n_planets)}'
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        return data
    else:
        return None
    
for index, row in enumerate(list_planets):
    df_planets.loc[index,'name'] = row['name']
    df_planets.loc[index,'climate'] = row['climate']
    df_planets.loc[index,'terrain'] = row['terrain']
    df_planets.loc[index,'population'] = row['population']
    
df_planets
