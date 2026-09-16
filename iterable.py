print("==== Iterable Objects and Range ====")
# Irerable Objects > String Dictionary Tuple List Range Map Filter

range_obj = range(3)  # [0:3)
print("the range_obj: ", range_obj)

text = "MIT"
for letter in text:
    print("the letter: ", letter)

# Iretating range_obj
for element in range_obj:
    print("the element: ", element)


print("==== Dictionary ====")
# Dictonary is JSON Object
person = {"name": "Justin", "age": 35, "single": True}
person_obj = dict(name="Justin", age=25, single=True)

print(f"the person: {person}")
print(f"the person_obj: {person_obj}")

# method: get()
# name = person_obj["name"]

name = person_obj.get("name")
hobby = person_obj.get("hobby")
balance = person_obj.get("balance", 0)

print("name", name)
print("hobby", hobby)
print(f"the name: {name}, the hobby: {hobby}, and balance: {balance}")

del person_obj["single"]
for key in person_obj:
    print(f"the key: {key} => value {person_obj.get(key)}")
