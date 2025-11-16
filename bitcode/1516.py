n = int(input())
l = list(map(int,input().split()))
for i in range(n):
    l.sort()
print(*l)