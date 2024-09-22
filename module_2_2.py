first = input('Введите первое чесло:')
second = input('Введите второе чесло:')
third = input('Введите третье чесло:')
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)