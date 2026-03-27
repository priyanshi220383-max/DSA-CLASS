# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)

# n = int(input("Enter a number: "))

# print("Factorial of", n, "is:", factorial(n))
# for fibonacci series
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter number: "))

print("Fibonacci Series:")
for i in range(n):
    print(fibonacci(i), end=" ")
print()