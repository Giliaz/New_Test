with open('test.txt') as file:
    print('Repeat after me:')
    for line in file:
        print(line.strip() + '!')