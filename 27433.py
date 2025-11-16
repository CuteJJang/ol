n = int(input())



def solve(k):
    
    if k == 0:
        return 1
    return solve(k-1) * k

print(solve(n))