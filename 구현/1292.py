a,b = map(int,input().split())

l = [0]
l2 = [0]
for i in range(1,10000):
    for j in range(i):
        l.append(i)
    if len(l) > 1001:
        break
l2 = [0] * len(l)
for i in range(1,len(l)):
    l2[i] = l2[i-1] + l[i]


print(l2[b]-l2[a-1])