n = int(input())
l = [0] + list(map(int,input().split()))
a,b = map(int,input().split())
f = [1] * (n+1)

while True:
    odd = 99999
    g = 0
    for i in range(a,b+1):
        if l[i] % 2 == 1 and odd > l[i]:
            odd = l[i]

    for i in range(a,b+1):
        if l[i] == 0:
            continue
        if l[i] % 2 == 0:
            l[i] = l[i] // 2
            f[i] +=1
        else:
            l[i] = odd -1
            f[i] +=1

        g+=l[i]
    if g == 0:
        break
print(*f[a:b+1])