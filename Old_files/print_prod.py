def print_products(*args):
    prod = [args[id] for id in range(len(args)) if type(args[id]) == str and args[id] != '']
    if len(prod):
        [print(f'{id + 1} {prod[id]}') for id in range(len(prod))]
    else:
        print('Нет продуктов')

print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
#print_products([4], {}, 1, 2, {'Beegeek'}, '')