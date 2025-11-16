a,b,v = map(int,input().split())
s = v-a
ans = 0
ans+=s//(a-b)
if  s % (a-b) != 0:
    ans+=1
print(ans+1)

