class Myclass:

# beginning of function main ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def main(self):

        for letter in 'Python':
            if letter == 'h':
                pass
                print('This is pass block')
            print('Current Letter :', letter)

        print("Good bye!")
# end of function main ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


z = 123
class Dog:

    def main():
        bark()

    def bark(self):
        print("Whaf Whaf")
        print(z)  # using global variant z

    def miau(self):
        print(z)  # using global variant z

        return "MIAU"

    def get_and_return(self,name):
        print(z)  # using global variant z
        return "name is:" + name




# this is contant definition in class where the program starts
if __name__ == '__main__':
     Myclass().main()
#calling function bark in Dog class
     Dog().bark()
#put value from a fanction which returns value
     voice = Dog().miau()
     print (voice)

#calling function which get and return value
     y = Dog().get_and_return("Ziv")
     print(y)

# keyboard input
mila = input("please enter.....")
print("name is: ", mila)
