my_file = open("/Users/yarzi01/Desktop/ziv.txt", 'w')
content = my_file.write('\n' "ziv yarshansky")
my_file.close()

my_file = open("/Users/yarzi01/Desktop/ziv.txt", 'r')
content = my_file.read()
print(content)
my_file.close()