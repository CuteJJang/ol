myNubers = [2,3,5,7,14,16,18]
newnubers = []
for i in myNubers:
    if i % 2 == 0 or i% 3 == 0 or i % 7 == 0:
        newnubers.append(i)
print(*newnubers)