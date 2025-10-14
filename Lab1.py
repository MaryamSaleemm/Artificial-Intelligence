######ACTIVITY 1
# sum of values until the user enter zero
Sum = 0
x = int(input("Enter the number:"))

while x!=0:
    x = int(input("Enter the number:"))
    Sum+= x
print("sum is:",    Sum)
    


######ACTIVITY 2
# even or not
e = int(input("Enter a number:"))

if e % 2 == 0:
    print("Number is even")
else:
    print("Number is not even")

######ACTIVITY 3
# prime or not

prime = True
i = 2
n = int(input("Enter a number:"))

while i < n:
    remainder = n % i
    if remainder == 0:
        prime = False
        break
    else:
        i = i + 1
        
if prime:
    print("Number is prime")
else:
    ("Number is even")

######ACTIVITY 4
# Accept 5 integer values from user and display their sum


sum = 0
i = 0

while i <= 4:
    s = input("Enter a number:")
    x = int(s)
    sum += x
    i = i + 1
print("sum is:", sum)
    

######ACTIVITY 5
#Calculate the sum of all the values between 0-10 using while loop.


sum = 0
i = 1

while i <= 10:
    sum += i
    i = i + 1
print("sum is:", sum)



######ACTIVITY 6
#Take input from the keyboard and use it in your program.

name = input("Enter your name:")
print("Hello,", name)


######ACTIVITY 7
#

import random

# generate a random number between 1 and 9
secret = random.randint(1, 9)

guesses = 0  # counter for number of guesses

print("Guess the number between 1 and 9! Type 'exit' to quit.")

while True:
    user_input = input("Enter your guess: ")

    if user_input.lower() == "exit":   # stop the game
        break

    # convert input to integer
    guess = int(user_input)
    guesses += 1

    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("Exactly right! 🎉")
        break

print("Game over! You made", guesses, "guesses.")

######     Lab Task 1
#prompts the user to input an integer and then outputs the number with the digits reversed

n = int(input("Enter an integer: "))

reversed_num = int(str(n)[::-1])

print("Reversed number:", reversed_num)


######     Lab Task 2
#program that reads a set of integers, and then prints the sum of the even and odd integers

numbers = list(map(int, input("Enter integers separated by space: ").split()))

even_sum = 0
odd_sum = 0

for num in numbers:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)

# Lab Task 3 
#fibonacci

n = int(input("Enter how many terms you want: "))

a, b = 0, 1  

for i in range(n):
    print(a, end=" ")   
    a, b = b, a + b 

# Lab Task 4
# Accept marks (1-100) and display grade

marks = int(input("Enter marks (1-100): "))

if marks < 50:
    grade = "F"
elif marks <= 60:
    grade = "E"
elif marks <= 70:
    grade = "D"
elif marks <= 80:
    grade = "C"
elif marks <= 90:
    grade = "B"
elif marks <= 100:
    grade = "A"
else:
    grade = "Invalid input"

print("Grade:", grade)

######     Lab Task 5
# factorial of a number

factorial = 1

x = int(input("Enter a number:"))

while x > 0:
   
    factorial *= x
    x = x - 1
print("factorial is:", factorial)