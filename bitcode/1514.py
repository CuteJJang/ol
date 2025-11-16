n = int(input())
l = [0] + list(map(int,input().split()))
a,b = map(int,input().split())
total = 0
for i in range(a,b+1):
    total+=l[i]
print(total)