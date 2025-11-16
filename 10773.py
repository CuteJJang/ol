k = int(input())
l = []
ans = 0
for i in range(k):
    a = int(input())
    if a == 0:
        l.pop()
    else:
        l.append(a)
for i in l:
    ans+=i
print(ans)