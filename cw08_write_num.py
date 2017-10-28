"""Kata: Write Number in Expanded Form
Best Practice by zebulan and sriddle
def expanded_form(n):
    result = []
    for a in range(len(str(n)) - 1, -1, -1):
        current = 10 ** a
        quo, n = divmod(n, current)
        if quo:
            result.append(str(quo * current))
    return ' + '.join(result)
"""


def expanded_form(num):
    x = str(num)
    the_string = ""

    for count, value in enumerate(x):
        if int(x[count]) > 0:
            y = x[count] + ('0' * (len(x) - count - 1))
            the_string += y + " + "
    return the_string[:-3]