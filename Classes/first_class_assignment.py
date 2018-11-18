# assignment A
x = 7
y = 44.3
print(x + y)
print(x*y)
print(y/x)

# assignment B
a = 8
a = 17
a = 9
b = 6
c = a + b
b = c + a
b = 8
print("the values of a b c are:", a, b, c)

# assignment C
name = "john"
print(name)
name = 'john'
print(name)
print("There is no difference between the 2 formats because Python accept both syntax")

my_number = 5+5
# print("result is: "+my_number) will not work because the var type is different from string and "+" need the same type
# suggesting to convert with str or change the "+" with "," which ignores the var type
print("result is: "+str(my_number))
print("result is:", my_number)

# assignment D
x = 5
y = 2.36
print(x+int(y))
# "int" declare an integer which means the value after the floating point will be removed so the result is 7

# challenge
a = 8
b = "123"
# print(a + b)
# the print above will not work since the "+" requires same var type
# suggested syntax below:
# for text sum:
print(str(a) + b)
# for integer sum:
print(a + int(b))

print()


