n,k = map(int,input().split())
l = []
ans = 0
for i in range(n):
    s = int(input())
    l.append(s)
while k != 0:
    ans +=k//l[-1]
    k = k % l[-1]
    l.pop()
    
print(ans)  