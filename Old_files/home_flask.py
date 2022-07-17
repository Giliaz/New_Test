import re
import random
import string
import csv

# password = []
# for _ in range(random.randrange(2, 5)):
#     password.append((string.ascii_uppercase)[random.randrange(len(string.ascii_uppercase))])
#     password.append((string.ascii_lowercase)[random.randrange(len(string.ascii_lowercase))])
# for _ in range(random.randrange(3, 5)):
#     password.append((string.digits)[random.randrange(len(string.digits))])
#     password.append((string.punctuation)[random.randrange(len(string.punctuation))])
# random.shuffle(password)
# pas = ''.join(password)
# print(f"Password lenght {len(password)} symb.: {(''.join(password))}")
#
# if re.match(r'[0-9a-zA-Z!"#$%&(){}\'*+,-./\\:;<>=?@\[\]^_`|~]{10,}', pas) :
#     print("True")
# if re.match(r'(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[!"#$%&(){}\'*+,-./\\:;<>=?@\[\]^_`|~])', pas):
#     print ("True")
# else:
#     print ("False")

num = random.randrange(10, 21)
password = random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation, k=num)
print (f"Password lenght {len(password)} symb.: {(''.join(password))}")

# откріваем файл csv
with open("hw.csv", newline='') as file:
    reader = csv.DictReader(file, delimiter=',')
    count = 0
    height = weight = 0.0
    for row in reader:
        height += float(row[' Height(Inches)'])
        weight += float(row[' Weight(Pounds)'])
        count += 1
    average_height = round((height/count), 2)
    average_weight = round((weight/count), 2)
    print (f'average_height = {average_height}, average_weight = {average_weight}')


