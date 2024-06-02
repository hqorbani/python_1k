name = input("Enter your name please: ")
marital_status = input("Enter your marital status (married/unmarried): ").lower()
level_education = input("please enter level of your education(BA/MA/PHD): ").upper()
age = int(input("please enter your age:"))
if marital_status in ["married","unmarried"]:
    if level_education in  ["BA","MA","PHD"]:
        # empty dic
        person = {}
        person['first_name'] = name
        person['marital_status'] = marital_status
        person['level_education'] = level_education
        person['age'] = age
        # print(person)

        for s , p in person.items():
            print(s ,"--->" , p)
    else:
        print("Error: education")
else:
    print("error for marital status")