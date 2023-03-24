def palindrome (list_input):
    check = False

    if len(list_input) <= 1:
        check = True
        return check
    else:
        half_len = int(len(list_input)/2)

        for i in range(0, half_len):
            if list_input[i] == list_input[len(list_input) - i - 1]:
                check = True
            else:
                check = False

        return check
