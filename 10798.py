l = []
for i in range(5):
    s = input()
    l.append(s)
    
for i in range(15):
    for j in range(5):
        s = l[j]
        if len(s) > i:
            print(s[i],end="")        