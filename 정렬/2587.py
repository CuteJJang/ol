l = []
ans = 0

for i in range(5):
    a = int(input())
    ans+=a
    l.append(a)
    
l.sort()
ans = ans // 5
print(ans,l[2],sep="\n")