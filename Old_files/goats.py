with open('goats.txt', 'r', encoding='utf-8') as file, open('answer.txt', 'w', encoding='utf-8') as file_2:
    result = {}
    for line in file.readlines():
        if line.strip() == 'COLOURS' or line.strip() == 'GOATS':
            file.readline()
        else:
            result[line.strip()] = result.get(line.strip(), -1) + 1
    summ = sum(result.values())
    for key, values in sorted(result.items()):
        if summ * 0.07 < values:
            print(key, file=file_2)
