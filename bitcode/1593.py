n = int(input())
l = [0]*(n+1)
s = list(map(int,input().split()))
ans = 0
for i in s:
    if l[i] == 0:
        l[i] = 1
    else:
        ans = ans + 1
print(ans)