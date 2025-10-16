import sys
import math

def is_prime(n):
    """Checks if a number is prime using an optimized method."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_pth_prime(p):
    """Finds the p-th prime number."""
    if p < 1:
        raise ValueError("Input must be a positive integer.")
    
    count = 0
    num = 1
    while count < p:
        num += 1
        if is_prime(num):
            count += 1
    return num

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <p>")
        sys.exit(1)
    
    try:
        p_input = int(sys.argv[1])
        if p_input < 1:
            print("Error: Please provide a positive integer.")
            sys.exit(1)
        
        prime_number = find_pth_prime(p_input)
        # A simple way to add suffixes like 'st', 'nd', 'rd', 'th'
        if 10 <= p_input % 100 <= 20:
            suffix = 'th'
        else:
            suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(p_input % 10, 'th')
            
        print(f"The {p_input}{suffix} prime number is: {prime_number}")

    except ValueError:
        print("Error: Invalid input. Please provide an integer.")
        sys.exit(1)
