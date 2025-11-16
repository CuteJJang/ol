x,y = input().split()

x = x[::-1]
y = y[::-1]

d = int(x)+int(y)
d = str(d)
d = d[::-1]
print(int(d))