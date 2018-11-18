# answer A
class dog:
    def __init__(self, shem, age):
        self.shem = shem
        self.age = age

#answer B
# class ConstructedShark:
#     def __init__(self, age):
#         self.age = age
#
# def main():
#     stevie = ConstructedShark(3)
#     print(stevie.age)
#
# if __name__ == "__main__":
#     main()
#±±±±±±±±±±±±±±±±±±±±±±±±±±±±
#±±  THE OUTPUT WILL BE 3  ±±
#±±±±±±±±±±±±±±±±±±±±±±±±±±±±
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#answer C
class car:
    @staticmethod
    def start():
        print("car is running....")
#±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±

#answer D
class husky(dog):
    def __init__(self, shem, age, howl):
        self.shem = shem
        self.age = age
        dog.__init__(self, shem, age)
        self.howl = howl

#±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±

#answer E
class BlackHusky(husky):
    def __init__(self, shem, age, howl, color):
        self.shem = shem
        self.age = age
        self.howl = howl
        husky.__init__(self, shem, age, color)
        self.color = color
    def return_color(self, color):          #this should be the method  getting the dog color
        self.color = color
#±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±

#answer F
#the code below has a missing main() function!!!
#need to add  "main()" before below the if__init__ line

#±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±

#answer G
import array as arr
a = arr.array("i",[3,6,9])
for i in range(len(a)):
    print(a[i])

my_list = {'Su': 5,'Zu': 6,'Key': 7}
print(my_list.keys(), my_list.values())



def main():
    raxi = dog('max', 6)
    print(raxi.shem, "is ", raxi.age, "years old.")

    dogsound = husky('max', 9, 'ahoooo')
    print(dogsound.howl)

#   dogcolor = BlackHusky.return_color('Black')     #this is static call and missing arguments to BlackHuskey
#    dogcolor = BlackHusky("joe", 2, True, "blue").return_color('Black')
#    print("the dog is", dogcolor)
    dogcolor = BlackHusky("joe",2,True,"blue")
    print('the dig is', dogcolor.color)




if __name__ == "__main__":
    main()

    car.start()               #calling static function with  no objects

