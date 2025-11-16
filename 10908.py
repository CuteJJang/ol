s = input()

l = 0
r = len(s)-1
ans = 1
while l <= r:
    if s[l] != s[r]:
        ans = 0
        break
    l = l + 1
    r = r - 1
print(ans)