with open('class_scores.txt', 'r', encoding='utf-8') as file, open('new_scores.txt', 'w', encoding='utf-8') as file_2:
    for line in file.readlines():
        val, num = line.split()
        print(val, (int(num) + 5) if (int(num) + 5) <= 100 else 100, file=file_2)
