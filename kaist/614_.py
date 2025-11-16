def count_list(lst):
    odd_num = 0
    even_num = 0
    
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            odd_num+=i
        else:
            even_num+=i
    return odd_num, even_num

print(count_list([1, 4, 7, 9, 12, 14, 17, 25]))