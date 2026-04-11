# n = int(input())
# a = [0] * 1_000_001
# for i in range(n):
#     s = int(input())
#     a[s] += 1


# for i in range(1,1_000_001):
#     if a[i] != 0:
#         for _ in range(a[i]):
#             print(i)
n = int(input())
l = []
for i in range(n):
    s = int(input())
    l.append(s)

l.sort()

for i in l:
    print(i)
