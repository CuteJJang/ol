w = []
k = []
for i in range(10):
    a = int(input())
    w.append(a)
w.sort(reverse=True)
for i in range(10):
    b = int(input())
    k.append(b)
k.sort(reverse=True)
print(w[1]+w[0]+w[2],k[0]+k[1]+k[2])