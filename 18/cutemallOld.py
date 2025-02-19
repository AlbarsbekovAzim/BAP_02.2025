v = int(input())
graph = {}
for i in range(1, v+1):
    graph[i] = set()
for i in range(v-1):
    u, v = map(int, input().split())
    graph[u].add(v)
    graph[v].add(u)
# print(graph)
isproblem = {}
cancut = 0
def main(cur, parent):
    if v % 2 == 0:
        return
    else:
        cancut = -1
        return