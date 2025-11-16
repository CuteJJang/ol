s = input()
L = 0
O = 0
V = 0
E = 0
for i in s:
    if i == "L":
        L+=1
    elif i == "O":
        O+=1
    elif i == "V":
        V+=1
    elif i == "E":
        E+=1
t = int(input())
aans = []
for _ in range( t):
    s = input()
    for i in s:
        if i == "L":
            L+=1
        elif i == "O":
            O+=1
        elif i == "V":
            V+=1
        elif i == "E":
            E+=1
        
    ans = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100
    aans.append((-ans,s))
    for i in s:
        if i == "L":
            L-=1
        elif i == "O":
            O-=1
        elif i == "V":
            V-=1
        elif i == "E":
            E-=1
aans.sort()
print(aans[0][1])            