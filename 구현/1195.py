s1 = list(map(int,input()))
s2 = list(map(int,input()))

if len(s1) < len(s2):
    s1,s2 = s2,s1
 



l1 = len(s1)
l2 = len(s2)
s1 = [0] * l2 + s1 + [0] * l2

ans2 = l1+l2

for i in range(l1+l2):
    ok = True
    for j in range(l2):
        if s1[i+j] + s2[j] == 4:
            ok = False
            break

    if ok:
        if i < l2:
            ans2 = min(ans2,l1+l2-i)
            
        elif  l2 <= i <l1+l2:
            ans2 = min(ans2,l1)
        else:
            ans2 = min(ans2,i)

        



print(ans2)