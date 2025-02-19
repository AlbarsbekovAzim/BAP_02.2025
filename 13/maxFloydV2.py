INF = float('inf')
def floyd_warshall(n, edges):
    dp = [[INF] * n for i in range(n)]
    for i in range(n):
        dp[i][i] = 0
    for u, v, length in edges:
        u -= 1
        v -= 1
        # dp[u][v] = dp[v][u] = length
        dp[u][v] = length
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    return dp
n, m = map(int, input().split())
edges = []
for i in range(m):
    u, v, length = map(int, input().split())
    edges.append((u, v, length))
dp = floyd_warshall(n, edges)
print('Floyd matrix:')
resultmax = -INF
for row in dp:
    print(" ".join(map(str, row)))
    resultmax = max(row) if max(row) > resultmax else resultmax
print('result(max) is:', resultmax)