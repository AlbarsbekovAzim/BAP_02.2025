t = int(input())
results = []
for ti in range(t):
    n = int(input())
    g = []
    isfree = []
    isproblem = []
    for i in range(n):
        kg = list(map(int, input().split()))
        g.append(kg)
        isfree.append(1)
        isproblem.append(0)
    def main():
        for i in range(n):
            if len(g[i]) > 1:
                for j in range(1, len(g[i])):
                    if isfree[g[i][j] - 1]:
                        isfree[g[i][j] - 1] = 0
                        break
                    elif j == len(g[i]) - 1:
                        isproblem[i] = 1
            else:
                isproblem[i] = 1
        problem = [l for l, num in enumerate(isproblem) if num == 1]
        if len(problem):
            problem = problem[0]
            whofree = [l for l, num in enumerate(isfree) if num == 1]
            if len(whofree):
                whofree = whofree[0] + 1
                results.append('IMPROVE')
                results.append(" ".join(map(str, [problem + 1, whofree])))
                return
        results.append('OPTIMAL')
    main()
for ti in range(len(results)):
    print(results[ti])