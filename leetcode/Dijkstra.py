import sys
import numpy as np

n = 5
edges = [[1, 2, 3], [1, 3, 3], [2, 3, 1], [1, 4, 2], [5, 2, 2], [3, 5, 1], [5, 4, 10]]

graph = np.zeros((n, n))

for ed in edges:
    graph[ed[0] - 1, ed[1] - 1] = ed[2]
    graph[ed[1] - 1, ed[0] - 1] = ed[2]

print(graph)

distance = np.inf * np.ones(n)

print(distance)

before = -1 * np.ones(n)

print(before)

visited = [False] * n
print(visited)

start = 4
distance[start] = 0

for _ in range(n):
    min_distance = np.inf
    min_index = -1

    for i in range(n):
        if not visited[i] and distance[i] < min_distance:
            min_distance = distance[i]
            min_index = i

    if min_index == -1:
        break

    visited[min_index] = True

    for i in range(n):
        if not visited[i] and graph[min_index, i] != 0:  # 未访问过且可达
            new_distance = graph[min_index, i] + distance[min_index]
            if new_distance < distance[i]:
                distance[i] = new_distance
                before[i] = min_index

print(distance)
print(before)

end = 3

road = list()
road.append(end)
while end != start:
    road.append(int(before[end]))
    end = int(before[end])

road = road[::-1]
print('The Min Distance Road:')
for ro in road:
    print(str(ro), end='')
    if ro != road[-1]:
        print('->', end='')


