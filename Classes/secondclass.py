a = 1
b = 2

if a > b:
    print("a is bigger")
elif a == b:
    print("equals")
elif a != b:
    print("not equal")
else:
    print("none")
# ±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±
for x in range(5):
    print(x)
# below loop strats with index value 3
for x in range(3,5):
    print(x)
# below loop starts with index value 3 until 8 in steps 2
for x in range (3,8,2):
    print(x)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# below loop is while and we need to increment the counter
count = 0
while count < 10:
    print (count)
    count += 1
# the below condition breaks the loop when counter get to 8
    if count == 8:
        break
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# the below condition skip one
# count = 0
# while count < 12:
# the below condition breaks the loop when counter value is 8
#     if count == 8:
#         continue
#         print (count)
#     count += 1
# while loop with else condition
count = 0
while count < 10:
    print (count)
    count += 1
else:
    print("I am out of the loop")

# the below loop add internal logic within the loop by using pass so it will print the condition and keep doing the "m"
for letter in 'Python':
   if letter == 'h':
       pass
       print('This is pass block')
   print('Current Letter :', letter)

print("Good bye!")




