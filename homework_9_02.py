def main():
    pass

key_new = lambda **kwargs: {key*2 : value for key, value in kwargs.items()}
print(key_new(abc=2, bbb=3, c=1))

if __name__ == '__main__':
    main()
