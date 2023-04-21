# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 16:39:49 2023

@author: admin
"""


import sys #импортируем модуль для работы с файлами:

#создаем функцию, которая будет открывать файл с матрицей смежности и считывать данные из него:
#Эта функция открывает файл, читает его содержимое и возвращает матрицу смежности в виде двумерного списка.
def readGraph(filename):
    graph = []
    with open(filename) as f:
        for line in f:
            row = list(map(int, line.strip().split()))
            graph.append(row)
    return graph


filename = "graph.txt"
graph = readGraph(filename)

#Далее мы определяем функцию для поиска в глубину:

def dfs(graph, visited, start, component):
    visited[start] = True
    component.append(start)
    for i in range(len(graph)):
        if graph[start][i] == 1 and not visited[i]:
            dfs(graph, visited, i, component)
"""
Эта функция принимает матрицу смежности `graph`, список посещенных вершин `visited`,
стартовую вершину `start` и список для хранения компонент связности `component`.

Она начинает с посещения стартовой вершины, добавляет ее в текущую компоненту и рекурсивно
вызывает себя для всех соседних вершин, которые еще не были посещены.

Теперь мы можем определить функцию для поиска всех компонент связности в графе:
"""
def findComponents(graph):
    visited = [False] * len(graph)
    components = []
    for i in range(len(graph)):
        if not visited[i]:
            component = []
            dfs(graph, visited, i, component)
            components.append(component)
    return components
"""
Эта функция инициализирует список `visited`, который будет использоваться для отслеживания посещенных вершин, а затем
выполняет поиск 
в глубину для каждой не посещенной вершины.

Каждый компонент связности добавляется в список `components`, который затем возвращается в качестве результата.

Наконец, мы можем вызвать функцию `findComponents`, чтобы вычислить количество и состав всех компонент связности в графе:
"""

components = findComponents(graph)
with open('output.txt', 'w') as f:
    f.write(f"Number of components: {len(components)}\n\n")
    for i, component in enumerate(components):
        f.write(f"Component {i+1}: {component}\n")
    
#Мы используем `len(components)` для вывода количества компонент связности и затем перебираем все компоненты для их 
#дальнейшего вывода.