# creating some variables
name = "Nick"
age = 45
temperature = 10
answer = True

"""
Here is a very cool sentence!

"""
print(f"My name is {name} and I am {age} years old.")
print(f"Today it is {temperature} degrees celcius. \nThis is {answer}.")
print(f"\nThe variables and types from above are as follows:")
print(f"Nick is a ", type(name)) 
print(f"45 is a ", type(age)) 
print(f"10 is a ", type(temperature)) 
print(f"True is a ", type(answer), "\n")

# datatypes in python
n = 5 # integer
pi = 3.14 # float
name = "Bob James" # string
is_student = True # boolean
fruit = ["apple", "banana", "pears", 8] #list
coordinates = (10, 20) # tuple - immutable
person = {"name": "Nick", "age": 45} # dictionary
numbers = {1, 2, 3, 4, 5, 5} # set - no duplicates

a = 15
b = 4
add = a + b
print(add)

subtract = a - b
print(subtract)

multiply = a * b
print(multiply)

divide = a / b
print(divide)

intdiv = a // b
print(intdiv)

modulo = a % b
print(modulo)

power = a ** b
print(power)

# Hello World
hej = "Hello, World!"
print(hej[0])
print(hej[6:12])

# Prints every other character
print(hej[1::2])

# Using a for loop
for i in range(len(hej)):
    if i % 2 != 0:
        print(hej[i], end="")
print("\n")

# While loop ... like in C?
# Prints Hello, World! backwards
index = len(hej) - 1
while index >= 0:
    print(hej[index], end="")
    index -= 1
print("\n")

# I should use Python's slicing capabilities
print(hej[::-1])

