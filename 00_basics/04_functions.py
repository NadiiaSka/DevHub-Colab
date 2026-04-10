# 04_functions.py
# Functions are reusable blocks of code. Define once, use many times!

def say_hello():
    print("Hello! Nice to meet you!")

def say_hello_to(name):
    print("Hello,", name + "! Great to see you!")

def add(a, b):
    return a + b

# Call the functions
say_hello()
say_hello_to("Alice")
say_hello_to("Bob")

result = add(3, 5)
print("3 + 5 =", result)

# Try it yourself:
# Write your own function that prints your name and age!
