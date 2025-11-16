b= input()
b=int(b)
a= input()
a=int(a)
일의자리=(a % 10)
십의자리=a // 10 % 10
백의자리=a//100
print(b*일의자리)
print(b*십의자리)
print(b*백의자리)
print(b*a)