class Student:

    i=0

    def __init__(self,name,height,shoesize):
        self.name=name
        self.height=height
        self.shoesize=shoesize
        self.stuCount=stuCount
        Student.stuCount += 1

#     def display(self):
#         print "here is a list of students"
#         print "his/her name is:", self.name
#         print "his/her height is:", self.height
#         print "his/her shoesize is:", self.shoesize
#         print "his/her id number is:", self.id
#         print
#
#
#
# ben = Student("Ben", "5'9", "11")
# ben.display()
#
# gabe = Student("Gabe", "5'10", "11")
# gabe.display()
#
# javier = Student("Javier", "5'8", "10")
# javier.display()
#
# aidan = Student("Aidan", "5'9", "9")
# aidan.display()

    def displayCount(self):
        print "Total Students %d" % Student.stuCount


    def displayStudent(self):
            print "Name : ", self.name,  ", Height: ", self.height,  ", Shoesize: ", self.shoesize


stu=[]

while 1:
    inp = raw_input("Enter 1 to add student, 2 to list students: ")
    if inp == "1":
        name = raw_input("Enter Name: ")
        height = raw_input("Enter height: ")
        shoesize = raw_input("Enter shoesize: ")
        stu.append(Student(name,height,shoesize))
    elif inp == "2":
        try:
            for i in range(0,len(stu)):
                stu[i].displayStudent()
            print "Total students %d" % (Student.stuCount)
        except IndexError:
            print "No current students"
    else:
        print "Invalid input"
