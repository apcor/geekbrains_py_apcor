import pickle, json

with open('group.pickle', 'rb') as f:
    read_pickle = pickle.load(f)

print(read_pickle)
print(type(read_pickle))

with open('group.json', 'r', encoding= 'utf-8') as f:
    read_json = json.load(f)

print(read_json)
print(type(read_json))