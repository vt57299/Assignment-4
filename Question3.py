# Write a Python program to square the elements of a list using map() function.

# Sample List: [4, 5, 2, 9]
# Square the elements of the list:
# # [16, 25, 4, 81]


# Getting list from user
lst = []
size = int(input("Enter size of list: "))
for i in range(size):
    elements = int(input("Enter elements: "))
    lst.append(elements)
print("Your list: ",lst)

# Squaring the elements of list using map() function
def square(lst):
    return lst**2
data = list(map(square,lst))
print("Square of the elements: ", data)