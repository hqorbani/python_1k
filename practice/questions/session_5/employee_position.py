#### Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.
### if employee is female, then she will work only in urban areas.

### if employee is a male and age is in between 20 to 40 then he may work in anywhere

### if employee is male and age is in between 40 to 60 then he will work in urban areas only.

### And any other input of age should print "ERROR".
age = int(input("please enter user age: "))
sex = input("please enter user sex:(male/female) ")
marital_status = input("please enter user marital status:(single/married/devorced) ")
print("user properties:")
print("age:", age)
print("sex:", sex)
print("marital status:", marital_status)
if sex == "female":
    print('she will work only in urban areas')
elif sex == "male" and 20 <= age <= 40:
    print("he may work in anywhere")
elif sex == "male" and (age >= 20 and age <= 40):
    print("he will work in urban areas only")
else:
    print("ERROR")






