def solution(number):
    if number < 0:
        return 0
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)