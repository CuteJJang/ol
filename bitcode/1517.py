n = int(input())
l = list(map(int,input().split()))
for i in range(n):
    l.sort(reverse=True)
print(*l)