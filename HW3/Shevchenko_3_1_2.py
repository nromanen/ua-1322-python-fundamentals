
fr_dgt = input('Введить чотиризначне число\n')
print(f'Ви ввели: {fr_dgt}')

digits = [int(i) for i in str(fr_dgt)]
print(digits)


rv_dgt = fr_dgt[::-1]
print(int(rv_dgt))

rv_dgt = int(''.join(sorted(str(fr_dgt))))
print(rv_dgt)