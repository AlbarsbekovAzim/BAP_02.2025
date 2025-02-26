sl = int(input())
s = str(input())
newS = []
for i in s:
    newS.append(i)
s = newS
del newS
# print(sl, s)
candel = 0
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# latest = 'a'
# def findlat():
#     global latest
#     latest = 'a'
#     for i in s:
#         latest = i if alphabet.index(i) > alphabet.index(latest) else latest
# findlat()
# print(latest)
def prevlet(j):
    if (j>0 and j<len(s)-1):
        # print(len(s), j)
        return ord(s[j-1]) == ord(s[j]) - 1 or ord(s[j+1]) == ord(s[j]) - 1
    elif (j==0 and j<len(s)-1):
        return ord(s[j+1]) == ord(s[j]) - 1
    elif (j==len(s)-1):
        return ord(s[j-1]) == ord(s[j]) - 1
for i in range(len(alphabet) - 1, -1, -1):
    # print(alphabet[i])
    j = 0
    while j < len(s):
        # print(s, j)
        if s[j] == alphabet[i] and prevlet(j):
            s.pop(j)
            candel+=1
            j = 0
        else:
            j+=1
print(candel)