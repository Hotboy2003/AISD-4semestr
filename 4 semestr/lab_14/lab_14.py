# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 18:56:50 2023

@author: admin
"""
"""
Алгоритм Рабина-Карпа (Rabin-Karp) – это алгоритм поиска подстроки, основанный на
использовании хеш-функций. Суть алгоритма заключается в следующем: сначала вычисляется
хеш-функция для образца и для каждой возможной подстроки в исходной строке. 
Если хэш-функции для образца и текущей подстроки совпадают, то выполняется дополнительная
проверка на полное совпадение. 

Одно из основных преимуществ алгоритма Рабина-Карпа заключается в скорости его работы: 
алгоритм работает за лучшее время O(n), где n — длина исходной строки. 
"""
# функция для считывания строки из файла
def read_file(filename):
    with open(filename, "r") as f:
        return f.read()

"""
Для каждого символа строки сначала вычисляется его код в таблице ASCII с помощью 
функции `ord`, затем символ умножается на степень числа 31 (параметр `p`) с номером
текущего символа и суммируется с предыдущими значениями. Таким образом, получается 
хеш-функция для строки.
"""
# функция для вычисления хеш-функции
def hash_func(s):
    p, h = 31, 0
    for i in range(len(s)):
        h = h * p + ord(s[i])
    return h

"""
Хеш-функция используется в алгоритме Рабина-Карпа для быстрого сравнения образца 
и подстрок в исходной строке. Сначала вычисляются хеш-функции для образца и для 
первой подстроки в исходной строке. Затем проходим по каждой возможной подстроке 
в исходной строке и вычисляем ее хеш-функцию. Если хеш-функции совпадают, 
то выполняется дополнительная проверка на полное совпадение. Если полное совпадение 
найдено, то возвращается индекс начала подстроки в исходной строке. Если подстрока 
не найдена, возвращается -1.
"""

# функция для реализации алгоритма Рабина-Карпа
def rabin_karp_search(text, pattern):
    # определяем длину строки и образца
    n, m = len(text), len(pattern)
    # вычисляем хеш-функцию для образца и первой подстроки в исходной строке
    p_hash, t_hash = hash_func(pattern), hash_func(text[:m])
    # проходим по каждой возможной подстроке в исходной строке, начиная с позиции m
    for i in range(n - m + 1):
        # если хеш-функции образца и текущей подстроки совпадают
        if p_hash == t_hash:
            # выполняем проверку на полное совпадение
            if text[i:i+m] == pattern:
                return i
        # пересчитываем хеш-функцию для следующей подстроки
        if i < n - m:
            t_hash = (t_hash - ord(text[i]) * pow(31, m-1)) * 31 + ord(text[i+m])
    return -1

filename = "input.txt"

# основная функция программы
def main():
    text = read_file(filename)
    # вводим образец
    pattern = input("Введите образец для поиска: ")
    # ищем образец в строке
    index = rabin_karp_search(text, pattern)
    if index == -1:
        print("Образец не найден")
    else:
        print(f"Образец найден в позиции {index}")

# вызываем основную функцию
if __name__ == "__main__":
    main()
