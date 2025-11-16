l = [0]*26
s = input()
for c in s:
    idx = ord(c)
    if idx >= 97:
        idx-=97
    else:
        idx-=65
    l[idx]+=1
ansv=-1
ansi=0
for i in range(26):
    if ansv < l[i]:
        ansv = l[i]
        ansi = i
    elif l[i] == ansv:
        ansi = ord('?')-65
print((chr(ansi+65)))