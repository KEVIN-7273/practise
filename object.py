'''
OBJECTS
1. What is object?
2. Iterable objects and Range
3. Dictionary
4. Error handling system

'''
import array  # package/module
import math  # package
from math import ceil, asin

print("==== What is Object? ====")

# An object has state and method properties
# Everything is an object in Python

print(type("Hello, World!"))
print(type(100))
print(type(True))
print(type(array))
print(type(math))

# Paradigm > Functional Programming and OOP
# OOP 4 concepts > Abstraction,  Encapsulation, Inheritence, Polimorphism

result1 = math.ceil(97.7)  # Call
print("result1: ", result1)

result2 = ceil(98.7)  # yaxshlitlash
print("result2: ", result2)


print("==== Error Handling System ====")
car_dict = dict(name="Toyota", year=2027, electric=True)

try:
    print("Passed here")
    result = car_dict["year"]
    print("result: ", result)
except KeyError as err:
    print("No origin state property found: ", err)
else:
    print("Executed successfully")
finally:
    print("Final closing logic")
