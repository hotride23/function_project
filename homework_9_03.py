def main():
    pass


def filter_to_odd(func):
    def do_filter():
        input_numbers = func()
        odd_numbers = [i for i in input_numbers if i % 2 == 0]
        print(odd_numbers)
    return do_filter


@filter_to_odd
def random_func():
    user_num = [1, 2, 3, 4, 5, 6]
    print(user_num)
    return user_num


random_func()


if __name__ == '__main__':
    main()
