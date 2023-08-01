# OJOK EMMANUEL NSUBUGA

# 21/U/06816/PS

# 2100706816

# QUESTION 1
# Use the values () method to return a list of all values in a dictionary

# Define a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Get all values using the values() method
values_list = list(my_dict.values())

# Print the list of values
print(values_list)

# QUESTION 2
# Program to check if a key exists in a dictionary
# Define a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Function to check if a key exists in the dictionary
def check_key(dictionary, key):
    if key in dictionary:
        return True
    else:
        return False

# Prompt the user to enter a key
key_to_check = input("Enter a key to check: ")

# Call the function to check if the key exists
result = check_key(my_dict, key_to_check)

# Print the result
if result:
    print("The key '{}' exists in the dictionary.".format(key_to_check))
else:
    print("The key '{}' does not exist in the dictionary.".format(key_to_check))


# QUESTION 3
# program to change dictionary
# Define a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Print the original dictionary
print("Original Dictionary:", my_dict)

# Update a specific key-value pair
my_dict['b'] = 5

# Print the updated dictionary
print("Updated Dictionary:", my_dict)

# Update multiple key-value pairs using another dictionary
new_values = {'a': 10, 'c': 20}
my_dict.update(new_values)

# Print the dictionary after updating multiple items
print("Dictionary after Multiple Updates:", my_dict)


# QUESTION 4
# program to add and delete items from a dictionary

# Define a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Print the original dictionary
print("Original Dictionary:", my_dict)

# Add a new key-value pair
my_dict['d'] = 4

# Print the dictionary after adding a new item
print("Dictionary after Adding an Item:", my_dict)

# Delete a key-value pair
del my_dict['b']

# Print the dictionary after deleting an item
print("Dictionary after Deleting an Item:", my_dict)


# QUESTION 5
# Program to iterate over dictionaries using for loops and how to nest dictionaries

# Define a dictionary
student_scores = {
    'John': 85,
    'Alice': 92,
    'Bob': 78,
    'Emma': 95
}

# Loop through the dictionary
print("Looping through the dictionary:")
for name, score in student_scores.items():
    print(name, ":", score)

# Nesting dictionaries
students = {
    'John': {
        'age': 18,
        'score': 85
    },
    'Alice': {
        'age': 20,
        'score': 92
    },
    'Bob': {
        'age': 19,
        'score': 78
    },
    'Emma': {
        'age': 17,
        'score': 95
    }
}

# Loop through the nested dictionaries
print("\nLooping through the nested dictionaries:")
for name, student_info in students.items():
    print("Name:", name)
    print("Age:", student_info['age'])
    print("Score:", student_info['score'])
    print()


# QUESTION 6
# use a condition to show how to use booleans

# Define boolean variables
is_sunny = True
is_raining = False

# Example 1: Simple boolean check
if is_sunny:
    print("It is sunny today!")
else:
    print("It is not sunny today.")

# Example 2: Multiple conditions
if is_sunny and not is_raining:
    print("It is sunny and not raining.")
elif is_sunny and is_raining:
    print("It is sunny but also raining.")
else:
    print("It is not sunny today.")

# Example 3: Boolean expression
temperature = 25
is_hot = temperature > 30

if is_hot:
    print("It is hot outside.")
else:
    print("It is not hot outside.")
