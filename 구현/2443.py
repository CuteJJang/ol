n = int(input())
ans = 1
for i in range(n):
    print(i*" ",(2*n-i*2-1)*"*",sep="")
    ans+=2