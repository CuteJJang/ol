l = [-1]*26
s = input()
c = 0
for i in s:
    p = ord(i)-97
    if l[p] == -1:
        l[p] = c
    c = c+1
print(*l)    
    
