def func(*args):
    sum = 0
    max = 0
    for i in args:
        sum += i
        continue
    for i in args:
        if i == args[-1]:
            max = i
    return (sum, max)


print(func(1, 2, 3, 4))