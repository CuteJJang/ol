s = input()

d = {
    0: "000",
    1: "001",
    2: "010",
    3: "011",
    4: "100",
    5: "101",
    6: "110",
    7: "111",
}

d1 = {
    0: "0",
    1: "1",
    2: "10",
    3: "11",
    4: "100",
    5: "101",
    6: "110",
    7: "111",
}
print(d1[int(s[0])],end="")
for i in s[1:]:
    print(d[int(i)],end="")
# a= 0
# e = 1

# n = s[::-1]

# l = []

# for i in n:
#     a += int(i) * e
#     e = e * 8

# while True:
#     if a == 0:
#         break

#     l.append(a%2)
#     a = a //2
    
# for i in l[::-1]:
#     print(i,end="")