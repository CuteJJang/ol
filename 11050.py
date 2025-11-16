n,k = map(int,input().split())

l = [1,1]
for _ in range(n-1):
    
    l2 = [l[0]] 
    for i in range(1, len(l)):
        l2.append(l[i-1] + l[i])
    l2.append(l[-1])
 
    l = l2

print(l[k])