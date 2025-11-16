n,m = list(map(int,input().split()))

l = [0] * (n+1)

for 짱굠 in range(m):
    s,e,k = list(map(int,input().split()))
    for i in range(s,e+1):
        l[i] = k


print(*l[1:])                            