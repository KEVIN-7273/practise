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
result1 = greet("Martin")       # Martin bu yerda
Argument
print("result1:", result1)

result2 = greeting("Kevin")
print("result2:", result2)
