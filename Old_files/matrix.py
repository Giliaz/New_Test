def matrix(rows=1, cols=None, value=0):
    matrix = [[value]*rows if cols is None else [value]*cols for _ in range(rows)]
    if cols == None:
        cols = rows
    # matrix = [[ value for _ in range(cols)] for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            print(matrix[r][c], end=' ')
        print()

matrix(5,3,6)