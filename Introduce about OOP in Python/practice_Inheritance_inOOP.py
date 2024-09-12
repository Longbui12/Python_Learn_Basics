# example :
class Animal:
    # Contructor: Build to object
    def __init__(self, animalTypeA, nameA, widthA, heightA, weightA):
        self.animalType = animalTypeA
        self.name = nameA
        self.width = widthA
        self.height = heightA
        self.weight = weightA

    # emits sound:
    def makeVoice(self):
        print('Unknow Voice !')

    # Print information:
    def printMe(self):
        print('animalType: {0}, name = {1}, width={2}, height={3}, weight={4}'.format(self.animalType, self.name, self.width, self.height, self.weight))

a1 = Animal('Human', 'Peter_Chang','','164cm','60kg')
a1.printMe()
a1.makeVoice()
 
class Dog(Animal):
    #contructor:
    def __init__(self, nameA, widthA, heightA, weightA, isChampionA, whatToEatA):
        # call contructor of parent class
        #Animal.__init__(self, 'Dog', nameA, widthA, heightA, weightA, isChampionA, whatToEatA)
        super().__init__('Dog', nameA, widthA, heightA, weightA)
        # assign values ​​to additional properties :
        self.isChampion = isChampionA
        self.whatToEat = whatToEatA

    # override mothod:
    def makeVoice(self):
        print('{0}: Woof'.format(self.name))

    # Override printMe to include Dog-specific details
    def printMe(self):
        super().printMe()  # Call the parent class's printMe method
        print('isChampion ={0}, whatToEat={1}'.format(self.isChampion, self.whatToEat))
    
    def takeCareHome(self):
        print('{0}: take care home'.format(self.name)) 

dog1= Dog('LUCKY', ' 45cm', ' 30cm',' 12kg', True ,' Mix rice')
dog2= Dog('ROLL ', ' 100cm', ' 80cm',' 20kg', True ,' Mix rice')
dog1.makeVoice()
dog1.printMe()
dog1.takeCareHome()
dog2.makeVoice()
dog2.printMe()

class Cat(Animal):
    #contructor:
    def __init__(self, nameA, widthA, heightA, weightA, whatToEatA, colorA):
        # call contructor of parent class:
        #Animal.__init__(self, 'Cat', widthA, heightA, weightA)
        super().__init__('Cat', nameA, widthA, heightA, weightA)
        # assign values ​​to additional properties :
        self.color = colorA
        self.whatToEat = whatToEatA
        
    # override method :
    def makeVoice(self):
            print('{0}: meow meow'.format(self.name))
    def printMe(self):
            super().printMe()
            print('whatToEatA = {0}, color = {1}'.format(self.whatToEat, self.color ))
          
    def catchMouse(self):
         print('{0}: catch a mouse'.format(self.name))

cat1 = Cat('Miu miu', '30cm', '6kg','10cm', 'Mix rice','orange')
cat1.makeVoice()
cat1.printMe()
cat1.catchMouse()
cat2 = Cat('Tom', '40cm', '10kg','15cm', 'Mix rice','Black')
cat2.makeVoice()
cat2.printMe()