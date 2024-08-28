import json

def read_json_file(file_name):
    f = open(file_name)
    data = json.load(f)
    return data

def write_json_file(file_name, data):
    # Serializing json
    json_object = json.dumps(data, indent=4)
    # Writing to sample.json
    with open(file_name, "w") as outfile:
        outfile.write(json_object)


