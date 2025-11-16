n = int(input())
l = []
f = [0]+[1]+[0]*29
l.append(f)
for i in range(1,n):
    a = [0]
    for j in range(1,31):
        t =l[i-1][j-1] + l[i-1][j]
        a.append(t)
    l.append(a)
e = 2
for c in l:
    for i in range(1,e):
        print(c[i],end=" ")
    print()
    e+=1