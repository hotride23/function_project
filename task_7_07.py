def even(*args):
    for i in args:
        if len(i) % 2 == 0:
            print(i)
print(even("hello", "welcome", "hi", "good", "bad", "4444"))
