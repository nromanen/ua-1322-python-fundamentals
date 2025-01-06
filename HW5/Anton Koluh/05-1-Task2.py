#Fibonacci up untill given goal_num

goal_num = int(input("Enter a number: "))
initial_num = 0
current_num = 1

print("0\n1")
while current_num + initial_num <= goal_num:
    print(initial_num + current_num)
    current_num, initial_num = current_num + initial_num, current_num