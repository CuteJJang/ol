n = int(input())
l = list(map(int,input().split()))
k = []
p = []
for i in l:
    if i % 2 == 1:
        k.append(i)

    else:
        p.append(i)
for i in range(len(k)):
    print(k[i],end=" ")
print()
for i in range(len(p)):
    print(p[i],end=" ")