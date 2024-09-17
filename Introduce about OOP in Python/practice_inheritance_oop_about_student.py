class People:
    def __init__(self, fullName, yearOfBirth, sex):
        self.name = fullName
        self.age = yearOfBirth
        self.gender = sex

    def eat(self):
        print('Do an la:')
    def drink(self):
        print('Do uong la:')
    def sleep(self):
        print('Cho ngu la')

    # Print all information:
    def printForPeople(self):
        print('name = {0}, age = {1} , gender = {2}'.format(self.name , self.age, self.gender))

# b1 = People('Peter', '30', 'men')
# b1.printForPeople()
# b1.eat()
# b1.drink()
# b1.sleep()

class Student(People):
    #contructor:
    def __init__(self, fullName, yearOfBirth, sex, studentId, codeClass, schoolName ):
        People.__init__(self, fullName, yearOfBirth, sex)
        self.student = studentId
        self.code = codeClass
        self.school = schoolName
    
    def eat(self):
        print('An com = {0}'.format(self.name))
    def drink(self):
        print('Uong bia = {0}'.format(self.name))
    def sleep(self):
        print('Ngu tren giuong : {0}'.format(self.name))
    
    def inforOfStudent(self):
        print('student = {0}, code = {1}, school ={2}'.format(self.student, self.code, self.school))
    
    def homeWork(self):
        print('{0}: Student allway home work'.format(self.name))

C1 = Student("Mr.Teo", 2000, 'Gay',111111, 'tn23tr', 'Hoa khanh University' )   
C1.eat()
C1.drink()
C1.sleep()
C1.inforOfStudent()
C1.homeWork()

# hobby ....