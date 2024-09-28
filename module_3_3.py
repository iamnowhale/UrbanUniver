def print_params(a = 1, b = 'строка', c = True):
  print(a, b, c)

print_params(2, 'СТРОКА', False)
print_params(2, 'СТРОКА')
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [5, 'Hello', [2,4]]
values_dict = {'a' : 1, 'b' : 'строка', 'c' : True}
values_list2 = [3.5, 'Hello, world!']

print_params(*values_list)
print_params(**values_dict)
print_params(*values_list2, 42)