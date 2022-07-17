with open('logfile.txt', 'r', encoding='utf-8') as file, open('output_2.txt', 'w', encoding='utf-8') as file_1:
    sp = [line.strip().split(', ') for line in file.readlines()]
    for name, start, stop in sp:
        hours_start, minutes_start = start.split(':')
        hours_stop, minutes_stop = stop.split(':')
        time = (int(hours_stop) * 60 + int(minutes_stop)) - (int(hours_start) * 60 + int(minutes_start))
        if time >= 60:
            print(name, file=file_1)
