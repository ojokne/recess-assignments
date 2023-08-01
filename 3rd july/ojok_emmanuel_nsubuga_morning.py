# matching and searching

# re.match() function
# re.search() function
# re.findall() function

# Example 1 Demonstrating regex 
# match first word in a string
# match group word
# match all numbers

import re

text = "Hello, my name is Jeff Geof. I am a programmer with 15 years of experience"

# match first word in a string
match = re.search(r"\b\w+\b", text)

if match:
    print("Found match: ", match.group())

matches = re.findall(r"\d+", text)

print("Matches: ",matches)

# Example 2
# validate email address

import re

def validate_email(email):
    pattern =  r'^[\w\.-]+@[\w\.-]+\.'
    if re.match(pattern, email):
        return True
    else:
        return False
    
# example usage
email1 = "jeff.geof98@gmail.com"
email2 = "jeff.geof98@gmailcom"

print(validate_email(email1))
print(validate_email(email2))

# Generators
# yeild keyword
# iterator '__iter__' and '__next__' methods

def factorial(n):
    # Return the factorial of a number
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
    
# print the factorial of a number from 1 - 5
for i in range(1,10):
    print(factorial(i))

# Example 3

def squares():
    for i in range(1,10):
        yield i**2

# create an iterator object that yeilds the squares of numbers from 1-10
squares_iterator = squares()

# print  the first 5 squares of numbers from 1-10
for i in range(5):
    print(next(squares_iterator))
    

# decorators @my_decorator

def my_decorator(func):
    def inner():
        print("This is the decorator")
        func()
    return inner
    
@my_decorator
def outer_decorator():
    print("This is the outer decorator")


outer_decorator()