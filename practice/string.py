a = "apple"
print(a.upper())

b = "CAT"
print(b.lower())

print(a.count("p"))

c = "hello worlodo"
print(c.index("o", 8))


# formating string
name = "John"
age = 30
print(f"My name is {name} and I am {age} years old.")
print("My name is {} and I am {} years old.".format(name, age))
print("My name is {1} and I am {0} years old.".format(age, name))
print("My name is {name} and I am {age} years old.".format(name="Jane", age=25))
