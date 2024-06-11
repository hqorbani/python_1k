persons = {
    "person_1":{
        "name": "Ali",
        "family": "Alavi",
        "age": 25
    },
    "person_2":{
        "name": "Mehrdad",
        "family": "Farahani",
        "age": 31
    }
}

for key , value in persons.items():
    # print(key)
    for k , v in value.items():
        print(k , v)