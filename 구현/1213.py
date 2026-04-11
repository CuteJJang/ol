al = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
d = {}
s = input()
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i] = 1

ans = []
ce = ""
for c in al:
    if c in d:
        while d[c] > 1:
            ans.append(c)
            d[c] -=2
        if d[c] == 1:
            if ce != "":
                print("I'm Sorry Hansoo")
                exit()
                break
            else:
                ce = c
                d[c] = 0

aans = ans + [ce] + list(reversed(ans))
print(*aans,sep="")