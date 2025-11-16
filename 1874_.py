n = int(input())
s = []
ans = []
t = int(input())
inputcnt = 1
for i in range(1,n+1):
    s.append(i)
    ans.append("+")
    while len(s) > 0 and s[-1] == t:
        s.pop()
        ans.append("-")
        if inputcnt == n:
            break
        t = int(input())
        inputcnt +=1
if len(s) > 0:
    print("NO")
else:
    print(*ans,sep="\n")