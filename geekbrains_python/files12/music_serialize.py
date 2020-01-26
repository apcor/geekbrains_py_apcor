import pickle, json

favourite_group = {
    'name': 'Felipe Cordeiro',
    'tracks': ['Legal e ilegal', 'Onde é que eu vou parar', 'Sou você'],
    'albums': [{'name': 'Kitsch Pop Cult', 'year': 2011},
               {'name': 'Transpyra', 'year': 2019}]
}

fav_group_pickle = pickle.dumps(favourite_group)

fav_group_json = json.dumps(favourite_group)

print(fav_group_pickle)
print(fav_group_json)

with open('group.pickle', 'wb') as f:
    f.write(fav_group_pickle)

with open('group.json', 'w', encoding ='utf-8') as f:
    f.write(fav_group_json)
