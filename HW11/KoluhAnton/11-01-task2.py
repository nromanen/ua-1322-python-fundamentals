from check_func import check

days = {1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday',
        7: 'Sunday'}

def check_day(inpt_day: str) -> str:
    if check(inpt_day):
        inpt_day = int(inpt_day)
        if inpt_day > 7: inpt_day = inpt_day % 7
        return days[inpt_day]
    


if __name__ == "__main__":
    inpt_day = input("Enter a number: ")
    print(check_day(inpt_day))
    