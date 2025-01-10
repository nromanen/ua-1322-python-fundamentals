evn_list = []
od_list = []
etc_list = []

for i in range(1, 10):
    if i % 2 == 0:
        evn_list.append(i)
        
    elif i % 3 == 0:
        od_list.append(i)
        
    else:
        etc_list.append(i)
    
print("even numbers that are divisible by 2: ", evn_list)
print("odd numbers that are divisible by 3: ", od_list)
print("numbers that are not divisible by 2 and 3", etc_list)