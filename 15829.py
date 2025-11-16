n = int(input())
s = list(input())
ans = 0

for i in range(n):
   ans+=(ord(s[i])-ord('a')+1)*(31**i)
print(ans%1234567891) 
        