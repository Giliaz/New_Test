n = int(input())
files = [input() for _ in range(n)]
with open('output_1.txt', 'w', encoding='utf-8') as file:
    for file_read in files:
        with open(file_read, 'r', encoding='utf-8') as file_1:
            for line in file_1.readlines():
                file.write(line)