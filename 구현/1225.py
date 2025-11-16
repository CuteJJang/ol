a,b = input().split()

aa = 0
bb = 0

for i in a:
    aa+=int(i)
for i in b:
    bb+=int(i)
print(aa*bb)