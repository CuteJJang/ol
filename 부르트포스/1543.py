l = input()
s = input()
ans = 0
t = 0
while True:
    if t + len(s) > len(l):
        break
    
    c = True
    if l[t] == s[0]:
        for i in range(len(s)):
            if t+i > len(l) or l[t+i] != s[i]:
                c = False
                break
        if c == True:
            ans+=1
            t+=len(s)
        else:
            t+=1
            
    else:
        t+=1
        
print(ans)