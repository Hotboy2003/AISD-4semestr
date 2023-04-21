# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 17:17:33 2023

@author: admin
"""
"""
Алгоритм нахождения эйлерова цикла в неориентированном графе заключается в следующем:
1. Проверяем граф на наличие эйлерова цикла. Это возможно только если степени всех 
вершин графа четные.
2. Находим произвольную вершину и запускаем DFS, в каждой вершине отмечая пройденные ребра 
и вершины.
3. Если мы дошли до вершины, из которой мы начали обход, и прошли все ребра, 
то граф содержит эйлеров цикл.
4. Если граф не содержит эйлеров цикл, то берем вершину из стека, у которой еще остались
непройденные ребра, и повторяем шаги 2-3, начиная с этой вершины.
5. В конце обхода, если список ребер, которые мы прошли, содержит все ребра графа, 
то граф содержит эйлеров цикл.
"""

input_file = 'input.txt'
output_file = 'output.txt'

"""
Для выполнения пункта 1 напишем функцию `check_eulerian_cycle()`, которая будет 
принимать на вход граф в виде матрицы смежности `graph`. Функция будет проверять, 
имеет ли граф эйлеров цикл, и возвращать булево значение `True` или `False`.
"""

def check_eulerian_cycle(graph):
    # проверяем, что степени всех вершин четные
    for i in range(len(graph)):
        degree = sum(graph[i])
        if degree % 2 != 0:
            return False
    return True

"""
Для выполнения пункта 2 и последующих создадим функцию `dfs()`, которая будет 
принимать на вход граф в виде матрицы смежности `graph`, номер вершины, с которой 
нужно начать обход `start_vertex` и список `path`, в который будут добавляться ребра, 
проходящие на пути обхода. В функции будем использовать булевый массив `visited`, 
который будет отмечать пройденные вершины и ребра.
"""

def dfs(graph, start_vertex, path, visited):
    visited[start_vertex] = True
    for v in range(len(graph)):
        if graph[start_vertex][v] != 0 and not visited[v]:
            path.append((start_vertex, v))
            dfs(graph, v, path, visited)

"""
Для выполнения пункта 4 создадим функцию `find_eulerian_cycle()`, которая будет 
принимать на вход граф в виде матрицы смежности `graph`. Функция будет искать эйлеров
цикл в графе начиная с вершины номер `start_vertex`. Если цикла нет, то мы будем 
брать вершину из стека, у которой еще остались непройденные ребра.
"""

def find_eulerian_cycle(graph, start_vertex):
    path = []
    visited = [False] * len(graph)

    # запускаем обход из указанной вершины
    dfs(graph, start_vertex, path, visited)

    # если список ребер, которые мы прошли, содержит все ребра графа, то граф содержит эйлеров цикл
    if len(path) == sum(map(sum, graph)) // 2:
        return path

    # ищем другую вершину из стека, у которой еще остались непройденные ребра
    for i in range(len(path)):
        edge = path[i]
        if not visited[edge[0]] or not visited[edge[1]]:
            # удаляем ребро из списка path и запускаем обход из новой вершины
            path.pop(i)
            visited = [False] * len(graph)
            dfs(graph, edge[0], path, visited)
            return find_eulerian_cycle(graph, edge[0])

"""
Для выполнения пункта 5 создадим функцию `convert_path_to_string()`, которая 
будет принимать на вход список ребер `path` и преобразовывать его в строку в 
формате "start_vertex-end_vertex".
"""

def convert_path_to_string(path):
    result = ''
    for edge in path:
        result += f'{edge[0]}-{edge[1]} '
    return result

with open(input_file) as f:
    n = int(f.readline()) # пустую строку можно проигнорировать
    graph = [list(map(int, line.split())) for line in f]

has_eulerian_cycle = check_eulerian_cycle(graph)

if not has_eulerian_cycle:
    with open(output_file, 'w') as f:
        f.write("Graph doesn't have an Eulerian cycle")
else:
    cycle = find_eulerian_cycle(graph, 0) # можно начинать обход из любой вершины, в данном случае выбрана вершина № 0
    cycle_str = convert_path_to_string(cycle)
    with open(output_file, 'w') as f:
        f.write(cycle_str)