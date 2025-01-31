def longest(string_list):
    largest_length = 0
    for string in string_list:
        if len(string) > largest_length:
            largest_length = len(string)
    for string in string_list:
        if len(string) == largest_length:
            print(string)