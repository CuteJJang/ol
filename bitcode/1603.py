s = input()
ansm = -9999
ansl = 9999

for i in range(len(s)):
    d = ord(s[i])
    if ord("a") <= d <= ord ("z"):
        if ansm < d:
            ansm = d
        if ansl > d:
            ansl = d
print(ansm-ansl)