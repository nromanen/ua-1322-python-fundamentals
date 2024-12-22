heads = int(input("Heads: "))
legs = int(input("Legs: "))

parts = (heads, legs)
cows = int(parts[1]/2 - parts[0])
results = (abs(cows), abs(parts[0] - cows))
check_parts = ((results[0] + results[1]), (results[0]*4 + results[1]*2))

if parts == check_parts:
    print(f"(Cow, Chicken): {results}")
else:
    print ("Impossible.")
