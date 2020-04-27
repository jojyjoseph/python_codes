'''
JavaScript Object Notation
'''

import json

# reading JSON from File 

print("##############")
print("Reading JSON from file\n")

with open('states.json') as f:
    data=json.load(f)

for state in data['states']:
    print(state['name'], state['abbreviation'])

print("\nRemoving the area code - modifying the JSON object and writing to a file")

for state in data['states']:
    del state['area_codes']

with open('new_states.json','w') as f:
    json.dump(data, f , indent =2)





