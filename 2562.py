l = []
for i in range (9):
    k = int(input())
    l.append(k)

ansh = l[0]
idx = 0

for i in range(  len(l)  ):
    if ansh <= l[i]:
        ansh = l[i]
        idx = i + 1
print(ansh,idx,sep="\n")        


