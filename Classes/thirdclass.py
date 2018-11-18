#import datetime             #importing datetime library - it can be also called specifically for calling the function as below
#±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±
class Dog:
    name = "johnny"         #declaring variable in a class so it becomes static variable or class

    def bark(self):
        print("waff waff")

    def jump(self):
        print("hop hop")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`

class cat:
    @staticmethod
    def run():
        print("Running....")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class student:                      # define constructor student
    def __init__(self, ID, name, grade):
        self.ID = ID
        self.name = name
        self.grade = grade
        print(ID, name, grade)
#±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±



def main():
    rex = Dog()
    rex.bark()
    rex.jump()              #calling object rex from type dog which can jump as a function

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    cat.run()               #calling static function with  no objects
#±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±

    ziv = student(29620812, 'zy', 99)     #put values in constractor ziv which is from student type




if __name__ == '__main__':
    print(Dog.name)
    main()
    from datetime import datetime   #instant library import (more efficient and more secured)
#    print(datetime.datetime.now())  #calling datetime which was imported in the head of this code
    print(datetime.now())  #calling datetime which was imported 2 lines above






