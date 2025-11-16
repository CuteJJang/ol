n,k = map(int,input().split())
l = list(map(int,input().split()))
a = []
for i in l:
    a.append(i)
    
a.sort()
print(a[-k])

