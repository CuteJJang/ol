n = int(input())
l = []

for i in range(1,n+1):
    l.append(i)


while True:
    if len(l) == 1:
        break
    
    ll = []
    if len(l) % 2 == 0:
        for i in range(0,len(l),2):
            ll.append(l[i])
    else:
        for i in range(2,len(l),2):
            ll.append(l[i])

    l = ll

# print(l[0])
print(*l)