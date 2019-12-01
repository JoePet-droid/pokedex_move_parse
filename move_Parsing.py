import json

with open('moves.json') as moves:
    data = json.load(moves)

for name in data:
    del name['category']
    del name['cname']
    del name['jname']
    if name['accuracy'] == None:
        del name['accuracy']
    if name['power'] == None:
        del name['power']

    with open('moves_updated.json', 'a') as p:
        json.dump(name, p, indent=2)

    # print(name)

