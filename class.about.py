'''
CLASS
(1) What is Class?
(2) Ordinary and Static properties
(3) Special Methods
'''

print("==== What is Class? ====")
# Class is a blueprint for Object creation!
# Class structure: state, constructor, method


class Person():
    # state
    message = "class state property"

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method1
    def intro(self):
        print(f"{self.name} says: How do you do?")

    # method2
    def say_age(self):
        print(f"{self.name} says he is {self.age}")

    @classmethod
    def explain(cls):
        print("static method property executed")


person1 = Person("Justin", 19)
person2 = Person("Martin", 21)
person3 = Person("John", 21)

# ordinary state
print("person1.name: ", person1.name)


# ordinary method
person1.intro()
person2.say_age()

# static state
print("new_massage: ", person1.message)
print(Person.message)


# static method
Person.explain()
person1.explain()  # methods work with objects too?
