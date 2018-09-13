class Person:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def greet(self):
        print("Hello, world! I am %s" % self.name)

class Class:
    def method(self):
        print('i have a self')

def function():
    print("i don't ...")

instance = Class()
instance.method()

instance.method = function
instance.method()