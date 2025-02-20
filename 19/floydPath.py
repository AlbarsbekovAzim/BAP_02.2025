INF = float('inf')
def floyd_warshall(n, edges):
    global path
    path = [[[] for j in range(n)] for i in range(n)]
    dp = [[INF for j in range(n)] for i in range(n)]
    for i in range(n):
        dp[i][i] = 0
        path[i][i].append(i+1)
    for u, v, length in edges:
        u -= 1
        v -= 1
        # dp[u][v] = dp[v][u] = length # for non-directed edges graph
        dp[u][v] = length # for directed edges graph
        path[u][v].append(u + 1)
        path[u][v].append(v + 1)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dp[i][j] > dp[i][k] + dp[k][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]
                    path[i][j] = path[i][k] + path[k][j][1:]
    return dp
n, m = map(int, input().split())
edges = []
for i in range(m):
    u, v, length = map(int, input().split())
    edges.append((u, v, length))
path = []
dp = floyd_warshall(n, edges)
print('Floyd matrix:')
# resultmax = -INF
for row in dp:
    print(" ".join(map(str, row)))
    # resultmax = max(row) if max(row) > resultmax else resultmax
# print('result(max) is:', resultmax)
print('path:')
for row in path:
    print(" ".join(map(str, row)))
# print(path)