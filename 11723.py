import sys

def input():
    return sys.stdin.readline().rstrip()


n = int(input())
s = set()

for i in range(n):
    l = input().split()
    if l[0] == "add":
        s.add(l[1])
    elif l[0] == "remove":
        if l[1] in s:
            s.remove(l[1])
    elif l[0] == "check":
        if l[1] in s:
            print(1)
        else:
            print(0)
    elif l[0] == "toggle":
        if l[1] in s:
            s.remove(l[1])
        else:
            s.add(l[1])
    elif l[0] == "all":
        for i in range(1,21):
            s.add(str(i))
    elif l[0] == "empty":
        s.clear()

    