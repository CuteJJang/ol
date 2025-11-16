l = [0] * 42

for i in range(10):
    s = int(input())
    s = s%42
    l[s] = 1

aa = 0
for i in l:
    aa = aa + i
print(aa)