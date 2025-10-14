##Activity 1
# Integr type list join
list1 = []
n = int(input("how many elements you want to add"))

i = 0
while i < n:
    s = int(input("enter a number"))
    list1.append(s)
    i = i + 1


list2 = []
r = int(input("how many elements you want to add"))

k = 0
while k < r:
    p = int(input("enter a number"))
    list2.append(p)
    k = k + 1

join_of_two_lists = list1+list2
print("join of two lists is this: " , join_of_two_lists)

##Activity 2
#find if a string is a palindrome or not


def isPalindrome(p):
    temp = p[::-1]

    if(p.capitalize() == temp.capitalize()):
        return True
    else:
        return False


p = str(input("enter a string: "))
palindrome = isPalindrome(p)    
print(palindrome)
    

##Activity 3
#Write a python code that finds another matrix/2D list that is a product of and b, i.e., C=a*b

a = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
c = [[0 for _ in range(3)] for _ in range(3)]  # Initialize 3x3 matrix with zeros

for i in range(3):
    for j in range(3):
        for k in range(3):
            c[i][j] += a[i][k] * b[k][j]

print(c)

##Activity 4
#perimeter of a polygon

def perimeter(points):
    total = 0
    for i in range(len(points)):
        j = (i + 1) % len(points)  # Connect last point to first
        x1, y1 = points[i]
        x2, y2 = points[j]
        total += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return total

p = [(0, 0), (1, 0), (1, 1), (0, 1)]
print(perimeter(p))

#Activity 5: Symmetric Difference

def symmetric_difference(a, b):
    return a.symmetric_difference(b)


set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
result = symmetric_difference(set1, set2)
print(result)  # Should print {1, 2, 5, 6}

#Actvity no 6
#Phone Number Dictionary

phone_book = {
    ("john", "doe"): "1234567890",
    ("jane", "smith"): "0987654321",
    ("alice", "johnson"): "5555555555"
}

# Search function
firstName = input("Enter first name: ")
lastName = input("Enter last name: ")
searchTuple = (firstName.lower(), lastName.lower())  # Case-insensitive

if searchTuple in phone_book:
    print(phone_book[searchTuple])
else:
    print("Name not found")
    
    ###Lab Task 1 – Merge Two Lists and Display in Sorted Order
# Lab Task 1
# Create two lists based on user input, merge them, and display in sorted order.

list1 = []
list2 = []

n1 = int(input("Enter number of elements for List 1: "))
for i in range(n1):
    val = int(input(f"Enter element {i+1} for List 1: "))
    list1.append(val)

n2 = int(input("Enter number of elements for List 2: "))
for i in range(n2):
    val = int(input(f"Enter element {i+1} for List 2: "))
    list2.append(val)

merged_list = list1 + list2
merged_list.sort()

print("\nMerged and Sorted List:", merged_list)

####Lab Task 2 – Find Smallest and Largest Element
# Lab Task 2
# Reuse merged list from Task 1

print("Smallest element:", min(merged_list))
print("Largest element:", max(merged_list))

###Lab Task 3 – Numerical Derivative of sin(x)
# Lab Task 3
from math import sin, cos, pi

h = 0.001  # small increment
x = -pi

print("\nX value".ljust(15), "Approx Derivative".ljust(20), "cos(x)")
while x <= pi:
    approx_derivative = (sin(x + h) - sin(x)) / h  # derivative approximation
    print(f"{x:.3f}".ljust(15), f"{approx_derivative:.6f}".ljust(20), f"{cos(x):.6f}")
    x += 0.1  # using 0.1 for fewer print lines (change to 0.001 for full range)

# Try h = 0.01 and h = 0.1 to observe changes in accuracy



#####Lab Task 4 – Birthday Dictionary
# Lab Task 4

birthdays = {
    "Albert Einstein": "03/14/1879",
    "Benjamin Franklin": "01/17/1706",
    "Ada Lovelace": "12/10/1815"
}

print("Welcome to the birthday dictionary. We know the birthdays of:")
for name in birthdays:
    print(name)

person = input("\nWho's birthday do you want to look up? ")
if person in birthdays:
    print(f"{person}'s birthday is {birthdays[person]}.")
else:
    print(f"Sorry, we don't have {person}'s birthday.")

######Lab Task 5 – Extract Keys from Dictionary
# Lab Task 5

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
keys = ["name", "salary"]

new_dict = {k: sample_dict[k] for k in keys}
print("\nExtracted Dictionary:", new_dict)