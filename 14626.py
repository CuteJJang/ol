s = input()
odd= True
a = 0
for i in range(len(s)):
    if s[i] == "*":
        if i % 2 == 0:
            odd = False
            
            
    else:
        if i % 2 == 1:
            a += int(s[i]) * 3
        else:
            a += int(s[i])

if odd == False:
    k = a % 10
    print(10-k)
else:
    for i in range(10):
        
        if (a+3*i) % 10 == 0:
            print(i)
            break