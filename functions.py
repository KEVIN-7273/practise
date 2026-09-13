''' FUNCTIONS
    (1) Define vs Call
    (2) Parametr va Argument
    (3) Keyword
    (4) Scope
'''

print("========= Define vs Call ==========")
# __builtins__ => print() type()
# Function => reusable block of code
# Instead of block {} in Java, Python uses indentation!

# Define - build


def greet(a):       # a - bu yerda parametr
    print(f"How do you do, {a}")


def greeting(b):
    print("greeting is executed")
    return f"Hi {b}"


# CALL -  execute
result1 = greet("Martin")       # Martin bu yerda Argument
print("result1:", result1)

result2 = greeting("Kevin")     # Kevin bu yerda Argument
print("result2:", result2)


print("========= Define vs Call ==========")


# DEFINE
def give_greet(name, age=22):
    print("give_greet is executed")
    return f"Hi {name}, you are {age} years old!"


# call
result3 = give_greet(name="Justin", age=28)
print("result3: ", result3)

result3 = give_greet(name="John")
print("result3: ", result3)


print("========= Define vs Call ==========")

b = 100  # 3


def calculate(a, b):  # 2
    c = a * b  # 1
    print(f"the c value: {c}")


# call
calculate(5, 50)
