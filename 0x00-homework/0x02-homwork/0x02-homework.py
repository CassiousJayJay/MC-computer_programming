def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
n = 5
result = factorial(n)
print("The factorial of ", n, "is", result)
