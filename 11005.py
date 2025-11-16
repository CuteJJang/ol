d,c = map(int,input().split())
ans = []
di={    
}
k = 10
for i in range(10):
    di[i] = i
for cc in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    di[k] = cc
    k+=1
while d != 0:
    ans.append(di[d%c])
    d = d//c
ans.reverse()
for i in range (len(ans)):
    print(ans[i],end="")
    