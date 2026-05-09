n = int(input())
l = []
for i in range(n):
    a = int(input())
    l.append(a)

l.sort()

k = l
s = set(l)
xs = 5
for i in k:
    ans = 0
    if i +1 not in s:
        ans+=1

    if i+2  not in s:
        ans+=1
    if i+3  not in s:
        ans+=1
    if i+4  not in s:
        ans+=1

    xs = min(ans,xs)
    
print(xs)