l = []
d = {}
a = []
for i in range(8):
    s = int(input())
    l.append(s)
    d[s] = i+1
    
l.sort(reverse=True)


for j in range(5):
    v  = l[j]
    c = d[v]
    a.append(c)   

a.sort()
        
print(sum(l[:5]))
for i in a:
    print(i,end=" ")

    
