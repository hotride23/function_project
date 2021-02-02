def main():
    pass

random_list = ['hello', 'good bye', 'have a nice day', 'welcome']
num_list = [i for i in range(len(random_list))]
result = list(map(lambda x, y: f'{x}: {y}', num_list, random_list))

print(result)

if __name__ == '__main__':
    main()
