n = int(input())
lx = []
ly = []
for i in range(n):
    a,b = map(int,input().split())
    lx.append(a)
    ly.append(b)
lx.sort()
ly.sort()
print((lx[-1]-lx[0])*(ly[-1]-ly[0]))
