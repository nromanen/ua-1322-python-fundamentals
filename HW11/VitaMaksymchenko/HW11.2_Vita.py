def day_analyze(number):
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday",
    }

    if 1 <= number <= 7:
        return days[number]
    else:
        return "Invalid number!"


def main():
    while True:
        try:
            user_input = input(
                "Enter a number (1-7) to get the corresponding day of the week: "
            )
            number = int(user_input)
            day = day_analyze(number)

            print(f"The {number} day of the week is {day}")
            if 1 <= number <= 7:
                break

        except ValueError:
            print("Invalid input!")


if __name__ == "__main__":
    main()
