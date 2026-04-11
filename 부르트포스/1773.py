n,c = map(int,input().split())
ks = []
for _ in range(n):
    ks.append(int(input()))
ks.sort()
kss = [ks[0]]
for k in ks:
    isAns = True
    for i in kss:
        if k %i == 0:
            isAns = False
            break
    if isAns:
        kss.append(k)

s = set()
for k in kss:
    for i in range(k,c+1,k):
        s.add(i)
print(len(s))