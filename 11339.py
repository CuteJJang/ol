n = int(input())
l = list(map(int,input().split()))
l.sort()
ans = [0] * (n)
f = 0
ans[0] = l[0]
for i in range(1,n):
    ans[i] = ans[i-1] + l[i]
for i in ans:
    f+=i

print(f)
    

