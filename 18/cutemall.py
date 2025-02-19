v = int(input())
graph = {}
isproblem = {}
cancut = 0
for i in range(1, v+1):
    graph[i] = []
for i in range(v-1):
    f, t = map(int, input().split())
    graph[f].append(t)
    graph[t].append(f)
def main(cur, parent):
    # print('cur is', cur)
    global cancut
    if v % 2 == 0:
        if len(graph[cur]) == 1:
            isproblem[cur] = 1
            if graph[cur][0] != parent:
                main(graph[cur][0], cur)
        elif len(graph[cur]) == 2:
            if graph[cur][0] != parent:
                main(graph[cur][0], cur)
            if graph[cur][1] != parent:
                main(graph[cur][1], cur)
            # print(graph)
            # print(isproblem)
            if (isproblem.get(graph[cur][0], False) and graph[cur][1] == parent) or (isproblem.get(graph[cur][1], False) and graph[cur][0] == parent):
                isproblem[cur] = 0
            elif isproblem.get(graph[cur][0], -2) == parent or isproblem.get(graph[cur][1], -2) == parent:
                if not isproblem[graph[cur][0]] and isproblem[graph[cur][1]] == parent:
                    cancut+=1
                if not isproblem[graph[cur][1]] and isproblem[graph[cur][0]] == parent:
                    cancut+=1
            else:
                cancut+=1
                isproblem[cur] = 1
        else:
            if graph[cur][0] != parent:
                main(graph[cur][0], cur)
            if graph[cur][1] != parent:
                main(graph[cur][1], cur)
            if graph[cur][2] != parent:
                main(graph[cur][2], cur)
            timed = [x for x in graph[cur] if x != parent]
            amountofp = 0
            for i in timed:
                if isproblem[i]:
                    amountofp+=1
            if len(timed) == 3 and amountofp == 1:
                cancut+=2
            elif amountofp == 1:
                cancut+=1
                isproblem[cur] = 0
    else:
        cancut = -1
        return

main(1, -1)
print(cancut)