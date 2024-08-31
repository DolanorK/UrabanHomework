my_dict = {'kostya':2000, 'pasha':2001,'oleg':1999}
print(my_dict)
print(my_dict['pasha'])
my_dict['kirill'] = 1998
print(my_dict['kirill'])
my_dict.update({'yarik':1984,
                'sergey':1997})
a = my_dict.pop('oleg')
print(a)
print(my_dict)
my_set = {'яблоко',2,6,2,5,3,6,2,6,True}
print(my_set)
print(my_set.add(False))
print(my_set.add(1))
print(my_set.discard(2))
print(my_set)
