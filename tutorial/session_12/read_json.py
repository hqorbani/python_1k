import json


# Open the JSON file
with open('files/json/properties.json') as file:
    data = json.load(file)

# Now 'data' contains the parsed JSON data
print(data)
print(type(data))

for item in data:
    print(item)
print("hello Melody")