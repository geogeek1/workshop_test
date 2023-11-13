# Basic Calculator

def add(x, y):
    return x + y

def power(x, n):
    # comments
    return some_super_fast_power(x, n)

def subtract(x, y):
    return x - y

def multiply(x, y):
    # comment
    return x * y

def divide(x, y):
    if y == 0:
        return "Division by zero is not allowed!"
    return x / y

if __name__ == "__main__":
    print("Welcome to the calculator!")
    print("Addition: 3 + 4 =", add(3, 4))
    print("Subtraction: 5 - 2 =", subtract(5, 2))
    print("Multiplication: 6 * 3 =", multiply(6, 3))
    print("Division: 10 / 2 =", divide(10, 2))
