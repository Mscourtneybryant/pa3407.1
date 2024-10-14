import re

# The Mighty Calculator
def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero!"

result = add_numbers(5, 3)
print("The sum is:", result)

result = subtract_numbers(10, 4)
print("The difference is:", result)

result = multiply_numbers(6, 2)
print("The product is:", result)

result = divide_numbers(15, 0)
print("The quotient is:", result)




# number one

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

num = int(input("Enter a number to find the Fibonacci sequence: "))
if num >= 0:
    print(f"The Fibonacci number at position {num} is {fibonacci(num)}")
else:
    print("Please enter a positive integer")


# number two 

def decode_message(encrypted_message, cipher_map):
    decrypted_message = ""
    for letter in encrypted_message:
        if letter in cipher_map:
            decrypted_message += cipher_map[letter]
        else:
            decrypted_message += letter
    return decrypted_message

cipher_map = {'H': 'S', 'e': 'o', 'l': 'l', 'o': 'a', 'W': 'H', 'r': 'w', 'd': 'r'}
encrypted_message = "Hello World"
print("Decrypted message:", decode_message(encrypted_message, cipher_map))


# number three 


def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(pattern, email):
        return True
    else:
        return False

email = input("Enter an email address to validate: ")
if validate_email(email):
    print("The email address is valid.")
else:
    print("The email address is invalid.")
