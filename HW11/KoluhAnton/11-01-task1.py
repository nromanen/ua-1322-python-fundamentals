from check_func import check


if __name__ == '__main__':
    while True:
        age = input("Enter your age: ")
        if check(age):
            print ("Odd" if int(age)%2 else "Even")
            break
