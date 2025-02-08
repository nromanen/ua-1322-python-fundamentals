def get_weekday(number):
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    return days.get(number, "Invalid input. Please enter a number from 1 to 7.")

def main():
    try:
        number = int(input("Enter a number (1-7) for the day of the week: "))
        print(get_weekday(number))
    except ValueError:
        print("Invalid input. Please enter a numerical value.")

if __name__ == "__main__":
    main()