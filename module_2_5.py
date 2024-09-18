def get_matrix(n: int, m: int, value):
    matrix = []

    for row in range(n):
        matrix.append([])

        for column in range(m):
            matrix[row].append(value)

    return matrix

result1 = get_matrix(2, 2, 10)
print(result1)