n = int(input())
l = []

for _ in range(n):
    a,b = map(int,input().split())
    l.append((a,b))

for i in range(n):
    w = l[i][0]
    h = l[i][1]
    ans= 1
    for j in range(n):
        w1 = l[j][0]
        h1 = l[j][1]
        if w1 > w and h1 > h:
            ans = ans + 1
    print(ans,end = " ")