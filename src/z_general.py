def fix(this_input):

    if type(this_input) == float:
        num = round(this_input, 3)
        if str(num).split('.')[1] != 0:
            return num
        else:
            return str(num).split('.')[0]

    elif type(this_input) == list:
        for index in range(len(this_input)):
            if type(this_input[index]) == float:
                this_input[index] = fix(this_input[index])
        return this_input

    else:
        return this_input