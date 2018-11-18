# class car:
#     def __init__(self, model, color):
#         self.model = model
#         self.color = color
#
# class ElectricCar(car):
#     def __init__(self, model, color, battery_type):
#         car.__init__()
#

# data stracture - array
import array as arr
a = arr.array("i",[3,6,9])
print(a[1])
a.append(11)
print(a[3])
a.pop(0)
print(a[0])
a.insert(0,99)
print(a[0])

# array functionality
print("array length", len(a))

for temp_num in a:
    print(temp_num)

    for i in range(len(a)):
        print(a[i])

my_list = [5, "a", True]        # list has the same functionality as an array



