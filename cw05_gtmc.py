"""
Kata: Get the Middle Character.

Best practice by hiasen and others:
def get_middle(s):
   return s[(len(s)-1)/2:len(s)/2+1]
"""


def get_middle(s):
    """Get the middle."""
    size = len(s)
    if size % 2 != 0:
        return s[int(size / 2)]
    else:
        return s[int(round(size / 2) - 1)] + s[int(round(size / 2))]
