register_number = int(input("How many people are going to register: "))
persons = {}
for item in range(register_number):
    name = input("Enter your name please: ")
    marital_status = input("Enter your marital status (married/unmarried): ").lower()
    level_education = input("please enter level of your education(BA/MA/PHD): ").upper()
    age = int(input("please enter your age:"))
    person = {}
    person['first_name'] = name
    person['marital_status'] = marital_status
    person['level_education'] = level_education
    person['age'] = age

    persons['person_' + str(item + 1)] = person

print(persons)