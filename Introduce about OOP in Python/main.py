# Example about create class simple in OOP of PYTHON:
class SimpleClass:
    #Attribute:
    i = 5

    #_init_:
    def __init__(self):
        self.j = 7
    
    # methods:
    def printMe(self):
        print(self.j)

objectA= SimpleClass()
objectB= SimpleClass()

objectA.printMe()
print(objectB.i)

# Change value of attribute:
objectA.i = 100
objectB.j = 500
print(objectA.i)
objectB.printMe()

# STATIC METHOD:
class SimpleClass2:
    # contructor:
    def __init__(self):
        self.name = "Long"
    
    # methods:
    def hello(self):
        print("Hello " + self.name)

    #static methods:
    @staticmethod
    def whatSup(name):
        print('What sup ' +  name)

objectC = SimpleClass2()
objectD = SimpleClass2()
objectC.hello()
objectD.whatSup('Peter_Chang')


SimpleClass2.whatSup('Ti')