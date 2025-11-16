n = int(input())
ans = 0
for _ in range(n):
    l = [0] * 26
    s = input()
    p = ""
    for c in s:
        if c == p:
            continue
        else:
            if l[ord(c)-97] == 1:
                ans-=1
                break
            else:
                l[ord(c)-97] = 1
        p = c
    ans+=1
print(ans)     

