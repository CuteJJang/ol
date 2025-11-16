lx = []
ly = []
for i in range(3):
    x,y = map(int,input().split())
    lx.append(x)
    ly.append(y)
lx.sort()
ly.sort()
if lx[1] == lx[0]:
    print(lx[2],end=" ")
else:
    print(lx[0],end=" ")
if ly[1] == ly[0]:
    print(ly[2],end=" ")
else:
    print(ly[0],end=" ")