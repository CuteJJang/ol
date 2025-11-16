n = int(input())
l = list(map(int,input().split()))
ansl = l[0]
ansh = l[0]
for i in l:
    if ansl > i:
        ansl = i
    if ansh < i:
        ansh = i
print(ansl,ansh)            