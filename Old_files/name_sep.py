def greet(name, *args):
    # str = (f'Hello, {name}')
    # if len(args) > 0:
    #     str += ' and '+ ' and '.join(args)
    # str += '!'
    str = f'Hello, {" and ".join((name,) + args)}!'
    return str

print(greet('rrrr'))