calls = 0


def count_calls():
    global calls
    calls = calls + 1


def string_info():
    print("Введите строку")
    string = input()
    lenght = len(string)
    upper = string.upper()
    lower = string.lower()
    my_tuple = (lenght, upper, lower)
    print(my_tuple)
    count_calls()


def is_contains():
    print("Введите строку и список")
    string = input()
    my_string = string.lower()
    list_to_search = input()
    my_list_to_search = list_to_search.lower()
    if my_string in my_list_to_search:
        print(True)
    else:
        print(False)
    count_calls()


string_info()
string_info()
is_contains()
is_contains()
print(calls)
