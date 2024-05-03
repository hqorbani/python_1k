gender_list = ['male' ,'female','other']
gender = input("please enter user gender(male/gender): ")
if gender in gender_list:
    print(gender)
    birth_year = int(input("please enter birth year:"))
    
else:
    print('your data is false')