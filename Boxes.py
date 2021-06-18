import math
num = int(input("Enter numbers of items:  "))
box = int(input("Enter the amount of boxes:  "))
quantity = math.ceil(num/box)
print("For ",num, "items, packing ",box, "items in each box"
", you will need ", quantity, "boxes.")