def expanded_form(num):
    x = str(num)
    the_string = ""

    for count, value in enumerate(x):
        if int(x[count]) > 0:
            y = x[count] + ('0' * (len(x) - count - 1))
            the_string += y + " + "
    return the_string[:-3]