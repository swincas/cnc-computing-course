# good code example
def factorial(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# bad code example
def bad_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result