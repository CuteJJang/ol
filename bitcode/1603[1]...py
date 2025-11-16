s = input()
ansm = -9999
ansl = 9999
for i in range(len(s)):
    a= ord(s[i])
    if ord("a") <= a <= ord("z"):
        if ansm < a:
            ansm = a
        if ansl > a:
            ansl = a
print(ansm-ansl)