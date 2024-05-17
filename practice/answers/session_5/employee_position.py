age = int(input("Please enter user's age: "))
sex = input("Enter user's sex (male/female): ").lower()
marital_status = input("Enter marital status (single/married/divorced): ").lower()

if sex == "male":
    print('He will have to work halftime.')
elif sex == "female":
    print('She will have to work full-time.')

if 18 <= age <= 65:
    if marital_status == "single":
        print('He will have to work on weekends only.')
    elif marital_status == "married" or marital_status == "divorced":
        print('He will work at weekends only')
    else:
        print('Error: Invalid marital status.')