


from collections import defaultdict


t = int(input())

def solve():
    n = int(input())
    d = defaultdict(int)
    
    for _ in range(n):
        a,b = input().split()
        d[b]+=1
    
    ans = 1
    for v in d.values():
        ans*=(v+1)
    ans = ans - 1
    print(ans) 
    
    
    
def solve2():
    n = int(input())
    d = defaultdict(list)
    
    for _ in range(n):
        a,b = input().split()
        d[b].append(a)
        
    
        
    k = len(d.keys())
    ans = []
    def recu(nn):   
        if nn == k:
            print(ans)
            return
        
        kind = list(d.keys())[nn]
        
    recu(0)   
    
    
    
    
    
                 
    
for  _ in range(t):
    solve2()