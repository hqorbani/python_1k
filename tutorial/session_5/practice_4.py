### Write a program to calculate an age in years and print it on result.
### Also if age is between 13 and 19 print a message that the user is a teenager.
### 13 <= age <= 19
#
#####  If you have any questios, please email me or leave message on Telegram.

birth_year = int(input("please enter your birth year: "))
age = 2024 - birth_year
print("your age is", age)
if 13 <= age <= 19:
    print("you are a teenager")