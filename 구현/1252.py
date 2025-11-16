a,b = input().split()

if len(a) > len(b):
    b = "0" * (max(len(a),len(b))-len(b)) + b
elif len(b) > len(a):
    a = "0" * (max(len(a),len(b))-len(a)) + a

a=a[::-1]
b = b[::-1]
ans = [0]
for i in range(len(a)):
    ans[i] = int(a[i])+int(b[i])+ans[i]
    
    ans.append(ans[i]//2)
    
    ans[i] = ans[i] % 2
    
while ans and ans[-1] == 0:
    ans.pop()
if len(ans) == 0:
    print(0)       
print(*ans[::-1],sep="")    
    