def day_of_week(num):
    """Return the name of the day corresponding to a given number."""
    days = ["Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday"]
    return f"{num} is {days[num-1]}"

def main():
    """ 
    Prompt the user to enter a number between 1 and 7 and print the 
    corresponding day or an appropriate error message.
    """
    try:
        num = int(input("Enter the number between 1 and 7: "))
        print(day_of_week(num))
    except ValueError:
        print("Invalid input. Please enter a number.")   
    except IndexError:
        print("The number isn'n in range between 1 and 7.")

if __name__ == "__main__":
    main()