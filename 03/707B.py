def main():
    nmk = list(map(int, input().split()))
    uvl = []
    for i in range(nmk[1]):
        uvl.append(list(map(int, input().split())))
    ka = []
    if nmk[2] > 0:
        ka = list(map(int, input().split()))
    else:
        print(-1)
        return
    minimum = []
    for i in range(nmk[0]):
        minimum.append(float('inf'))
    for i in range(len(uvl)):
        minimum[uvl[i][0] - 1] = uvl[i][2] if uvl[i][2] < minimum[uvl[i][0] - 1] else minimum[uvl[i][0] - 1]
        minimum[uvl[i][1] - 1] = uvl[i][2] if uvl[i][2] < minimum[uvl[i][1] - 1] else minimum[uvl[i][1] - 1]
    minfordelivery = []
    for i in range(len(ka)):
        minfordelivery.append(minimum[ka[i] - 1])
    if min(minfordelivery) < float('inf'):
        print(min(minfordelivery))
    else:
        print(-1)
main()