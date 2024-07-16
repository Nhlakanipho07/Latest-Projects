def columns(string_list):

    if string_list != []:
        max_length = len(max(string_list, key=len))
        adjust_length = [string.ljust(max_length) for string in string_list]

        for string_index in range(max_length):
            string_column = [
                string[string_index : string_index + 1] for string in adjust_length
            ]
            print(" ".join(string_column))
