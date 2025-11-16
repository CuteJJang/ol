t = int(input())
l = [0] * 4
l[1] = 1
for i in range(t):
    a,b = map(int,input().split())
    l[a],l[b] = l[b],l[a]

for i in range(1,4):
    if l[i] == 1:
        print(i)    