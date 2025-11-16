n = int(input())
ans = 0
ansl = []
for i in range(n+1):
    a = n
    b = i
    t = [n,i]
    while True:
        c = a-b
        a= b
        b =c
        if b < 0:
            break
        t.append(b)
    if ans < len(t):
        ans = len(t)
        ansl = t[:]
        
print(ans)
print(*ansl)
    