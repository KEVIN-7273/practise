# Dunder __builtins__, __init__
massage = "PYTHON: Everything is object!"
print(massage)

result = type(massage)
print("result: ", result)

''' I PYTHON , there are builtin tools:
(1) TYPES > int, float, str, list, dict,
(2) FUNCTIONS > print(), len(), inpit(), type(), str(), int()
(3) CONSTANTS > True, False, None
'''

print(dir(__builtins__))
