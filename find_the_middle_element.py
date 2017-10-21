def gimme(input_array):
    # Implement this function
    if input_array[0] > input_array[1] and input_array[0] < input_array[2]:
        return 0
    elif input_array[0] < input_array[1] and input_array[0] > input_array[2]:
        return 0
    elif input_array[1] < input_array[0] and input_array[1] > input_array[2]:
        return 1
    elif input_array[1] > input_array[0] and input_array[1] < input_array[2]:
        return 1
    else:
        return 2