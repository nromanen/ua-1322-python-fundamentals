def solution(number):
    if number < 0:
        return 0
    return sum(n for n in range(number) if n % 3 == 0 or n % 5 == 0)
