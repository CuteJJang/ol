k = 0
for i in range(1,4):
    s = input()
    if s[0] != "F" and s[0] != "B":
        k = 4-i + (int(s))
    
if k % 3 == 0 and k % 5 == 0:
    print("FizzBuzz")
elif k % 3 == 0 :
    print("Fizz")
elif k % 5 == 0:
    print("Buzz")
else:
    print(k)
    