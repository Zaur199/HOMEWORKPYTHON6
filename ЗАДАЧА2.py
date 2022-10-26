# Задача 1. Напишите программу, удаляющую из текста все слова содержащие "абв".

from ntpath import join


text = 'Напишите прогабврамму, удабваляющую из текста все слова, содержащие'

text = list(filter(lambda x: 'абв' not in x, text.split()))
text1 = " ".join(text)

print(text1)