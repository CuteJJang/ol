n = int(input())
k = [0] + list(map(int,input().split()))

start,end = map(int,input().split())

ans = [1] * (n+1)

while True:
    total = 0
    o = 1000
    for i in range(start,end+1):
        total += k[i]
        if k[i] % 2 == 1 and o > k[i]:
            o = k[i] - 1
    if total == 0:
        break    
    for i in range(start,end+1):
        if k[i] == 0:
            continue
        if k[i] % 2 == 0:
            k[i] = k[i]//2
            ans[i]+=1
        else:
            k[i] = o
            ans[i]+=1

for i in range(start,end+1):
    print(ans[i],end=" ")
