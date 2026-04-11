k,s,m  = input().split()
m = int(m)

k = (int(k[1]) -1,ord(k[0]) - ord("A"))
s = (int(s[1]) -1,ord(s[0]) - ord("A"))

di   = {
    'B':(-1,0),
    'T': (1,0),
    'R': (0,1),
    'L': (0,-1),
    'RT': (1,1),
    'RB': (-1,1),
    'LT':(1,-1),
    'LB' : (-1,-1),
}

for _ in range(m):
    order = input()
    dy, dx = di[order]
    nk = (k[0]+dy,k[1]+dx)
    
    if 0 <= nk[0] < 8 and 0 <= nk[1] < 8:
        if s == nk: 
            ns = (s[0]+dy,s[1]+dx)
            if 0 <= ns[0] < 8 and 0 <= ns[1] < 8:
                s = ns
                k = nk
            else:
                continue

        else:
            k = nk
    else:
        continue


k = chr(k[1] + ord('A'))+ str(k[0] +1)
s = chr(s[1] + ord('A'))+ str(s[0] +1)
print(k)
print(s)