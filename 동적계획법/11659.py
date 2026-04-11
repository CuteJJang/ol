import sys
input = sys.stdin.readline
n,m = map(int,input().rstrip().split())
l = [0] + list(map(int,input().split()))


for i in range(1,n+1):
    l[i] = l[i-1] + l[i]

for i in range(m):
    s,e = map(int,input().split())
    print(l[e]-l[s-1])

# for _ in range(m):
#     s,e = map(int,input().split())
#     ans = 0
#     for i in range(s,e+1):
#         ans += l[i]
#     print(ans)