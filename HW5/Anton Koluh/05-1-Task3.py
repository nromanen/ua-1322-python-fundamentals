#Calculate factorial with a loop

goal_num = int(input("Enter a number: "))
result = 1
for i in range(1, goal_num + 1):
    result = result*i

print(f"{goal_num}!={result}")