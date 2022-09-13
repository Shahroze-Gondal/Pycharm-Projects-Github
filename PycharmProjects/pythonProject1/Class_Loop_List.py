dogs = ['roger', 1, True]
dogs[2] = 5
dogs.append('hello')
dogs.extend(['inaam', 1])
dogs.remove(1)
dogs.insert(3, 'Imran Khan')
print(dogs)

# Loops
items = ['h', 'g', 'j']
for x in enumerate(items):
    print(x)

# Classes


class Animal:
    def walk(self):
        print("Walking..")


class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print('Barking')


dog_obj = Dog('German', 20)
dog_obj.bark()
dog_obj.walk()
print(type(dog_obj))
print(dog_obj.age)
