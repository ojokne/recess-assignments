# OJOK EMMANUEL NSUBUGA
# 21/U/06816/PS
# 2100706816

# EXCEPTION HANDLINH

def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Invalid operand types for division.")
    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        print("Finally block executed.")


# Example usage
num1 = 10
num2 = 0
result = divide_numbers(num1, num2)
if result is not None:
    print(f"Result: {result}")


# FILE HANDLING

# Writing to a file
def write_to_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
            print(f"Successfully wrote to file: {filename}")
    except Exception as e:
        print(f"An error occurred while writing to file: {str(e)}")


# Reading from a file
def read_from_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Content of file '{filename}':")
            print(content)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred while reading from file: {str(e)}")


# Example usage
filename = "example.txt"

# Writing to file
write_to_file(filename, "Hello, world!")

# Reading from file
read_from_file(filename)
