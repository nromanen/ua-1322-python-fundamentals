def correct_tail(body, tail):
    if body[-len(tail):] == tail:
        return True
    else:
        return False
