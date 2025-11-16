n = int(input())
l = list(map(int,input().split()))
stack = []
idx = 0
for last in  range(1,n+1):
    if stack and stack[-1] == last:
        stack.pop()
        continue
    while idx != n:
        if last == l[idx]:
            idx+=1
            break
        else:
            stack.append(l[idx])
            idx+=1
            
        
if len(stack) == 0:
    print("Nice")
else:
    print("Sad")        
    