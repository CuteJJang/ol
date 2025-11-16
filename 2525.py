h,m = input().split()
h = int(h)
m = int(m)
t = int(input())
m = m + t
h = h + (m //60)
m = m % 60
h = h % 24
print(h,m)