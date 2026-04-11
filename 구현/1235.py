n = int(input())
s = [input() for _ in range(n)]

l = len(s[0])

for i in range(1,l+1):
    d = {}
    ans = True
    for t in s:
        if t[-i:] in d:
            ans  = False
            break
        else:
            d[t[-i:]] = 0

    if ans:
        print(i)
        break




        
        

