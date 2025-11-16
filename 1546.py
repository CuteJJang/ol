n = int(input())

l = list(map(int,input().split()))
ans = 0
m = max(l)
for i in l:
    ans += i/m*100
print(ans/n)