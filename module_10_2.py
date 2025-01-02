import threading
import time

# Общее количество врагов для всех рыцарей
enemies = 100
lock = threading.Lock()

class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        global enemies
        days = 0
        print(f"{self.name}, на нас напали!")
        while True:
            with lock:
                if enemies <= 0:
                    break
                # Рыцарь сражается, уменьшая количество врагов
                enemies -= self.power
                if enemies < 0:
                    enemies = 0
            days += 1
            time.sleep(1)  # Один день сражения (задержка в 1 секунду)
            print(f"{self.name} сражается {days} день(дня)..., осталось {enemies} воинов.")

        print(f"{self.name} одержал победу спустя {days} дней(дня)!")


# Создание рыцарей
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков
first_knight.start()
second_knight.start()

# Ожидание завершения потоков
first_knight.join()
second_knight.join()

# Вывод строки об окончании сражений
print("Все битвы закончились!")