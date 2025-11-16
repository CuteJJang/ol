s = input()
a = []
for i in range(1,len(s)):
    for j in range(i+1,len(s)):
        a.append(s[:i][::-1]+s[i:j][::-1]+s[j:][::-1])
a.sort()
print(a[0])