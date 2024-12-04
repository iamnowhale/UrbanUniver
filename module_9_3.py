first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x) - len(y) for x, y in zip(first, second))
print(list(first_result))


min_length = min(len(first), len(second))

second_result = (len(first[i]) == len(second[i]) for i in range(min_length))
print(list(second_result))