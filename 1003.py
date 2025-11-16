ans = {
    0:(1,0),
    1:(0,1),
    2:(1,1),
    3:(1,2),
    4:(2,3)
}

def solve():

    n = int(input())
    def fibo(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        if n in ans:
            return ans[n]
        lans = fibo(n-1)
        rans = fibo(n-2)
        
        ans[n] = lans[0]+rans[0],lans[1]+rans[1]
        return ans[n]

    fibo(n)
    print(*ans[n])

t = int(input())
for _ in range(t):
    solve()
    