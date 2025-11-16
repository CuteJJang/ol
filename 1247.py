def solve():
    ans = 0
    n = int(input())
    for i in range(n):
        a = int(input())
        ans+=a
    if ans > 0 :
        print("+")
    elif ans < 0:
        print("-")
    else:
        print(0)
for _ in range(3):
    solve()

    