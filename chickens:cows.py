heads = int(input("Enter heads: "))
legs = int(input("Enter legs: "))

valid = [heads, legs]
cows = abs((valid[1] - abs(valid[0]) * 2) / 2)  # різниця ніг і голів = половина ніг корів
if (valid[1] - valid[0] * 2) % 2 == 0:  # п-5еревіряємо, чи різниця на 2 дає ціле число
    cows = int(cows)
    chikens = abs(valid[0]- cows) # обчислення кількості курей
    cowslegs = cows * 2
    if (valid[1] - cowslegs) / 2 == valid[0]:
        print(f"Chikens {chikens}, Cows {cows}")
    else:
        print("Impossible")
else:
        print("Impossible")
