def count_sheep(sheep):
    present = 0
    for i in sheep:
        if i:
            present += 1
    return present
