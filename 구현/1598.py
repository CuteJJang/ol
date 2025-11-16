a,b = map(int,input().split())
a,b = min(a,b),max(a,b)
ans=0
f = (a-1)//4
f2 = (b-1)//4
ans+= max(f2,f)-min(f2,f)

f = (a-1)%4
f2 = (b-1)%4
ans+= max(f2,f)-min(f2,f)




print(g+h)