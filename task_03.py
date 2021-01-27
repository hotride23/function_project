def function(*args):
    result = 0
    for i in args:
        result +=i
        continue
    result *= len(args)
    return result
print(function(1, 2, 3, 4))