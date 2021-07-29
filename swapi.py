import requests
import pandas as pd

uri = 'https://swapi.dev/api/people/'

def fetch_num_people ():
    r = requests.get(uri)
    if r.status_code == 200:
        data = r.json()
        count = data["count"]
        return count
    else:
        return "NO DATA"


def fetch_all_people():
    datalist=[]
    for i in range (1, fetch_num_people()+2):
        url = f'{uri}{str(i)}'
        r_people = requests.get(url)
        if r_people.status_code == 200:
            data_people = r_people.json()
            datalist.append(data_people)
    return datalist


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