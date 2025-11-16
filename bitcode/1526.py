s = input()
k = int(input())

# print(*s[k-1:])

for i in range(len(s)):
    if i >= (k-1):

        print(s[i],end="")