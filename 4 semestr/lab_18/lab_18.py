"""
Задача о суммах подмножеств заключается в том, чтобы найти все подмножества 
множества чисел и их суммы.

Жадный алгоритм может использоваться для решения этой задачи. Идея заключается
в том, чтобы начинать с пустого множества и итеративно добавлять числа из 
исходного множества. После добавления каждого числа мы создаем новые подмножества,
которые включают это число, и объединяем их со всеми предыдущими подмножествами.
Этот процесс повторяется до тех пор, пока все числа из исходного множества не
будут добавлены.
"""

"""
функция subset_sums, которая принимает множество чисел и возвращает список всех
подмножеств и их сумм.
"""
def subset_sums(numbers):
    # Создаем список для хранения всех подмножеств и их сумм
    subsets = [set()]
    
    # Итеративно добавляем числа из исходного множества
    for number in numbers:
        # Создаем новые подмножества, которые включают это число, и объединяем
        #их со всеми предыдущими подмножествами
        new_subsets = [{number} | subset for subset in subsets]
        # Добавляем новые подмножества в список всех подмножеств
        subsets += new_subsets
    
    # Возвращаем список всех подмножеств и их сумм в виде кортежей
    return [(subset, sum(subset)) for subset in subsets]

numbers = {1, 2, 3}
subsets = subset_sums(numbers)
for subset, subset_sum in subsets:
    print(f'{subset} = {subset_sum}')