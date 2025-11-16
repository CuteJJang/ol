n = int(input())
ans = []
def solve(s,o,e,k):
    if k == 1:
        ans.append((s,e))
        return 
    solve(s,e,o,k-1)
    ans.append((s,e))   
    solve(o,s,e,k-1)
    

solve(1,2,3,n)

print(len(ans))
for c in ans:
    print(*c)