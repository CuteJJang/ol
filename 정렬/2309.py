l = []
for i in range(9):
    t = int(input())
    l.append(t)
l.sort()

for i1 in range(3):
    for i2 in range(i1+1,9):
        for i3 in range(i2+1,9):
            for i4 in range(i3+1,9):
                for i5 in range(i4+1,9):
                    for i6 in range(i5+1,9):
                        for i7 in range(i6+1,9):
                            ans = l[i1] + l[i2] + l[i3] + l[i4] + l[i5] + l[i6] + l[i7]
                            if ans == 100:
                                print(l[i1],l[i2],l[i3],l[i4],l[i5],l[i6],l[i7],sep="\n")
                                exit()
                                    