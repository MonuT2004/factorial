def factorial(n):
    if n == 0 or n == 1:   # Base case
        return 1
    else:
        return n * factorial(n - 1)   # Recursive call

# Test the function
num = 5
print("Factorial of", num, "is", factorial(num))
