s = input()
ans = 0
l = [3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10]
for c in s:
    idx = ord(c)-65
    ans = ans + l[idx]
print(ans)