class Myclass:
# answer G
# beginning of function printhello
    def main(self):
        print('Hello')
# end of function printhello

#beginning of function calculate
    def calculate(self):
        y = 5 + 3.2
        print(y)
# end of function calculate

#answer H
    def get_and_return(self, name):
        return "name is:" + name

    def getnumber(self, num):
        n = num / 2
        return n

# answer I
    def sum(self, num1, num2):
        n = num1 + num2
        return n

    def spaceadd(self, word1, word2):
        str = word1 + ' ' + word2
        return str


# this is the program starting point

if __name__ == '__main__':

    Myclass().main()                        #calling the first function printhello
    Myclass().calculate()                   # calling the calculator
    n = Myclass().get_and_return("Ziv")     # calling the the getname and provide the name
    print(n)                                # print the name recieved by the function

    y = Myclass().getnumber(8)              #calling hte function which return the number devided by 2
    print("number devide by 2 is:", y)

    x = Myclass().sum(5, 9)                 #calling the summary function
    print("the sum is:", x)

    w1 = input("enter first word:")
    w2 = input("enter second word:")
    myphrase = Myclass().spaceadd(w1, w2)   #calling the string spacing function
    print("my sentense is:", myphrase)      # return the phrase after adding the space betwen the 2 strings which was provided from the keyboard


