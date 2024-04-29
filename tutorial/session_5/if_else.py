#if elif and else:
a = 33
b = 100
if a < b and a > 10:
    print("a is smaller than b")
    print("finished")
elif 10 < a < 20:
    print("a is greater than b")
elif a == 30 or a == 50:
    print("a equal 30 or 50")
elif not a < 10:
    print("a is not smaller than 10")
else:
    print("your data are False")

print("finished")



