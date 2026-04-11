n = int(input())
l = [0]*1001

l[1]= 1
l[2]= 2
for i in range(3,n+1):
    l [i] = l[i-1] + l[i-2]
print(l[n]%10007)