with open("test.txt") as test, open('test_copy.txt', 'w') as test_copy:
    # new = []
    # for line in test:
    #    new.append(line.rstrip())
    # for i in range(len(new) - 1, -1, -1):
    #    test_copy.write(new[i]+'\n')
    for lines in reversed(test.readlines()):
        test_copy.write(lines)
