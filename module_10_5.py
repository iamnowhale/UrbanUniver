import time
from multiprocessing import Pool

# Функция для считывания данных из файла
def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())
    return all_data

# Список файлов для обработки
file_names = [f"Files/file {i}.txt" for i in range(1, 5)]

def linear_execution():
    start_time = time.time()
    for file_name in file_names:
        read_info(file_name)
    end_time = time.time()
    print(f"Линейное выполнение заняло: {end_time - start_time:.4f} секунд")

def multiprocess_execution():
    start_time = time.time()
    with Pool() as pool:  # По умолчанию Pool использует количество ядер процессора
        pool.map(read_info, file_names)
    end_time = time.time()
    print(f"Многопроцессное выполнение заняло: {end_time - start_time:.4f} секунд")

# Запуск выполнения
if __name__ == "__main__":

    linear_execution()  # Линейный подход
    # multiprocess_execution()  # Многопроцессный подход