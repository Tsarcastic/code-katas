def accum(s):
    # your code
    l = len(s)
    the_string = ""
    cnt = 0
    while l > 0:
        the_string += (s[cnt] * (1)).upper()
        the_string += (s[cnt] * (cnt)).lower() + "-"
        l += -1
        cnt += 1
    the_string = the_string[:-1]
    return the_string