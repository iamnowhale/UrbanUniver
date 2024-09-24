def func(num) -> str:
  s = ''
  for i in range(1, num):
   for j in range(i, num):
     if num % (i + j) == 0 and i != j:
       s += str(i) + str(j)

  return s

def prnt(number):
  print(f'Для числа {number} - {func(number)}')

for i in range(3, 21):
  prnt(i)
