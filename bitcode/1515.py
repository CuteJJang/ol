n = int(input())
l =  list(map(int,input().split()))
k = int(input())
l[k] ,l[k-2] = l[k-2],l[k]
print(*l)