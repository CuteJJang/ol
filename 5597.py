l = [0] * 31

for i in range(28):
    s = int(input())
    l[s] = 1


for i in range(1,31):
    if l[i] == 0:
        print(i)