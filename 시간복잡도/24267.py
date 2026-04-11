s = int(input())

def solve(n):
    cnt = n * (n-1) * (n-2) // 6
    # for i in range(1,n-1):
    #     for j in range(i+1,n):
    #         for k in range(j+1,n+1):
    #             cnt+=1

    return cnt


print(solve(s))
