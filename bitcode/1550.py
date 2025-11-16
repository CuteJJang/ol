n,m,k = list(map(int,input().split()))
l = [0] * (n+ 1)
for i in range(k):
    s = list(map(int,input().split()))
    for c in s:
        l[c]+=1


for i in range(1,n+1):
    if l[i] != 0:
        print(f"{i} {l[i]}")