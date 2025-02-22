import math
n = int(input())
ans = []
for j in range(n):
    x = int(input())
    xdevby111 = math.floor(x/111)
    leftafterxdby111 = x - xdevby111 * 111
    finalleft = leftafterxdby111 - math.floor(leftafterxdby111/11) * 11
    if (x > 1111 or xdevby111 >= 11 - finalleft or finalleft == 0):
        ans.append("YES")
    else:
        ans.append("NO")
for i in range(n):
    print(ans[i])