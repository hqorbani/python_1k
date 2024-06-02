name = input("Enter your name please: ")
marital_status = input("Enter your marital status (married/unmarried): ").lower()
level_education = input("please enter level of your education(BA/MA/PHD): ").upper()
age = int(input("please enter your age:"))
person = {}
person['first_name'] = name
person['marital_status'] = marital_status
person['level_education'] = level_education
person['age'] = age

# nested dictionary:
persons = {}

persons['person_1'] = person

print(persons)

print(persons['person_1'])