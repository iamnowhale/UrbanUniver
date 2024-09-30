data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(*args):
    summa = 0

    for element in args:
        if isinstance(element, str):
            summa += len(element)
        if isinstance(element, (int, float)):
            summa += element
        if isinstance(element, (list, tuple, set)):
            summa += calculate_structure_sum(*element)
        if isinstance(element, dict):
            summa += calculate_structure_sum(*element.keys())
            summa += calculate_structure_sum(*element.values())

    return summa


print(calculate_structure_sum(data_structure))