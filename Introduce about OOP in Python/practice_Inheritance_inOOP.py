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
        Animal.__init__(self, 'Dog', nameA, widthA, heightA, weightA, isChampionA, whatToEatA)
        # assign values ​​to additional properties :
        self.whatToEat = whatToEatA
        self.isChampion = isChampionA

    # override mothod:
    def makeVoice(self):
        print('{0}: Woof'.format(self.name))

dog1= Dog('Lucky', '45cm', '30cm','12kg', True,'Mix rice')
dog2= Dog('Roll', '100cm', '80cm','20kg', True,'Mix rice')
dog1.makeVoice()
dog1.printMe()
dog2.makeVoice()
dog2.printMe()