n = int(input())
stack = []
for _ in range(n):
    s = input().split()
    if "push" == s[0]:
        stack.append(s[1])

    elif "pop" == s[0]:
        if len(stack) == 0:
            print(-1)
        else:
            v = stack.pop()
            print(v)
    elif "top" == s[0]:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif "size" == s[0]:
        print(len(stack))
    else:
        if len(stack) == 0:
            print(1)
        else:
            print(0)