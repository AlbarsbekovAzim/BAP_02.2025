# import sys

INF = float('inf')

def floyd_warshall(n, edges):
    # Инициализация матрицы расстояний
    dp = [[INF] * n for i in range(n)]

    for i in range(n):
        dp[i][i] = 0  # Расстояние от вершины до самой себя равно 0

    # Заполнение матрицы на основе входных данных
    for u, v, length in edges:
        u -= 1  # Приведение индекса к 0-based
        v -= 1
        dp[u][v] = dp[v][u] = length

    # Алгоритм Флойда-Уоршелла
    for k in range(n):  # Текущая вершина, используемая для улучшения
        for i in range(n):
            for j in range(n):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    return dp

# Ввод данных
n, m = map(int, input().split())  # n - количество вершин, m - количество рёбер
edges = []

for i in range(m):
    u, v, length = map(int, input().split())
    edges.append((u, v, length))

# Вычисление кратчайших путей
dp = floyd_warshall(n, edges)

print('Floyd matrix:')
resultmax = -INF
# Вывод матрицы расстояний (опционально)
for row in dp:
    print(" ".join(map(str, row)))
    resultmax = max(row) if max(row) > resultmax else resultmax
print('result(max) is:', resultmax)