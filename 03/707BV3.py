def main():
    n, m, k = map(int, input().split())
    uvl = [tuple(map(int, input().split())) for i in range(m)]
    if k == 0:  
        print(-1)
        return
    ka = set(map(int, input().split()))

    min_cost = float('inf')

    for u, v, cost in uvl:
        if (u in ka and v not in ka) or (v in ka and u not in ka):
            min_cost = min(min_cost, cost)

    print(min_cost if min_cost < float('inf') else -1)

main()