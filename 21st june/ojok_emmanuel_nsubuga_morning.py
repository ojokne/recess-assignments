# OJOK EMMANUEL NSUBUGA

# 21/U/06816/PS

# 2100706816

# QUESTION 1
# Write a program to ask students about their mental health
# Ask for the student's name
name = input("Enter your name: ")

# Prompt for mental health rating
rating = int(input("On a scale of 1 to 10, how would you rate your mental health? "))

# Validate the rating
if rating < 1 or rating > 10:
    print("Invalid rating. Please enter a number between 1 and 10.")
else:
    # Display the rating
    print(f"Thank you, {name}! Your mental health rating is: {rating}")

    
# QUESTION 2
# Prompt students on a scale of 1 to 10 to rate thier mental health

print("Student Mental Health Survey")

# Ask for the student's name
name = input("Enter your name: ")

# Prompt for mental health rating
rating = int(input("On a scale of 1 to 10, how would you rate your mental health? "))

# Validate the rating and provide feedback
if rating < 1 or rating > 10:
    print("Invalid rating. Please enter a number between 1 and 10.")
else:
    print(f"Thank you, {name}! Your mental health rating is: {rating}")

    # Provide feedback based on the rating
    if rating <= 3:
        print("We're sorry to hear that you're experiencing challenges. Please consider reaching out to a trusted adult or professional for support.")
    elif rating <= 7:
        print("It's great to hear that your mental health is relatively good. Keep up the self-care practices.")
    else:
        print("Fantastic! Your mental health is in a good place. Keep up the positive mindset and self-care routines.")
