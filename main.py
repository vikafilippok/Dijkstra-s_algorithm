import numpy as np

file = open("job_Var3.out", "w")

def dejkstra(matrix, start, n):
    distances = [np.inf] * n
    previous = [None] * n
    distances[start - 1] = 0
    visited = [False] * n

    for iteration in range(n-1):
        # Найти вершину с минимальным расстоянием из ещё не посещённых
        min_dist = np.inf
        for v in range(n):
            if not visited[v] and distances[v] < min_dist:
                min_dist = distances[v]
                u = v

        visited[u] = True

        # Обновить расстояние и предшествующую вершину для каждого соседа
        for v in range(n):
            if matrix[u][v] != '*' and not visited[v]:
                alt = (distances[u] + matrix[u][v])
                if alt < distances[v]:
                    distances[v] = alt
                    previous[v] = u + 1


        print(f"{iteration + 1}", file=file)
        print("D:", ' '.join(f"{int(d) if d != np.inf else '*'}" for d in distances), file=file)
        print("P:", ' '.join(f"{int(p) if p is not None else start}" for p in previous), file=file)

    return distances, previous

def convert_star(val):
    if val.decode('UTF-8') == '*':
        return np.nan  # Преобразует '*' в NaN
    return float(val)

inputFile = open("./data/job_Var3.in", "r")
list_info = inputFile.readline().split()
n = int(list_info[0])
start = int(list_info[2])

converters = {i: convert_star for i in range(n)}

matrix = np.loadtxt(inputFile, converters=converters) #there should be NO text in the file after the matrix



dejkstra(matrix, start, n)
