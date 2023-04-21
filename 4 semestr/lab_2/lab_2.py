"""
выбирается стартовая вершина, от которой будет выполняться поиск кратчайших путей, инициализируется очередь `q`, 
которая будет использоваться для обхода графа в ширину, и инициализируются массивы `visited` и `distances`. 
Массив `visited` будет использоваться для отслеживания того, была ли вершина уже посещена во время обхода BFS, 
а массив `distances` будет использоваться для отслеживания кратчайшего расстояния от стартовой вершины до каждой другой вершины.

Далее запускается алгоритм BFS. Сначала из очереди `q` извлекается стартовая вершина и помечается как посещенная. 
Затем для каждой соседней вершины, еще не посещенной и имеющей ребро с текущей вершиной (то есть со значением в матрице смежности > 0), 
устанавливается флаг посещенности и вычисляется расстояние как расстояние текущей вершины + вес ребра. Результат записывается в массив `distances`.
 Если вершина успешно обработана, то он добавляется в очередь `q` для будущего обхода, до тех пор пока очередь `q` не станет пустой.
"""
from queue import Queue

with open('graph.txt', 'r') as f:
    matrix = [list(map(int, line.strip().split())) for line in f]

# определяем стартовую вершину
start_node = 0

# создаем очередь
q = Queue()
q.put(start_node)

# создаем два массива
visited = [False] * len(matrix)
visited[start_node] = True
distances = [float('inf')] * len(matrix)
distances[start_node] = 0

# BFS 
while not q.empty():
    node = q.get()
    for neighbor, weight in enumerate(matrix[node]):
        if weight > 0 and not visited[neighbor]:
            visited[neighbor] = True
            q.put(neighbor)
            distances[neighbor] = distances[node] + weight


with open('result.txt', 'w') as f:
    for i, distance in enumerate(distances):
        f.write(f' Кратчайший путь до узла {i}: {distance}\n')