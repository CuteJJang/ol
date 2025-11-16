n = int(input())
ans = 1
for i in range(1,n+1):
    print(" "*(n-i),ans * "*",sep="")
    ans+=2