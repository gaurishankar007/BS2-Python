# Factorial of a number
# Iterative

# Algorithm
# 1. Start
# 2. Declare two integers a and b
# 3. Input a value on a and set value of b 1
# 4. Use for loop of range from 2 to that number
# 5. Set another value to b inside for loop which is the result of the multiplication of b and the values from for loop
# 6. print b outside of the for loop
# 7. Stop
# Implementation
a = int(input("Enter a number: "))
b = 1
for i in range(2, a + 1):
    b = b * i
print(b)

# Recursive

# Algorithm
# 1. Start
# 2. Stop

# Implementation


def factorial(a):
    if a == 1 or 0:
        return 1
    else:
        return a * factorial(a-1)


p = int(input("Enter a number: "))
if p < 0:
    print("The factorial of negative number doesn't exist.")
print(factorial(p))


# Fibonacci Series up to nth term
# Iterative

# Algorithm
# 1. Start
# 2.
# 3.
# 4.
# 5.
# 6.
# 7. Stop
# Implementation
a = int(input("Enter a number: "))
b = 0
if a == 0 or a == 1:
    print(a)
else:
    for i in range(a):
        b = b + i
print(b)

# Recursive

# Algorithm
# 1. Start
# 2. Stop

# Implementation


def fibonacci(a):
    if a == 1 or a == 0:
        return a
    else:
        return fibonacci(a - 1) + fibonacci(a - 2)


p = int(input("Enter a nth term: "))
if p < 0:
    print("Enter a positive number.")
else:
    print(f"The required fibonacci series:")
    for i in range(p):
        print(fibonacci(i))



