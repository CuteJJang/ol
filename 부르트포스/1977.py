m = int(input())
n = int(input())
l = []

a  = 1
while True:
    if a*a > n:
        break
    
    if m <= a*a <= n:
        l.append(a*a)
    a+=1
        
if l:
    print(sum(l))
    print(min(l))
else:
    print(-1)