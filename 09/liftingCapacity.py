# graph = []
prev = []
minint = float('-inf')
maxint = float('inf')
d = int(input('count of dots: '))
for i in range(d):
    # addg = []
    # for j in range(d):
    #     addg.append(minint)
    # graph.append(addg)
    prev.append(minint)
# for i in range(d):
#     addc = list(map(int, input(str(i+1) + "'th dot connected to: ").split()))
#     addw = list(map(int, input('distances of roads below: ').split()))
#     for j in range(len(addc)):
#         graph[i][addc[j]-1] = addw[j]
#         graph[addc[j]-1][i] = addw[j]
# for i in graph:
#     print(i)


graph = [
    [minint, 3, minint, 6, 4, minint],
    # [3, minint, minint, minint, minint, 1],
    # [minint, minint, minint, 2, minint, 5],
    [3, minint, 8, minint, minint, 1],
    [minint, 8, minint, 2, minint, 5],
    [6, minint, 2, minint, 3, minint],
    [4, minint, minint, 3, minint, 7],
    [minint, 1, 5, minint, 7, minint]
]


# graph = [
#     [minint, 1, 1, minint, minint, minint],
#     [1, minint, minint, 1, minint, minint],
#     [1, minint, minint, 4, 1, minint],
#     [minint, 1, 4, minint, minint, 2],
#     [minint, minint, 1, minint, minint, 4],
#     [minint, minint, minint, 2, 4, minint]
# ]

# graph = [
#     [minint, 1, minint, 2],
#     [1, minint, 1, minint],
#     [minint, 1, minint, 1],
#     [2, minint, 1, minint]
# ]
minmax = maxint
start = int(input('from which dot we start: '))
end = int(input('on which dot we end: '))
locked = set([])
def main(ondot):
    global minmax
    locked.add(ondot)
    if ondot == end:
        print(minmax)
    else:
        for i in range(d):
            # print(graph[ondot-1][i], prev[i])
            prev[i] = graph[ondot-1][i] if graph[ondot-1][i] > prev[i] else prev[i]
        # print(prev)
        max_cost = max([x for i, x in enumerate(prev) if x != 0 and i+1 not in locked])
        ind = [x for x, num in enumerate(prev) if num == max_cost and x+1 not in locked]
        # locked.add(max_cost)
        minmax = max_cost if max_cost < minmax else minmax
        # print(ondot)
        # print(max_cost)
        # print(ind[0] + 1)
        # for x, num in enumerate(graph[ondot-1]):
        #     print(num == min_cost)
        #     print(x+1 not in locked)
        main(ind[0]+1)
main(start)
# main(4)
# main(5)
