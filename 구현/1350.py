input()
l = list(map(int,input().split()))
c = int(input())
ans = 0 
for a in l:
    ans+= a//c
    if a %c != 0 :
        ans+=1
print(c*ans)