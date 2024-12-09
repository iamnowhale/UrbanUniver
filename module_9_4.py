# 1
first = 'Мама мыла раму'
second = 'Рамена мало было'

a = list(map(lambda x, y: x == y, first, second))
print(a)


# 2
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w') as file:
            for data in data_set:
                file.write(str(data) + '\n')

    return write_everything


writer_1 = get_advanced_writer('example1.txt')
writer_2 = get_advanced_writer('example2.txt')
writer_3 = get_advanced_writer('exampl3.txt')
writer_1('Это строчка', 123)
writer_2('Это строчка', {'a': 2})
writer_3('Это строчка', True)

# 3
import random


class MysticBall:
    def __init__(self, *words):
        self.words = list(words)

    def __call__(self):
        return random.choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())