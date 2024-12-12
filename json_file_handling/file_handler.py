import json;

# specify the path to JSON file
json_file_path = "json_file_handling/example_1.json"

# open the JSON file for reading
with open(json_file_path,"r")as json_file:
    # load the json data into a python dictionary
    content = json.load(json_file)
    
# contains the content of the JSON file print as the dictionary
print(content)

for key,value in content.items():
    print(key,value)
