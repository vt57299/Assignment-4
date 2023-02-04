# Write a Python program to triple all numbers of a given list of integers. Use Python map.

# sample list: [1, 2, 3, 4, 5, 6, 7]
# Triple of list numbers:
# [3, 6, 9, 12, 15, 18, 21]


# Getting list from user
lst = []
size = int(input("Enter size of list: "))
for i in range(size):
    elements = int(input("Enter elements: "))
    lst.append(elements)
print("Your list: ",lst)

# Tripling the elements of list
def triple(lst):          
    return lst*3
data = list(map(triple,lst))
print("Triple of list numbers: ", data)