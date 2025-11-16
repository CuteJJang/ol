n = int(input())
l = [-1] * 5006
l[3] = 1
l[5] = 1
for i in range(3,n+1):
    if l[i] != -1:
        if l[i]+1 < l[i+3] or l[i+3] == -1:
            l[i+3] = l[i]+1
        if l[i]+1 < l[i+5] or l[i+5] == -1:
            l[i+5] = l[i]+1
print(l[n])