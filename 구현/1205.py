n,t,p = map(int,input().split())
if n == 0:
    l = []
else:

    l = list(map(int,input().split()))
l.sort(reverse=True)
if len(l) <p:
    l.append(t)
else:
    if l[-1] <  t:
        l[-1] = t
    else:
        print(-1)
        exit()
l.sort(reverse=True)
ans = [0] * len(l)
ans[0] = 1

if l[0] == t:
    print(1)
    exit()


for i in range(1,len(l)):
    if l[i-1]  != l[i]:

        ans[i] = i+1
    else:
        ans[i] = ans[i-1]

    if l[i] == t:
        print(ans[i])
        break

