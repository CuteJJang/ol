n = int(input())
s = []
ans = 0
for i in range(n):
    a = int(input())
    s.append(a)
s.sort(reverse=True)
for i in range(n):
    if s[i] >= 20:
        ans+=1
    print(s[i],end=" ")
print()
print(ans)