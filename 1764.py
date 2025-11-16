n,m = map(int,input().split())
s = set()
ans = []

for i in range(n):
    s.add(input())
for _ in range(m):
    d = input()
    if d in s:
        ans.append(d)
ans.sort()
print(len(ans))
for i in ans:
    print(i)