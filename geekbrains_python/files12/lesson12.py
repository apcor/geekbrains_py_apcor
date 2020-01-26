import json

friends = [
    {'name': 'Max', 'age': 23, 'phones': [123, 234]},
    {'name': "Leo", 'age': 33}
]

with open('friends.json', 'w') as f:
    json_friends = json.dump(friends, f)

with open('friends.json', 'r') as f:
    friends = json.load(f)

print(friends)
print(type(friends))


# print(type(friends))
# json_friends = json.dumps(friends)
# print(json_friends)
# print(type(json_friends))
#
# friends = json.loads(json_friends)
# print(friends)