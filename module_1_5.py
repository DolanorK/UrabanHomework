immutable_var = 1, True, "строка"
print(immutable_var)
#immutable_var[0] = 200
#print(immutable_var) кортеж не поддерживает обращение по элементам, используется как хранилище данных, которое мы не хотим изменять
mutable_list = [True, 'строка', 2]
mutable_list[0] = False
mutable_list[1] = 12
mutable_list[2] = 'новая строка'
print(mutable_list)
