v = int(input())
graph = [[] for i in range(v+1)]
cancut = 0
for i in range(v-1):
    f, t = map(int, input().split())
    graph[f].append(t)
    graph[t].append(f)

def main(start):
    global cancut
    stack = [(start, -1)]
    subtree_size = {i: 1 for i in range(1, v + 1)}
    order = []

    while stack:
        node, parent = stack.pop()
        order.append((node, parent))
        for neighbor in graph[node]:
            if neighbor != parent:
                stack.append((neighbor, node))

    for node, parent in reversed(order):
        if parent != -1:
            subtree_size[parent] += subtree_size[node]
            if subtree_size[node] % 2 == 0:
                cancut += 1

if v % 2 == 1:
    print(-1)
else:
    main(1)
    print(cancut)