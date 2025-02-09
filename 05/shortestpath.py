graph = []
prev = []
maxint = float('inf')
d = int(input('count of dots: '))
for i in range(d):
    addg = []
    for j in range(d):
        addg.append(maxint)
    graph.append(addg)
    prev.append(maxint)
for i in range(d):
    addc = list(map(int, input(str(i+1) + "'th dot connected to: ").split()))
    addw = list(map(int, input('distances of roads below: ').split()))
    for j in range(len(addc)):
        graph[i][addc[j]-1] = addw[j]
        graph[addc[j]-1][i] = addw[j]
for i in graph:
    print(i)


# graph = [
#     [maxint, 1, 1, maxint, maxint, maxint],
#     [1, maxint, maxint, 1, maxint, maxint],
#     [1, maxint, maxint, 4, 1, maxint],
#     [maxint, 1, 4, maxint, maxint, 2],
#     [maxint, maxint, 1, maxint, maxint, 4],
#     [maxint, maxint, maxint, 2, 4, maxint]
# ]

# graph = [
#     [maxint, 1, maxint, 2],
#     [1, maxint, 1, maxint],
#     [maxint, 1, maxint, 1],
#     [2, maxint, 1, maxint]
# ]

start = int(input('from which dot we start: '))
end = int(input('on which dot we end: '))
locked = set([])
def main(ondot, plus):
    locked.add(ondot)
    if ondot == end:
        print(plus)
    else:
        for i in range(d):
            # print(graph[ondot-1][i], prev[i])
            prev[i] = graph[ondot-1][i] + plus if graph[ondot-1][i] + plus < prev[i] else prev[i]
        # print(prev)
        min_cost = min([x for i, x in enumerate(prev) if x != 0 and i+1 not in locked])
        ind = [x for x, num in enumerate(prev) if num == min_cost and x+1 not in locked]
        # print(ondot)
        # print(min_cost)
        # print(ind[0] + 1)
        # for x, num in enumerate(graph[ondot-1]):
        #     print(num + plus == min_cost)
        #     print(x+1 not in locked)
        main(ind[0]+1, min_cost)
main(start, 0)
