def single_root_words(root_word, *other_words):
  list_ = []
  for root in other_words:
    if root_word.lower() in root.lower() or root.lower() in root_word.lower():
      list_.append(root)
  return list_

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)