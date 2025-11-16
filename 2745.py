s,c = input().split()
c =  int(c)
s = s[::-1]

a = 1
ans = 0
di = {
}
g = 0
for cc in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    di[cc]  = g
    g+=1
for i in range(len(s)):
    key = s[i]
    k = di[key]
    ans+= k *a
    a = a * c
print(ans)    
    