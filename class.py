class Student:

    i=0

    def __init__(self,name,height,shoesize):
        self.name=name
        self.height=height
        self.shoesize=shoesize
        self.id=Student.i
        Student.i += 1

    def display(self):
        print "here is a list of students"
        print "his/her name is:", self.name
        print "his/her height is:", self.height
        print "his/her shoesize is:", self.shoesize
        print "his/her id number is:", self.id
        print



ben = Student("Ben", "5'9", "11")
ben.display()

gabe = Student("Gabe", "5'10", "11")
gabe.display()

javier = Student("Javier", "5'8", "10")
javier.display()

aidan = Student("Aidan", "5'9", "9")
aidan.display()
