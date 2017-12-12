"""

Kata: Mumbling.
Best Practice By coldbydauph & others
def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))
"""


def accum(s):
    """Mumble up some strings."""
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
