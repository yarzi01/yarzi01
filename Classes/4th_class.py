# I/O overview

my_file = open("/Users/yarzi01/Documents/DevOps/classes/kuku.txt", 'r+', encoding='utf-8')
content = my_file.read()
print(content)

content = my_file.write('\n' "בוקר טוב")
my_file.close()

try:
    newfile = open("/Users/yarzi01/Documents/DevOps/classes/kuku.txt", 'r+')
except IOError:
    print("Error: cant open file for modify")
try:
    print(newfile.read())
    newfile.close()
except IOError:
    print("this is wrong")
finally:
    print("this will not run")



