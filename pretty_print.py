# how to print and format prinitng

a = "2"

# type is sensative so if you have a int, translate to str(). Easy to use can also be + instead of ,
print(a, "is a number")

# contrains type with %s to be string
print("%s is also a number" % (a))

# replaces all the {} with format in order e.g. {}{}{}.format(a,b,c)
print("{} is still a number".format(a))

# easiest and cleanest way to print variable
print(f"And i think {a} is still a number")


star = "*"

for i in range(10):
    print(star*i)


name = "Suleman"

print(name[3])

last_name = "Mazhar"

full_name = name + " " + last_name

print(full_name)



# sting manipulation

print("hello".upper())
print("HELLO".lower())
print("this is a.... cool sentence".split('.'))