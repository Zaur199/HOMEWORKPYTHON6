# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

lst = [5, 8, 6, 5, 3, 8, 1, 0, 6]
count = 0
data = [x for x in range(len(lst))]
res = list(filter(lambda x: lst.count(x) == 1, data))
res.sort(reverse = True)
print(f'{lst} => {res}')