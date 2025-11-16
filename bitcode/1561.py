n = int(input())
a = 2
b = 0
ans = 0

while True:
    if n % a == 0:
        b = n // a
        if a > b:
            break

        if a *3 >= b:
            if a == b:
                ans = ans + 1
            else:
                ans = ans + 2
    a = a + 1 
if ans == 0 :
    ans = ans - 1       
print(ans)