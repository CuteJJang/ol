n = int(input())

l = list(map(int,input().split()))

v = int(input())

ans = 0
for i in range(len(l)):
    if l[i] == v:
        ans = ans + 1
print(ans)

