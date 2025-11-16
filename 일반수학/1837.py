p,k = map(int,input().split())
prime = [1] * 1000001

prime[0] = 0
prime[1] = 0

d = 0

for i in range( 2,k):
    if prime[i] == 1:
        for t in range(i,k,i):
            prime[t] = 0
            
        prime[i] = 1
        
        if p % i == 0:
            d = i
            break
            
if d != 0:
    print("BAD",d)
else:
    print("GOOD")       