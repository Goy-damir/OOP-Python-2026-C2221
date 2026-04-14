class Dog:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def Bark(self, cat):
        if self.status == cat.status:
            print((self.name), " bark at ", (cat.name))
        else:
            print((self.name), "ignors the cat")

class Cat:
    def __init__(self, name, status):
        self.name = name
        self.status = status
    def Scare(self, dog):
        if self.status == dog.status:
            print((self.name), "scared because of the bark")
        else:
            print((self.name), "ignores the dog")

dog = Dog("Joe", 1)
cat = Cat("Tom", 1)
dog.Bark(cat)
cat.Scare(dog)