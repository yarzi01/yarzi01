class Myclass:
    def main(self):
        try:
            a = 1/0;                #ANSWER 1: the exception is caught and
        except:
            print("all type of errors are handled")

        try:
            x = 1
        finally:
            print("finally")    #ANSWER 2 & 3: this will be printed anyway

        try:                    #ANSWER 4
            f = open("/Users/yarzi01/Documents/DevOps/classes/kuku.txt", "r")
        except:
            print("All kind of errors will be handled")     #הקובץ נפתח לקריאה בלבד אך מכיוון שאין כתיבה אין בעיה

        try:                    #ANSWER 5
            f = open("/Users/yarzi01/Documents/DevOps/classes/kuku.txt", "r")
            f.write("123")                                  #כאן מתבצעת כתיבה לקובץ שנפתח לקריאה בלבד ולכן מתקבלת טעות
        except IOError:
            print("Error: can't find file or read data")
        try:
            newfile = open("/Users/yarzi01/Documents/DevOps/classes/kuku.txt", 'r+')
        except IOError:
            print("Error: cant open file for modify")       #כאן הקובץ נפתח לעדכון ולכן לא מתבצע ה exception

#ANSWER 6: except IOError: handles input output exceptions| except ZeroDivisionError: handle error which is result of divide by 0


#ANSWERS 7-10
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        my_file = open("/Users/yarzi01/Documents/DevOps/classes/words1.doc", 'w')
        content = my_file.write('\n' "Ziv Yarshansky")
        my_file.close()

        my_file = open("/Users/yarzi01/Documents/DevOps/classes/words1.doc", 'r+')
        content = my_file.write('\n' "זיו ירשנסקי")
        my_file.close()
        my_file = open("/Users/yarzi01/Documents/DevOps/classes/words1.doc", 'r')
        content = my_file.read()
        my_file.close()
        print(content)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


if __name__ == '__main__':

    Myclass().main()



