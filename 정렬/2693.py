t = int(input())
for i in range(t):
    l = list(map(int,input().split()))
    l.sort()
    print(l[-3])