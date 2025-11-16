n,k = map(int,input().split())
l = [0]
for i in range(1,n+1):
    if n % i == 0:
        l.append(i)
if k > len(l)-1:
    print(0)
else:
    print(l[k])