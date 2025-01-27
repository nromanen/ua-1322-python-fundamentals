def check(num: str) -> bool:
    try:
        num = int(num)
        if num < 0:
            # I understand that raising and catching is a silly thing to do,
            # but that is what the task asked for, personally i would have done it with
            # simply return false instead of raising and catching the exeption we just raised.
            raise ValueError("Negative Number")
    except ValueError as f:
        print ("Not a number! or nergative number.", f)
        return False

    return True