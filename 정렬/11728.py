n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
l = []

for i in a:
    l.append(i)
for i in b:
    l.append(i)
l.sort()

for i in l:
    print(i,end= " ")