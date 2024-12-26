num = str(input("Input a 4 digit number: "))
num_list = list(num)
num_list.sort()

print(f"Sum: {sum(map(int, num))}",
      f"Reverse: {num[::-1]}",
      sep = "\n")
print("Ascending: ", *num_list, sep ="")