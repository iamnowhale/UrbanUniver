class WordsFinder:
  def __init__(self, *file_names):
      self.file_names = list(file_names)

  def get_all_words(self):
      all_words = {}
      for filename in self.file_names:
          with open(filename, 'r+') as file:
              text = file.read().lower()

              for i in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                  text = text.replace(i, '')

              words = text.split()
              all_words[filename] = words

      return all_words

  def find(self, word):
      word = word.lower()
      all_words = self.get_all_words()
      result = {}
      for filename, words_list in all_words.items():
          if word in words_list:
              position = words_list.index(word) + 1
              result[filename] = position
      return result

  def count(self, word):
      words_count = self.get_all_words()
      counted_words = {}
      for filename, words_list in words_count.items():
          counted_words[filename] = words_list.count(word.lower())
      return counted_words


finder2 = WordsFinder('test.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего