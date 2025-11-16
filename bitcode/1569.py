n = int(input())
l = [0,1,2,4]
for i in range(4,n+1):
    l.append(l[i-1]+l[i-2]+l[i-3])
    l[i] = l[i-1] + l[i-2] + l[i-3]
print(l[n])  