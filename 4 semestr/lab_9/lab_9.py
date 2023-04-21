# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 17:03:34 2023

@author: admin
"""
"""
Для решения данной задачи необходимо выполнить следующие шаги:
1. Считать данные из файла с помощью модуля built-in Python `open()`.
2. Написать функцию `bellman_ford()`, которая будет принимать на вход граф в 
виде матрицы смежности и вершину, из которой нужно найти кратчайшие пути.
3. В функции `bellman_ford()` реализовать алгоритм Беллмана-Форда.
4. Записать результаты в итоговый файл с помощью `open()`.
"""

input_file = 'input.txt'
output_file = 'output.txt'

"""
Для выполнения пункта 2 создадим функцию `bellman_ford()`, которая будет 
принимать на вход граф в виде матрицы смежности `graph` и вершину, из которой 
нужно найти кратчайшие пути `start_vertex`. В данной функции будем использовать 
списки `distances` и `predecessors`, в которых будут храниться расстояния 
до каждой вершины и предшественники на кратчайшем пути соответственно.
"""

def bellman_ford(graph, start_vertex):
    # инициализация списков
    distances = [float('inf')] * len(graph)
    predecessors = [None] * len(graph)

    distances[start_vertex] = 0  # расстояние до стартовой вершины равно 0

    # проходимся по всем ребрам графа
    for _ in range(len(graph)-1):
        for u in range(len(graph)):
            for v in range(len(graph)):
                if graph[u][v] != 0 and distances[u] + graph[u][v] < distances[v]:
                    distances[v] = distances[u] + graph[u][v]
                    predecessors[v] = u

    return distances, predecessors

"""
Для выполнения пункта 3 вызовем функцию `bellman_ford()` с параметрами - графом 
в виде матрицы смежности и номером вершины, из которой мы ищем кратчайшие пути.
"""

# считываем граф из файла
with open(input_file, 'r') as f:
    graph = []
    for line in f:
        graph.append(list(map(int, line.strip().split())))

# запускаем алгоритм Беллмана-Форда
start_vertex = 0
distances, predecessors = bellman_ford(graph, start_vertex)

"""
Для выполнения пункта 4 создадим переменную `result`, в которой будем хранить 
результаты. Результаты будем записывать в выходной файл. Формат вывода: 
номер вершины и ее расстояние до стартовой вершины.
"""

result = ''
for i in range(len(distances)):
    result += f'{i}: {distances[i]}\n'

with open(output_file, 'w') as f:
    f.write(result)

