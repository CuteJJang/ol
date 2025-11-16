l = []
t = 1

while True:
    if t*(t+1)//2>1000:
        break
    l.append(t*(t+1)//2)
    t+=1
    
ans = {}

for i in range(len(l)):
    for j in range(i,len(l)):
        for k in range(j,len(l)):
            key = l[i] + l[j] + l[k]
            ans[key] = 1

t = int(input())
for _ in range(t):
    a = int(input())
    if a in ans:
        print(1)
    else:
        print(0)