n = int(input())
p = []
for i in range(n):
    x,y = map(int,input().split())
    p.append([y,x])
p.sort()
for y,x in p:
    print(x,y)