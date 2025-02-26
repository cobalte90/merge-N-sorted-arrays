list_for_sort = [] # Список для хранения результата алгоритма

n = int(input('Введите количество массивов для слияния: '))

for i in range(n):
    list_for_sort.append(list(map(lambda x : int(x), input(f'Введите через пробел массив номер {i+1}: ').split())))

# Функция для слияния двух массивов
def mergesort(l1, l2):
    # Обработка случаев, когда один из массивов пуст
    if not l1:
        return l2
    if not l2:
        return l1

    res = [] # Результат слияния двух массивов
    i1, i2 = 0, 0 # Индексы для итерации по двум массивам (указатели)

    while i1 + i2 < len(l1) + len(l2):
        if (i1 != len(l1)) and (i2==len(l2) or l1[i1] <= l2[i2]):
            res.append(l1[i1])
            i1 += 1
        else:
            res.append(l2[i2])
            i2 += 1

    return res

out = [] # Список для хранения результата алгоритма
# Последовательно применяем функцию слияния к массивам ( out и 1-й, out и 2-й и так далее)
# При этом out каждый раз обновляется и содержит результат слияния предыдущих массивов
for i in range(len(list_for_sort)):
    out = mergesort(out, list_for_sort[i])

print('Результат слияния массивов:',*out, sep=' ')
