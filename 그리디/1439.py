s = input()
cnt1 = 0
cnt0 = 0

p = s[0]

if s[0] == '1':
    cnt1+=1
    p = s[0]
else:
    cnt0+=1
    p = s[0]
for c in s:
    if c != p:
        if c == '1':
            cnt1 += 1
        else:
            cnt0 +=1
        p=c
    
print(min(cnt1,cnt0))

