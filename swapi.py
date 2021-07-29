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
    
#df_planets