import csv
with open("Crimes.csv", newline='') as file:
    reader = csv.DictReader(file, delimiter=',')
    dict = {}
    for row in reader:
        if row['Date'][6:10] == '2015':
            dict[row['Primary Type']] = dict.get(row['Primary Type'], 0) + 1
print(*sorted(dict.items(), key=lambda x: x[1],reverse=True)[0])

with open("Crimes.csv", encoding="utf-8") as cry_raw:
    read_cry_2015 = csv.reader(cry_raw, delimiter=",")
    crimes = [pry[5] for pry in read_cry_2015 if "2015" in pry[2]]
print(max(crimes, key=crimes.count))