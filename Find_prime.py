import math

def is_prime(number):
    """Checks if a given number is a prime number."""

    if number <= 1:
        return False
    
    if number == 2:
        return True
  
    if number % 2 == 0:
        return False
    
    limit = int(math.sqrt(number)) + 1
    for i in range(3, limit, 2):
        if (number % i) == 0:
            return False
            
    return True

user_input = input("Enter a number to check: ")

try:
    num = int(user_input)
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
