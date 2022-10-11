# Задача 1:
#
# Напишите программу, удаляющую из текста все слова, 
# содержащие ""абв""

text = input('Введите текст:\n')

list_word = text.split()
list_index = []

for i in list_word:
    for k in i:
        if k == 'а' or k == 'б' or k == 'в':
            list_index.append(list_word.index(i))
            break

for i in list_index[::-1]:
    list_word.pop(i)

list_word =' '.join(list_word)
print(list_word)