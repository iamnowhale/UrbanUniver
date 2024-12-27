import threading
from time import sleep, time

def write_words(word_count, file_name):
  result = None
  with open (file_name, 'w') as file:
      for i in range(word_count):
          result = file.write(f'Какое-то слово № {i + 1}\n')
          sleep(0.1)
      print(f'Завершилась запись в файл {file_name}')

  return result

start_time = time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_time = time()
print(f'Работа потоков {end_time - start_time: 4f}')


threads = [
    threading.Thread(target= write_words, args=(10, 'example5.txt')),
    threading.Thread(target= write_words, args=(30, 'example6.txt')),
    threading.Thread(target= write_words, args=(200, 'example7.txt')),
    threading.Thread(target= write_words, args=(100, 'example8.txt'))
]


start_time = time()

for i in threads:
  i.start()

for i in threads:
  i.join()

end_time = time()

print(f'Работа потоков {end_time - start_time: 4f}')

