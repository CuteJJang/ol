s = input()
y = " "#이전 문자 저장용
n = " "#지금 문자 저장용
ans = 0
for i in s:
    n = i
    if n == " " and y != " ":
        ans = ans + 1
    y = n 
if n != " ":
    ans = ans + 1
print(ans)
