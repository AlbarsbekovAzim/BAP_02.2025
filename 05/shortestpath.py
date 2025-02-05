graph = []
d = int(input('count of dots: '))
for i in range(d):
    addg = []
    for j in range(d):
        addg.append(0)
    graph.append(addg)
for i in range(d):
    addc = list(map(int, input(str(i+1) + "'th dot connected to: ").split()))
    addw = list(map(int, input('distances of roads below: ').split()))
    for j in range(len(addc)):
        graph[i][addc[j]-1] = addw[j]
        graph[addc[j]-1][i] = addw[j]
for i in graph:
    print(i)
# graph = [
#     [0, 1, 1, 0, 0, 0],
#     [1, 0, 0, 1, 0, 0],
#     [1, 0, 0, 4, 1, 0],
#     [0, 1, 4, 0, 0, 2],
#     [0, 0, 1, 0, 0, 4],
#     [0, 0, 0, 2, 4, 0]
# ]
start = int(input('from which dot we start: '))
end = int(input('on which dot we end: '))
locked = set([])
def main(ondot, plus):
    locked.add(ondot)
    if ondot == end:
        print(plus)
    else:
        min_cost = min([x + plus for i, x in enumerate(graph[ondot-1]) if x != 0 and i+1 not in locked])
        ind = [x for x, num in enumerate(graph[ondot-1]) if num + plus == min_cost and x+1 not in locked]
        # print(min_cost)
        # print(ind)
        # for x, num in enumerate(graph[ondot-1]):
        #     print(num == min_cost)
        #     print(x+1 not in locked)
        main(ind[0]+1, min_cost)
main(start, 0)