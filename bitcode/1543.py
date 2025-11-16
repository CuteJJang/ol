n = int(input())
l = list(map(int,input().split()))
m = 0
for i in range(n):
    if l[i] > m:
        m = l[i]
print(m) 