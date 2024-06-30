name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

def introduce(full_name,age):
    print(f"Hello, {full_name}!")
    print(f"Your are {age} years old")

introduce("Hamzeh Qorbani" , 39)
print("---------------")
introduce(name , age)

