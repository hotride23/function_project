def factorial(a):
    i = 1
    sum = 1
    while i <= a:
        sum *= i
        i += 1
    return sum
print(factorial(5))