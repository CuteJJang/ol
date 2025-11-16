def sum_between(start,end):
    if start > end:
        print("start는 end보다 클 수 없습니다.")
    result = []
    for i in range(start,end+1):
        result.append(i)
    return result
print("0 ~ 10", sum_between(0 , 10))
print("0 ~ 100", sum_between(0 , 100))
print("50 ~ 100", sum_between(50 , 100))
print("30 ~ 10", sum_between(30 , 10))
