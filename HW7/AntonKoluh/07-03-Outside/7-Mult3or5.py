def solution(number):
    num_lst = []
    for x in range(number - 1, 0, -1):
        if x % 3 == 0 or x % 5 == 0:
            num_lst.append(x)
    return sum(num_lst)