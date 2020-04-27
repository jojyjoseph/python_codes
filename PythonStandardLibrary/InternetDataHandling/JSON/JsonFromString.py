'''
JavaScript Object Notation
'''

import json

# reading JSON from String

print("##############")
print("Reading JSON from String\n")

#JSON file writen in a multiline string
people_string = '''
{
    "people" : [
    {
        "name" : "John Smith",
        "phone": "615-555-7164",
        "emails": ["johnsmith@bogusemail.com","john.smith@work-place.com"],
        "has_license" : false
    },
    {
        "name" : "Jane Doe",
        "phone" : "560-555-5153",
        "emails": null,
        "has_license":true
    }
    ]
}
'''

#read the string to data
data = json.loads(people_string)
print("type of the JSON object is ", type(data))
print("\nprinting JSON\n",data)

print("type of data[\"people\"] is ", type(data["people"]))
print("\nlooping through both person")
for person in data['people']:
    #prints the name of the person
    print(person['name'])
    #delete the phone number from JSON object
    del person['phone']

print("\nDump the updated JSON object to a string with a better format  and sorting (optional)")
new_string = json.dumps(data, indent=2, sort_keys=True)
print(new_string)



#different JSON elements are mapped to different container in Python
print("\nDifferent JSON elements are converted to python containers\nobject -- dict\narray -- list\nstring -- str\nnumber(int) -- int\nnumber(real) -- float\ntrue -- True\nfalse -- False\nnull -- None")






