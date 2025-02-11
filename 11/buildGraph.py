n = int(input("How many vertices we'll add: "))
graph = {}
for i in range(4+n):
    graph[i+1] = set([])
for i in range(5, 5 + n):
    for j in range(5, 5 + n):
        if not j == i:
            graph[i].add(j)
for i in range(1, 5):
    for j in range(2):
        lengths = [len(graph[x]) for x in graph if x > 4]
        ind = [index + 5 for index, num in enumerate(lengths) if num == min(lengths)]
        graph[i].add(ind[0])
        graph[ind[0]].add(i)

# print([graph[x] for x in graph])

for i in range(4 + n):
    print(i+1,':',graph[i+1])


    # print(len(graph[i+1]))
# print(graph)